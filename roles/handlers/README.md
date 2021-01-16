# bcrisp4.postfix.handlers

Helper role that provides some common Ansible handlers for use in other Postfix roles

## Role Variables

| Variable | Default | Description |
|-|-|-|
| postfix_service_name | "postfix" | The name of the Psotfix service |

## Handlers
### `restart postfix`
Issues a restart of the Postfix service

### `reload postfix`
Issues a reload of the Postfix service

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
