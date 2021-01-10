# bcrisp4.postfix.install ![bcrisp4.postfix.install](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.install/badge.svg)

Install Postfix

## Role Variables

| Variable                | Default   | Description                                                                      |
|-------------------------|-----------|----------------------------------------------------------------------------------|
| postfix_package_name    | "postfix" | Name of the Postfix package that should be installed from the OS package manager |
| postfix_package_version | ""        | Optionally specify a version for the Postfix package                             |

## Example Playbook

```yaml
- hosts: 127.0.0.1
  tasks:
    - import_role:
        name: bcrisp4.postfix.install

```
## Supported Platforms

- Debian
  - Stretch (9)
  - Buster (10)
- Ubuntu
  - Bionic (18.04)
  - Focal (20.04)
- EL (CentOS)
  - 7
  - 8
- Fedora
  - 31
  - 32

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
