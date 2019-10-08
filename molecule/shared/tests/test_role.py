import pytest

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
  ('awscli'),
])
def test_awscli_is_installed(host, name):
    packages = host.pip_package.get_packages()
    assert name in packages


@pytest.mark.parametrize('username,groupname,s3_config', [
  ('test_user', 'test_group', 's3'),
])
def test_awscli_config_file(host, username, groupname, s3_config):
    awscli_config = host.file('/home/' + username + '/.aws/config')
    assert awscli_config.exists
    assert awscli_config.is_file
    assert awscli_config.user == username
    assert awscli_config.group == groupname
    assert awscli_config.contains(s3_config)


@pytest.mark.parametrize('username,groupname', [
  ('test_user', 'test_group'),
])
def test_awscli_credentials_file(host, username, groupname):
    awscli_config = host.file('/home/' + username + '/.aws/credentials')
    assert awscli_config.exists
    assert awscli_config.is_file
    assert awscli_config.user == username
    assert awscli_config.group == groupname
