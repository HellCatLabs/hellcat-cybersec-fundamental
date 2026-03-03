"""
Tests for 05-misc module.
Covers: DNS resolver, fake user generator, log spammer.
"""

import os
import sys
import csv
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


# ── dns_resolver ─────────────────────────────────────────────────────────────

class TestDnsResolver:
    def test_resolve_known_domain(self):
        """resolve() should return at least one IP for a well-known domain."""
        mod = _load_module(
            "resolve",
            os.path.join(ROOT, "05-misc", "dns_resolver", "resolve.py"),
        )
        ips = mod.resolve("localhost")
        assert len(ips) >= 1
        assert any("127" in ip for ip in ips)

    def test_resolve_invalid_returns_empty(self):
        """resolve() should return empty list for an invalid domain."""
        mod = _load_module(
            "resolve",
            os.path.join(ROOT, "05-misc", "dns_resolver", "resolve.py"),
        )
        ips = mod.resolve("this.domain.does.not.exist.zzz")
        assert ips == []

    def test_cli_help(self):
        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "05-misc", "dns_resolver", "resolve.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "targets" in result.stdout.lower()


# ── fake_usergen ─────────────────────────────────────────────────────────────

class TestFakeUsergen:
    def test_gen_user_returns_expected_keys(self):
        """gen_user() should return a dict with all expected fields."""
        mod = _load_module(
            "generate_users",
            os.path.join(ROOT, "05-misc", "fake_usergen", "generate_users.py"),
        )
        user = mod.gen_user()
        for key in ["username", "email", "password_plain", "password_hash", "created_at"]:
            assert key in user, f"Missing key: {key}"

    def test_gen_user_email_format(self):
        """Generated email should contain @ and a dot."""
        mod = _load_module(
            "generate_users",
            os.path.join(ROOT, "05-misc", "fake_usergen", "generate_users.py"),
        )
        user = mod.gen_user()
        assert "@" in user["email"]
        assert "." in user["email"].split("@")[1]

    def test_password_hash_is_sha256(self):
        """Password hash should be 64 hex characters (SHA-256)."""
        mod = _load_module(
            "generate_users",
            os.path.join(ROOT, "05-misc", "fake_usergen", "generate_users.py"),
        )
        user = mod.gen_user()
        assert len(user["password_hash"]) == 64
        int(user["password_hash"], 16)  # should be valid hex

    def test_main_creates_csv(self):
        """main() should create a valid CSV with the requested number of rows."""
        mod = _load_module(
            "generate_users",
            os.path.join(ROOT, "05-misc", "fake_usergen", "generate_users.py"),
        )
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            path = f.name
        try:
            mod.main(path, 5)
            assert os.path.exists(path)
            with open(path) as csvf:
                reader = csv.DictReader(csvf)
                rows = list(reader)
            assert len(rows) == 5
            assert "username" in rows[0]
        finally:
            os.unlink(path)


# ── log_spammer ──────────────────────────────────────────────────────────────

class TestLogSpammer:
    def test_gen_line_format(self):
        """gen_line() should return a string with expected log structure."""
        mod = _load_module(
            "spam_logs",
            os.path.join(ROOT, "05-misc", "log_spammer", "spam_logs.py"),
        )
        line = mod.gen_line()
        assert "Z " in line  # timestamp
        assert "src=" in line
        assert 'msg="' in line

    def test_gen_line_contains_valid_level(self):
        """gen_line() should include a valid log level."""
        mod = _load_module(
            "spam_logs",
            os.path.join(ROOT, "05-misc", "log_spammer", "spam_logs.py"),
        )
        valid_levels = {"INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL"}
        line = mod.gen_line()
        found = any(level in line for level in valid_levels)
        assert found, f"No valid log level found in: {line}"

    def test_cli_limited_output(self):
        """Running with -n 3 should produce exactly 3 lines."""
        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "05-misc", "log_spammer", "spam_logs.py"), "-n", "3", "-r", "1000"],
            capture_output=True, text=True, timeout=10,
        )
        lines = [l for l in result.stdout.strip().split("\n") if l]
        assert len(lines) == 3
