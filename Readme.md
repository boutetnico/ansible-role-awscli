ansible-role-awscli
===================

This role installs and configures AWS Command Line Interface.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable          | Required | Default            | Choices   | Comments                                          |
|-------------------|----------|--------------------|-----------|---------------------------------------------------|
| awscli_users      | true     | `[]`               | list      | Main configuration list. See `defaults/main.yml`. |

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
