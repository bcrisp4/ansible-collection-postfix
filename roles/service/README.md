# bcrisp4.postfix.service ![bcrisp4.postfix.service(https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.service/badge.svg)

Manage Postfix service state

## Role Variables

| Variable | Default | Description |
|-|-|-|
| postfix_service_name | "postfix" | The name of the Psotfix service |
| postfix_service_state | "started" | The desired state of the Postfix service. One of "started", "stopped", "restarted" or "reloaded" |
| postfix_service_enabled | true | Should the Postfix service be enabled so that it starts on boot? |

## Example Playbook

```yaml
- hosts: 127.0.0.1
  tasks:
    - import_role:
        name: bcrisp4.postfix.service

```
The above would ensure that `postfix` is started and enabled

```yaml
- hosts: 127.0.0.1
  vars:
    postfix_service_state: stopped
    postfix_service_enabled: false
  tasks:
    - import_role:
        name: bcrisp4.postfix.service

```
The above would ensure that `postfix` is stopped and disabled

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
