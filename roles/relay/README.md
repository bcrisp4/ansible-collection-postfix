# bcrisp4.postfix.relay

Configure Postfix as an SMTP relay server.

Default configuration provides a local-only relay (i.e. only the local server itself has relay access)

## Role Variables

| Variable | Default | Description |
|-|-|-|
| postfix_relay_config_dir | "/etc/postfix" | Path to the Postfix configuration directory |
| postfix_relay_config_file_owner | "root" | The user that should own the Postfix config file. |
| postfix_relay_config_file_group | "root" | The group that should own the Postfix config file. |
| postfix_relay_config_file_mode | "ugo=r" | The permissions of the Postfix config file. |
| postfix_relay_relayhost_name | "" | The hostname of the upstream SMTP server to relay to. You need to set this to something. See: <http://www.postfix.org/postconf.5.html#relayhost> |
| postfix_relay_relayhost_port | 587 | The port of the upstream SMTP server. See: <http://www.postfix.org/postconf.5.html#relayhost> |
| postfix_relay_relayhost_mx_lookups | false | Should MX lookup be enabled for the upstream SMTP server? See: <http://www.postfix.org/postconf.5.html#relayhost> |
| postfix_relay_myhostname | "{{ inventory_hostname }}" | The hostname  of your SMTP server. See: <http://www.postfix.org/postconf.5.html#myhostname> |
| postfix_relay_mydomain | "local" | The domain of your SMTP server. See: <http://www.postfix.org/postconf.5.html#mydomain> |
| postfix_relay_mydestination | ["$myhostname", "localhost.$mydomain", "$mydomain"] | The list of domains that are delivered via the $local_transport mail delivery transport. See: <http://www.postfix.org/postconf.5.html#mydestination> |
| postfix_relay_mynetworks | ["127.0.0.0/8"] | A list of networks that your SMTP server trusts. See: <http://www.postfix.org/postconf.5.html#mynetworks> |
| postfix_relay_interfaces | ["loopback-only"] | A list network interfaces that Postfix can receive mail from. See: <http://www.postfix.org/postconf.5.html#inet_interfaces> |
| postfix_relay_restrictions | ["permit_mynetworks", "permit_sasl_authenticated", "defer_unauth_destination"] | A list of access controls applied to the SMTP relay. See: <http://www.postfix.org/postconf.5.html#smtpd_relay_restrictions> |
| postfix_relay_sasl | false | Should SASL authentication be used when connecting to the upstream relay? See: <http://www.postfix.org/postconf.5.html#smtp_sasl_auth_enable> |
| postfix_relay_sasl_username | "" | The username to use for SASL authentication with the upstream relay. i.e. the bit before the @ |
| postfix_relay_sasl_domain | "" | The domain to use for SASL authentication with the upstream relay. i.e. the bit after the @ |
| postfix_relay_sasl_password | "" | The password to use for SASL authentication with the upstream relay. |
| postfix_relay_sasl_security_options | ["noanonymous"] | A list of SASL auth security options. See: <http://www.postfix.org/postconf.5.html#smtp_sasl_security_options> |
| postfix_relay_extra_config | {} | A dictionary of extra configuration parameters to apply. See: <https://github.com/bcrisp4/ansible-collection-postfix/tree/main/roles/config_file> |

You need to set `postfix_relay_relayhost_name` to something.  

If the upstream SMTP server enforces SASL authentication, you will also need to set `postfix_relay_sasl: true` and set: `postfix_relay_sasl_username`, `postfix_relay_sasl_domain` and `postfix_relay_sasl_password`.

## Example Playbook

```yaml
- hosts: 127.0.0.1
  vars:
    postfix_relay_relayhost_name: smtp.mailgun.org
    postfix_relay_sasl: true
    postfix_relay_sasl_username: user
    postfix_relay_sasl_domain: mg.example.org
    postfix_relay_sasl_password: sup3rsecUrpassw0rd!
  tasks:
    - import_role:
        name: bcrisp4.postfix.relay

```

The above would configure Postfix to relay emails sent by localhost to [Mailgun](https://www.mailgun.com/).

## Dependencies

This role makes use of several other roles in the `bcrisp4.postfix` collection:

- bcrisp4.postfix.install
- bcrisp4.postfix.config_file
- bcrisp4.postfix.service
- bcrisp4.postfix.handlers

## Supported Platforms

Written and tested on Debain Buster. Should work on any Debain or EL based Linux distro.

## License

MIT

## Author Information

Ben Crisp <ben@thecrisp.io>
