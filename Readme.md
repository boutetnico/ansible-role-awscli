ansible-role-awscli
===================

This role installs and configure AWS Command Line Interface.

[![Build Status](https://travis-ci.org/boutetnico/ansible-role-awscli.svg?branch=master)](https://travis-ci.org/boutetnico/ansible-role-awscli)

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------
- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 16.04 (Xenial Xerus)](http://releases.ubuntu.com/16.04/)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)


Role Variables
--------------

| Variable                     | Required | Default                         | Choices   | Comments                                      |
|------------------------------|----------|---------------------------------|-----------|-----------------------------------------------|
| awscli_user_home             | yes      | `/root`                         | string    |                                               |
| awscli_user                  | yes      | `root`                          | string    |                                               |
| awscli_group                 | yes      | `root`                          | string    |                                               |
| awscli_aws_access_key_id     | false    |                                 | string    |                                               |
| awscli_aws_secret_access_key | false    |                                 | string    |                                               |
| awscli_region                | false    |                                 | string    |                                               |
| awscli_s3_configuration      | false    | `[]`                            | list      | S3-specific config. See `defaults/main.yml`   |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - role: ansible-role-awscli
          awscli_user_home: /home/test_user
          awscli_user: test_user
          awscli_group: test_group
          awscli_aws_access_key_id: aaaa
          awscli_aws_secret_access_key: bbbb
          awscli_s3_configuration:
            - "use_accelerate_endpoint = false"


Testing
-------

## Debian

`molecule --base-config molecule/shared/base.yml test --scenario-name debian`

## Ubuntu

`molecule --base-config molecule/shared/base.yml test --scenario-name ubuntu`

License
-------

MIT

Author Information
------------------

[@boutetnico](https://github.com/boutetnico)
