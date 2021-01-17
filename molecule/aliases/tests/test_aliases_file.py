import os

import testinfra.utils.ansible_runner

INVENTORY = os.environ['MOLECULE_INVENTORY_FILE']
HOST_PATTERN = "all"

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    INVENTORY).get_hosts(HOST_PATTERN)

test_file_path = os.path.abspath(__file__)
test_dir = os.path.dirname(test_file_path)


def test_postfix_aliases_file_is_correct(host):
    with open(f'{test_dir}/files/output/aliases') as x:
        test_file_content = x.read()
    file = host.file("/etc/aliases")
    assert file.exists
    assert file.user == "root"
    assert file.group == "root"
    assert file.mode == 0o444
    assert file.content_string == test_file_content


def test_postfix_aliases_database_created(host):
    file = host.file("/etc/aliases.db")
    assert file.exists
