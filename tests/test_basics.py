"""
Tests for 01-basics module.
Covers: user info retrieval, file operations, MAC address generation.
"""

import os
import sys
import socket
import tempfile
import importlib.util
import pytest

# ── Helpers ──────────────────────────────────────────────────────────────────

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def _load_module(name, path):
    """Dynamically load a Python module from a file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ── 02_user_info ─────────────────────────────────────────────────────────────

class TestUserInfo:
    def test_getlogin_returns_string(self):
        """os.getlogin() or getpass.getuser() should return a non-empty string."""
        try:
            login = os.getlogin()
        except OSError:
            import getpass
            login = getpass.getuser()
        assert isinstance(login, str)
        assert len(login) > 0

    def test_gethostname_returns_string(self):
        """socket.gethostname() should return a non-empty string."""
        hostname = socket.gethostname()
        assert isinstance(hostname, str)
        assert len(hostname) > 0


# ── 04_file_ops ──────────────────────────────────────────────────────────────

class TestFileOps:
    def test_file_dropper_example_functions_exist(self):
        """file_dropper_example.py should define all expected functions."""
        mod = _load_module(
            "file_dropper_example",
            os.path.join(ROOT, "01-basics", "04_file_ops", "file_dropper_example.py"),
        )
        for fn_name in [
            "drop_text_file",
            "append_to_file",
            "drop_in_temp_folder",
            "drop_with_random_name",
            "write_binary_file",
            "overwrite_existing_file",
            "drop_to_startup",
        ]:
            assert hasattr(mod, fn_name), f"Missing function: {fn_name}"

    def test_drop_text_file_creates_file(self):
        """drop_text_file() should create a file with expected content."""
        mod = _load_module(
            "file_dropper_example",
            os.path.join(ROOT, "01-basics", "04_file_ops", "file_dropper_example.py"),
        )
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as tmp:
            path = tmp.name
        try:
            mod.drop_text_file(path)
            assert os.path.exists(path)
            with open(path) as f:
                assert "test drop" in f.read().lower()
        finally:
            os.unlink(path)

    def test_append_to_file_appends(self):
        """append_to_file() should add content without overwriting."""
        mod = _load_module(
            "file_dropper_example",
            os.path.join(ROOT, "01-basics", "04_file_ops", "file_dropper_example.py"),
        )
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w") as tmp:
            tmp.write("first line\n")
            path = tmp.name
        try:
            mod.append_to_file(path)
            with open(path) as f:
                content = f.read()
            assert "first line" in content
            assert "Appended" in content
        finally:
            os.unlink(path)


# ── 05_exo solutions ────────────────────────────────────────────────────────

class TestExerciseSolutions:
    def test_exo3_random_mac_format(self):
        """random_mac() should return a valid MAC format 02:xx:xx:xx:xx:xx."""
        mod = _load_module(
            "exo3",
            os.path.join(ROOT, "01-basics", "05_exo", "solution", "exo3_mac_randomizer.py"),
        )
        mac = mod.random_mac()
        parts = mac.split(":")
        assert len(parts) == 6, f"MAC should have 6 octets, got {len(parts)}"
        assert parts[0] == "02", "First octet should be 02 (locally-administered)"
        for p in parts:
            assert len(p) == 2, f"Each octet should be 2 hex chars, got '{p}'"
            int(p, 16)  # should not raise
