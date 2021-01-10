# bcrisp4.postfix.install ![bcrisp4.postfix.install](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.install/badge.svg)

Install Postfix

Currently only written to work on Debian.

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

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
