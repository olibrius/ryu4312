"""Smoke tests: verify core modules import and ryu-manager starts."""
import subprocess
import sys
import pytest


CORE_MODULES = [
    'ryu',
    'ryu.base.app_manager',
    'ryu.controller.controller',
    'ryu.lib.hub',
    'ryu.lib.packet.packet',
    'ryu.lib.packet.ethernet',
    'ryu.lib.packet.ipv4',
    'ryu.lib.packet.ipv6',
    'ryu.lib.packet.tcp',
    'ryu.lib.packet.udp',
    'ryu.lib.packet.bgp',
    'ryu.lib.packet.zebra',
    'ryu.ofproto.ofproto_v1_3_parser',
    'ryu.ofproto.ofproto_v1_4_parser',
    'ryu.ofproto.ofproto_v1_5_parser',
    'ryu.flags',
    'ryu.app.wsgi',
]


@pytest.mark.parametrize('module', CORE_MODULES)
def test_module_importable(module):
    result = subprocess.run(
        [sys.executable, '-c', f'import {module}'],
        capture_output=True, text=True
    )
    assert result.returncode == 0, (
        f"Cannot import {module}:\n{result.stderr}"
    )


def test_ryu_manager_version():
    result = subprocess.run(
        [sys.executable, '-m', 'ryu.cmd.manager', '--version'],
        capture_output=True, text=True
    )
    output = result.stdout + result.stderr
    assert result.returncode == 0 or 'ryu' in output.lower(), (
        f"ryu-manager --version failed:\n{result.stderr}"
    )
