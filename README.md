# Ansible Collection - bcrisp4.postfix

Install and configure Postfix

*WIP*

## Roles

### [bcrisp4.postfix.relay](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/relay)

Configures Postfix as an SMTP relay

### [bcrisp4.postfix.install](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/install) ![bcrisp4.postfix.install](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.install/badge.svg)

Installs the Postfix package

### [bcrisp4.postfix.service](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/service)

Manages the Postfix service state

### [bcrisp4.postfix.config_file](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/config_file) ![bcrisp4.postfix.config_file](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.config_file/badge.svg)

Generates Postfix configuration files.

### [bcrisp4.postfix.master_file](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/master_file) ![bcrisp4.postfix.master_file](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.master_file/badge.svg)

Generates Postfix master process configuration files.

### [bcrisp4.postfix.handlers](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/handlers)

Provides some common Ansible handler for other Postfix roles

## Todo
- [x] Role to install Postfix
- [x] Helper role to generate Postfix config files
- [x] Helper role to generate Postfix Master Process config files
- [x] Helper role to manage the Postfix service
- [ ] Testing and CI for the Postfix service role
- [x] Helper role to provide common handlers (e.g. reloading Postfix)
- [x] Role to configure Postfix as an SMTP relay
- [ ] Testing and CI for the Postfix relay role

## License

Released under the [MIT license](https://raw.githubusercontent.com/bcrisp4/ansible-collection-postfix/main/LICENSE.txt)
