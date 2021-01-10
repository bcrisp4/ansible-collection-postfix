import os

import testinfra.utils.ansible_runner

INVENTORY = os.environ['MOLECULE_INVENTORY_FILE']
HOST_PATTERN = "all"

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    INVENTORY).get_hosts(HOST_PATTERN)


def test_postfix_package_is_installed(host):
    postfix_package = "postfix"
    pkg = host.package(postfix_package)
    assert pkg.is_installed
