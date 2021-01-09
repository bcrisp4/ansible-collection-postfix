import os
import pytest

import testinfra.utils.ansible_runner

INVENTORY = os.environ['MOLECULE_INVENTORY_FILE']

SCENARIO = os.environ['MOLECULE_SCENARIO_NAME']
DISTRO = os.environ['MOLECULE_DISTRO'] if os.getenv(
    "MOLECULE_DISTRO") is not None else "debian"
DISTRO_VERSION = os.environ['MOLECULE_DISTRO_VERSION'] if os.getenv(
    "MOLECULE_DISTRO_VERSION") is not None else ""

HOST_PATTERN = f"molecule_{SCENARIO}_{DISTRO}_{DISTRO_VERSION}"

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    INVENTORY).get_hosts(HOST_PATTERN)


@pytest.mark.parametrize("package_name", [
    ("postfix"),
])
def test_postfix_package_is_installed(host, package_name):
    pkg = host.package(package_name)
    assert pkg.is_installed
