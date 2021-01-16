# bcrisp4.postfix.master_file ![bcrisp4.postfix.master_file(https://github.com/bcrisp4/ansible-collection-postfix/workflows/bcrisp4.postfix.master_file/badge.svg)

Manage Postfix configuration files

This role mostly exists to enable reuse of the Postfix config file Jinja template in other roles in this collection.

## Role Variables

| Variable | Default | Description |
|-|-|-|
| postfix_master_file_path | "/etc/postfix/master.cf" | The path that the Postfix master config file should be created at |
| postfix_master_file_owner | "root" | The user that should own Postfix master config file |
| postfix_master_file_group | "root" | The group that should own Postfix master config file |
| postfix_master_file_mode | "ug=r,o=" | The permissions that should be applied to Postfix master config file |
| postfix_master_file_config | [] | A list of dictionaries describing the Posfix master service configuration. See examples |
| postfix_master_file_handlers |  | An optional list of handlers to notify if the Postfix master config file has changed. |

## Example Playbook

```yaml
- hosts: 127.0.0.1
  variables:
    # This Postfix configuration serves only as an example. It is not complete.
    postfix_master_file_config:
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
      - service: rewrite
        type: unix
        chroot: true
        command: trivial-rewrite
      - service: ifmail
        type: unix
        unpriv: false
        chroot: false
        maxprox: 2
        command: pipe
        args:
          - flags=Fq.
          - user=bsmtp
          - argv=/usr/lib/bsmtp/bsmtp
          - -t$nexthop
          - -f$sender
          - $recipient
  tasks:
    - import_role:
        name: bcrisp4.postfix.master_file

```
The above would create `/etc/postfix/master.cf` like:
```
# Ansible managed: Do NOT edit this file manually!
# Docs: master(5) (http://www.postfix.org/master.5.html)

# ==========================================================================
# service type  private unpriv  chroot  wakeup  maxproc command + args
# (default)     (yes)   (yes)   (no)    (never) (100)
# ==========================================================================
smtp	inet	n	-	y	-	-	smtpd
pickup	unix	n	-	n	60	1	pickup
rewrite	unix	-	-	y	-	-	trivial-rewrite
ifmail	unix	-	n	n	-	-	pipe flags=Fq. user=bsmtp argv=/usr/lib/bsmtp/bsmtp -t$nexthop -f$sender $recipient
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