# bcrisp4.postfix.service
Manage Postfix service state

# Role Variables

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

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
