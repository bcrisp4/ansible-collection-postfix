# bcrisp4.postfix.config_file ![bcrisp4.postfix.config_file](https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.config_file/badge.svg)

Manage Postfix configuration files

## Role Variables

| Variable | Default | Description |
|-|-|-|
| postfix_config_file_path | "/etc/postfix/main.cf" | The path that the Postfix config file should be created at |
| postfix_config_file_owner | "root" | The user that should own Postfix config file |
| postfix_config_file_group | "root" | The group that should own Postfix config file |
| postfix_config_file_mode | "ug=r,o=" | The permissions that should be applied to Postfix config file |
| postfix_config_file_config | {} | A dictionary describing the Posfix configuration (i.e. main.cf). See examples |

## Example Playbook

```yaml
- hosts: 127.0.0.1
  variables:
    # This Postfix configuration serves only as an example. There is no guarantee
    # that it is valid or secure.
    postfix_config_file_config:
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
  tasks:
    - import_role:
        name: bcrisp4.postfix.config_file

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
