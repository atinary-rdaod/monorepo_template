import pytest
from util.env import require_env


def test_require_env_returns_value(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("FOO", "bar")
    assert require_env("FOO") == "bar"


def test_require_env_raises_when_missing(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("MISSING_VAR", raising=False)
    with pytest.raises(RuntimeError, match="MISSING_VAR"):
        require_env("MISSING_VAR")
