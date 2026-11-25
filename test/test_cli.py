"""Tests for the CLI flow."""

from axs_hasher import cli

DIGEST = "ungWv48Bz+pBQUDeXa4iI7ADYaOWF3qctBD/YfIAFa0="


class _Answer:  # pylint: disable=too-few-public-methods
    """Fake questionary question."""

    def __init__(self, value):
        self.value = value

    def ask(self):
        """Return the canned answer."""
        return self.value


def _patch(monkeypatch, algorithm, text, confirm):
    monkeypatch.setattr(cli.questionary, "select", lambda *a, **k: _Answer(algorithm))
    monkeypatch.setattr(cli.questionary, "text", lambda *a, **k: _Answer(text))
    monkeypatch.setattr(cli.questionary, "confirm", lambda *a, **k: _Answer(confirm))
    copied = []
    monkeypatch.setattr(cli.pyperclip, "copy", copied.append)
    return copied


def test_prints_and_copies(monkeypatch, capsys):
    """Digest is printed and copied when confirmed."""
    copied = _patch(monkeypatch, "SHA-256", "abc", True)
    cli.run()
    assert DIGEST in capsys.readouterr().out
    assert copied == [DIGEST]


def test_no_copy_when_declined(monkeypatch, capsys):
    """Nothing is copied when declined."""
    copied = _patch(monkeypatch, "SHA-256", "abc", False)
    cli.run()
    assert DIGEST in capsys.readouterr().out
    assert not copied


def test_cancel_exits_cleanly(monkeypatch, capsys):
    """Cancelling the prompt prints nothing."""
    copied = _patch(monkeypatch, None, "abc", True)
    cli.run()
    assert capsys.readouterr().out == ""
    assert not copied
