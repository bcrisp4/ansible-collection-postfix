# Ansible Collection - bcrisp4.postfix

Install and configure Postfix

*WIP*

## Roles

### [bcrisp4.postfix.install](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/install) ![bcrisp4.postfix.install](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.install/badge.svg)

Installs the Postfix package

### [bcrisp4.postfix.config_file](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/config_file) ![bcrisp4.postfix.config_file](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.config_file/badge.svg)

Generates Postfix configuration files. Mostly a helper role to allow reuse of the same Jinja template in other roles.

### [bcrisp4.postfix.master_file](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/master_file) ![bcrisp4.postfix.master_file](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.master_file/badge.svg)

Generates Postfix master process configuration files. Mostly a helper role to allow reuse of the same Jinja template in other roles.

### [bcrisp4.postfix.service](https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/service)

Manages the Postfix service state

## Todo
- [x] Role to install Postfix
- [x] Helper role to generate Postfix config files
- [x] Helper role to generate Postfix Master Process config files
- [x] Helper role to manage the Postfix service
- [ ] Helper role to provide common handlers (e.g. reloading Postfix)
- [ ] Role to configure Postfix as an SMTP relay

## License

Released under the [MIT license](https://raw.githubusercontent.com/bcrisp4/ansible-collection-postfix/main/LICENSE.txt)
