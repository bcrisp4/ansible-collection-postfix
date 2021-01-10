# bcrisp4.postfix.configure ![bcrisp4.postfix.configure](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.configure/badge.svg)

Configure Postfix

## Role Variables

| Variable                   | Default        | Description                                                                                             |
|----------------------------|----------------|---------------------------------------------------------------------------------------------------------|
| postfix_service_name       | "postfix"      | Name of the Postfix service                                                                             |
| postfix_service_state      | "started"      | The desired state of the Postfix service                                                                |
| postfix_service_enabled    | True           | Should the Postfix service be enabled?                                                                  |
| postfix_config_dir         | "/etc/postfix" | The path to the directory that Postfix config files should be created in                                |
| postfix_config_dir_owner   | "root"         | The user that should own the Postfix config directory                                                   |
| postfix_config_dir_group   | "root"         | The group that should own the Postfix config directory                                                  |
| postfix_config_dir_mode    | "u=rwx,go=rx"  | The permissions that should be applied to the Postfix config directory                                  |
| postfix_config_file_main   | "main.cf"      | The path where the main Postfix config file should be created, relative to postfix_config_dir           |
| postfix_config_file_master | "master.cf"    | The path where the Postfix master process config file should be created, relative to postfix_config_dir |
| postfix_config_file_owner  | "root"         | The user that should own Postfix config files                                                           |
| postfix_config_file_group  | "root"         | The group that should own Postfix config files                                                          |
| postfix_config_file_mode   | "ug=r,o="      | The permissions that should be applied to Postfix config files                                          |
| postfix_config_main        | {}             | A dictionary describing the main Posfix config (i.e. main.cf). See examples.                            |
| postfix_config_master      | {}             | A dictionary describing the Posfix master process config (i.e. main.cf). See examples.                  |

## Dependencies
### Roles
- TODO

## Example Playbook

```yaml
- hosts: 127.0.0.1
  variables:
    # This Postfix configuration serves only as an example. There is no guarantee
    # that it is valid or secure.
    postfix_config_main:
      smtpd_banner: $myhostname ESMTP $mail_name (Debian/GNU)
      biff: false
      append_dot_mydomain: false
      readme_directory: false
      compatibility_level: 2
      smtpd_tls_cert_file: /etc/ssl/certs/ssl-cert-snakeoil.pem
      smtpd_tls_key_file: /etc/ssl/private/ssl-cert-snakeoil.key
      smtpd_use_tls: yes
      smtpd_tls_session_cache_database: btree:${data_directory}/smtpd_scache
      smtp_tls_session_cache_database: btree:${data_directory}/smtp_scache
      smtpd_relay_restrictions: permit_mynetworks permit_sasl_authenticated defer_unauth_destination
      myhostname: mail.example.org
      alias_maps: hash:/etc/aliases
      alias_database: hash:/etc/aliases
      myorigin: /etc/mailname
      mydestination: 
        - $myhostname
        - example.org
        - localhost.localdomain
        - localhost
      relayhost: '' 
      mynetworks: 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
      mailbox_size_limit: 0
      recipient_delimiter: +
      inet_interfaces: all
      inet_protocols: all
    # The following is not a complete or valid Postfix master process configuration.
    # It serves only as a demonstration.
    postfix_config_master:
      - service: smtp 
        type: inet
        private: false
        chroot: true
        command: smtpd
      - service: pickup
        type: unix
        private: false
        unprivileged: true
        chroot: false
        wakeup: 60
        maxproc: 1
        command: pickup
  tasks:
    - import_role:
        name: bcrisp4.postfix.configure

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
