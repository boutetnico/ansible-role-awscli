[![tests](https://github.com/boutetnico/ansible-role-awscli/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-awscli/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.awscli-blue.svg)](https://galaxy.ansible.com/boutetnico/awscli)

ansible-role-awscli
===================

This role installs and configures [AWS Command Line Interface](https://aws.amazon.com/cli/).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                   | Required | Default       | Choices   | Comments                                          |
|----------------------------|----------|---------------|-----------|---------------------------------------------------|
| awscli_users               | true     | `[]`          | list      | Main configuration list. See `defaults/main.yml`. |
| awscli_package_state       | true     | `present`     | string    | Use `latest` to upgrade.                          |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-awscli
          awscli_users:
            - name: test_user
              group: test_group
              home: /home/test_user
              aws_access_key_id: aaaa
              aws_secret_access_key: bbbb
              s3_configuration:
                - "use_accelerate_endpoint = false"


Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
