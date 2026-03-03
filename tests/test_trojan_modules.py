"""
Tests for 04-keyloggers-trojans module.
Tests the modular architecture (exfil, autostart) and CLI.
"""

import os
import sys
import subprocess
import importlib.util
import tempfile
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ── modules/autostart ───────────────────────────────────────────────────────

class TestAutostart:
    def test_simulate_persistence_exists(self):
        """autostart.py should define simulate_persistence()."""
        mod = _load_module(
            "autostart",
            os.path.join(ROOT, "04-keyloggers-trojans", "modules", "autostart.py"),
        )
        assert hasattr(mod, "simulate_persistence")
        assert callable(mod.simulate_persistence)

    def test_simulate_persistence_runs(self, capsys):
        """simulate_persistence() should print simulation output."""
        mod = _load_module(
            "autostart",
            os.path.join(ROOT, "04-keyloggers-trojans", "modules", "autostart.py"),
        )
        mod.simulate_persistence()
        captured = capsys.readouterr()
        assert "Simulating" in captured.out or "persistence" in captured.out.lower()


# ── modules/exfil ────────────────────────────────────────────────────────────

class TestExfilModule:
    def test_send_keylog_function_exists(self):
        """exfil.py should define send_keylog()."""
        mod = _load_module(
            "exfil",
            os.path.join(ROOT, "04-keyloggers-trojans", "modules", "exfil.py"),
        )
        assert hasattr(mod, "send_keylog")
        assert callable(mod.send_keylog)

    def test_send_keylog_no_file_handles_gracefully(self, capsys):
        """send_keylog() should warn if file doesn't exist."""
        mod = _load_module(
            "exfil",
            os.path.join(ROOT, "04-keyloggers-trojans", "modules", "exfil.py"),
        )
        # Call with a nonexistent file path
        mod.send_keylog(filepath="/tmp/this_file_does_not_exist_12345.txt")
        captured = capsys.readouterr()
        assert "No keylog" in captured.out or "not found" in captured.out.lower()


# ── server/default_exfil_server ──────────────────────────────────────────────

class TestExfilServerCLI:
    def test_server_help(self):
        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "04-keyloggers-trojans", "server", "default_exfil_server.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "--port" in result.stdout
        assert "--save-dir" in result.stdout


# ── trojan.py CLI ────────────────────────────────────────────────────────────

pynput_available = importlib.util.find_spec("pynput") is not None


@pytest.mark.skipif(not pynput_available, reason="pynput not installed")
class TestTrojanCLI:
    def test_trojan_help(self):
        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "04-keyloggers-trojans", "trojan.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "--interval" in result.stdout
