import { useCallback, useEffect, useState } from "react";

import { client } from "./api/client";

type Notification = {
  id: string;
  recipient: string;
  subject: string;
  status: "PENDING" | "SENT" | "FAILED";
  created_at: string;
  sent_at: string | null;
};

export function App() {
  const [notifications, setNotifications] = useState<Notification[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [recipient, setRecipient] = useState("demo@example.com");
  const [subject, setSubject] = useState("hello");
  const [body, setBody] = useState("hi there");

  const refresh = useCallback(() => {
    client
      .GET("/api/notifications/")
      .then((res) => {
        if (res.error) setError("Failed to load notifications");
        else setNotifications(res.data as Notification[]);
      })
      .catch(() => setError("Backend not reachable"));
  }, []);

  useEffect(() => {
    refresh();
    // Poll while anything is pending so the UI flips to SENT without a manual refresh.
    const interval = setInterval(refresh, 1000);
    return () => clearInterval(interval);
  }, [refresh]);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    const res = await client.POST("/api/notifications/", {
      body: { recipient, subject, body },
    } as never);
    if (res.error) setError("Failed to send");
    else refresh();
  };

  return (
    <main style={{ fontFamily: "system-ui, sans-serif", padding: "2rem", maxWidth: 720 }}>
      <h1>Monorepo template</h1>
      <p>
        POSTs a notification to the Django API. The request returns immediately;
        a Celery worker simulates "sending" (a 2-second sleep) and flips the
        status to <code>SENT</code>. The list below polls every second.
      </p>

      <form onSubmit={submit} style={{ display: "grid", gap: "0.5rem", marginBottom: "1.5rem" }}>
        <input value={recipient} onChange={(e) => setRecipient(e.target.value)} placeholder="recipient" />
        <input value={subject} onChange={(e) => setSubject(e.target.value)} placeholder="subject" />
        <textarea value={body} onChange={(e) => setBody(e.target.value)} placeholder="body" rows={3} />
        <button type="submit">Send</button>
      </form>

      {error && <p style={{ color: "crimson" }}>{error}</p>}

      <ul>
        {notifications.map((n) => (
          <li key={n.id}>
            <strong>{n.subject}</strong> → {n.recipient} — <em>{n.status}</em>
          </li>
        ))}
      </ul>
      {notifications.length === 0 && !error && <p>No notifications yet. Submit the form above.</p>}
    </main>
  );
}
