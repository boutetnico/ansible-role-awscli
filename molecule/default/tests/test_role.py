import pytest


@pytest.mark.parametrize(
    "package",
    [
        "python3-pip",
    ],
)
def test_dependencies_installed(host, package):
    pkg = host.package(package)
    assert pkg.is_installed


@pytest.mark.parametrize(
    "name",
    [
        ("awscli"),
    ],
)
def test_awscli_is_installed(host, name):
    packages = host.pip.get_packages(pip_path="pip3")
    assert name in packages


def test_awscli_command_works(host):
    cmd = host.run("aws --version")
    assert cmd.rc == 0
    assert "aws-cli" in cmd.stdout or "aws-cli" in cmd.stderr


@pytest.mark.parametrize(
    "username,directory,mode",
    [
        ("test_user", "/home/test_user/.aws", 0o755),
        ("test_user2", "/home/test_user2/.aws", 0o755),
    ],
)
def test_aws_directory_exists(host, username, directory, mode):
    d = host.file(directory)
    assert d.exists
    assert d.is_directory
    assert d.user == username
    assert d.mode == mode


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
    assert awscli_config.mode == 0o644
    assert awscli_config.contains(s3_config)


@pytest.mark.parametrize(
    "username,groupname,key,secret",
    [
        ("test_user", "test_group", "aaaa", "bbbb"),
        ("test_user2", "test_group", "cccc", "dddd"),
    ],
)
def test_awscli_credentials_file(host, username, groupname, key, secret):
    awscli_credentials = host.file("/home/" + username + "/.aws/credentials")
    assert awscli_credentials.exists
    assert awscli_credentials.is_file
    assert awscli_credentials.user == username
    assert awscli_credentials.group == groupname
    assert awscli_credentials.mode == 0o600
    assert awscli_credentials.contains(key)
    assert awscli_credentials.contains(secret)
