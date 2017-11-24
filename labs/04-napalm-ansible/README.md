# NAPALM with Ansible:
- This is about consuming napalm from Ansible
- https://github.com/napalm-automation/napalm-ansible

## Content:
- 
- 

## Installation:
- Follow the installation instructions [here](http://napalm.readthedocs.io/en/latest/tutorials/ansible-napalm.html)
- Below few captures as an example:
```
mab@mab-infra:~$  napalm-ansible
To make sure ansible can make use of the napalm modules you will have
to add the following configurtion to your ansible configureation
file, i.e. `./ansible.cfg`:

    [defaults]
    library = /home/mab/.local/lib/python2.7/site-packages/napalm_ansible

For more details on ansible's configuration file visit:
https://docs.ansible.com/ansible/latest/intro_configuration.html
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ cat ~/mab_automate/napalm/labs/04-napalm-ansible/ansible.cfg 
[defaults]
library = /home/mab/.local/lib/python2.7/site-packages/napalm_ansible
inventory = hosts
# the below is for Ansible 2.3 and above
host_key_checking = Falsemab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ ll /home/mab/.local/lib/python2.7/site-packages/napalm_ansible
total 164
drwxrwxr-x   2 mab mab  4096 oct.  22 13:05 ./
drwx------ 157 mab mab 12288 nov.  15 16:40 ../
-rw-rw-r--   1 mab mab   447 nov.  15 16:40 __init__.py
-rw-rw-r--   1 mab mab   796 nov.  15 16:40 __init__.pyc
-rw-rw-r--   1 mab mab  5281 nov.  15 16:40 napalm_cli.py
-rw-rw-r--   1 mab mab  4428 nov.  15 16:40 napalm_cli.pyc
-rw-rw-r--   1 mab mab  3409 nov.  15 16:40 napalm_diff_yang.py
-rw-rw-r--   1 mab mab  3813 nov.  15 16:40 napalm_diff_yang.pyc
-rw-rw-r--   1 mab mab  9912 nov.  15 16:40 napalm_get_facts.py
-rw-rw-r--   1 mab mab  8366 nov.  15 16:40 napalm_get_facts.pyc
-rw-rw-r--   1 mab mab 11481 nov.  15 16:40 napalm_install_config.py
-rw-rw-r--   1 mab mab 10012 nov.  15 16:40 napalm_install_config.pyc
-rw-rw-r--   1 mab mab  9367 nov.  15 16:40 napalm_parse_yang.py
-rw-rw-r--   1 mab mab  8760 nov.  15 16:40 napalm_parse_yang.pyc
-rw-rw-r--   1 mab mab  8186 nov.  15 16:40 napalm_ping.py
-rw-rw-r--   1 mab mab  6309 nov.  15 16:40 napalm_ping.pyc
-rw-rw-r--   1 mab mab  3555 nov.  15 16:40 napalm_translate_yang.py
-rw-rw-r--   1 mab mab  3801 nov.  15 16:40 napalm_translate_yang.pyc
-rw-rw-r--   1 mab mab  8306 nov.  15 16:40 napalm_validate.py
-rw-rw-r--   1 mab mab  7608 nov.  15 16:40 napalm_validate.pyc
mab@mab-infra:~$ 
mab@mab-infra:~$ 
```
