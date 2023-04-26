import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "name",
    [
        ("awscli"),
    ],
)
def test_awscli_is_installed(host, name):
    packages = host.pip.get_packages(pip_path="pip3")
    assert name in packages


@pytest.mark.parametrize(
    "username,groupname,s3_config",
    [
        ("test_user", "test_group", "s3"),
    ],
)
def test_awscli_config_file(host, username, groupname, s3_config):
    awscli_config = host.file("/home/" + username + "/.aws/config")
    assert awscli_config.exists
    assert awscli_config.is_file
    assert awscli_config.user == username
    assert awscli_config.group == groupname
    assert awscli_config.contains(s3_config)


@pytest.mark.parametrize(
    "username,groupname,key,secret",
    [
        ("test_user", "test_group", "aaaa", "bbbb"),
    ],
)
def test_awscli_credentials_file(host, username, groupname, key, secret):
    awscli_credentials = host.file("/home/" + username + "/.aws/credentials")
    assert awscli_credentials.exists
    assert awscli_credentials.is_file
    assert awscli_credentials.user == username
    assert awscli_credentials.group == groupname
    assert awscli_credentials.contains(key)
    assert awscli_credentials.contains(secret)
