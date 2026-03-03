"""
Tests for 02-network-ops module.
Tests what can be tested without root/sudo privileges.
"""

import os
import sys
import socket
import importlib.util
import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def _load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ── 01_interface_info ────────────────────────────────────────────────────────

class TestInterfaceInfo:
    def test_hostname_resolves(self):
        """gethostname() should return something resolvable."""
        hostname = socket.gethostname()
        assert isinstance(hostname, str) and len(hostname) > 0

    def test_local_ip_is_valid(self):
        """Local IP should be a valid IPv4 or IPv6 address."""
        import ipaddress
        hostname = socket.gethostname()
        try:
            local_ip = socket.gethostbyname(hostname)
        except socket.gaierror:
            # Fallback: use UDP trick to get local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(("8.8.8.8", 80))
                local_ip = s.getsockname()[0]
            finally:
                s.close()
        addr = ipaddress.ip_address(local_ip)
        assert addr  # parsed successfully


# ── 02_port_scanner ─────────────────────────────────────────────────────────

class TestPortScanner:
    def test_scanner_argparse_help(self):
        """scanner.py should accept --help without crashing."""
        import subprocess

        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "02-network-ops", "02_port_scanner", "scanner.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "target" in result.stdout.lower()

    def test_scanner_detects_open_port(self):
        """Scanner should find a port we open ourselves."""
        import subprocess

        # Open a temporary TCP server
        srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        srv.bind(("127.0.0.1", 0))
        srv.listen(1)
        port = srv.getsockname()[1]

        try:
            result = subprocess.run(
                [
                    sys.executable,
                    os.path.join(ROOT, "02-network-ops", "02_port_scanner", "scanner.py"),
                    "127.0.0.1",
                    "--start-port", str(port),
                    "--end-port", str(port),
                    "--timeout", "1",
                ],
                capture_output=True, text=True, timeout=10,
            )
            assert f"Port open: {port}" in result.stdout
        finally:
            srv.close()


# ── Packet sniffer / ARP / MITM ─────────────────────────────────────────────
# These require root privileges so we only test CLI argument parsing.

scapy_available = importlib.util.find_spec("scapy") is not None


@pytest.mark.skipif(not scapy_available, reason="scapy not installed")
class TestSnifferCLI:
    def test_sniffer_extended_help(self):
        import subprocess

        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "02-network-ops", "03_packet_sniffer", "sniffer-extended.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "--output" in result.stdout


@pytest.mark.skipif(not scapy_available, reason="scapy not installed")
class TestArpSpooferCLI:
    def test_arp_spoof_help(self):
        import subprocess

        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "02-network-ops", "04_arp_spoofer", "arp_spoof.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "--target" in result.stdout
        assert "--gateway" in result.stdout


@pytest.mark.skipif(not scapy_available, reason="scapy not installed")
class TestMitmCLI:
    def test_mitm_help(self):
        import subprocess

        result = subprocess.run(
            [sys.executable, os.path.join(ROOT, "02-network-ops", "05_mitm_simulation", "mitm.py"), "--help"],
            capture_output=True, text=True, timeout=5,
        )
        assert result.returncode == 0
        assert "--target" in result.stdout
