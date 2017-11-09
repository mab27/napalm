# Lab2

## Overview:
- Writing custom workflows based on standard actions from the NAPALM pack.
- Goal is to iterate againse the list of device in the inveotry list

## Getters (show commands):

- get_facts_all:
```
mab@mab-infra:~$ st2 run napalm.get_facts_all
..............
id: 5a04a3e67cae22371c88a76a
action.ref: napalm.get_facts_all
parameters: None
status: failed
result_task: end_task
result: 
  failed: false
  return_code: 0
  succeeded: true
start_timestamp: 2017-11-09T18:52:22.395654Z
end_timestamp: 2017-11-09T18:52:50.607687Z
+--------------------------+------------------------+---------------+--------------------+-------------------------------+
| id                       | status                 | task          | action             | start_timestamp               |
+--------------------------+------------------------+---------------+--------------------+-------------------------------+
| 5a04a3e67cae22371c88a76d | succeeded (2s elapsed) | get_inventory | napalm.file_to_obj | Thu, 09 Nov 2017 18:52:22 UTC |
| 5a04a3e87cae22371c88a76f | failed (6s elapsed)    | get_facts     | napalm.get_facts   | Thu, 09 Nov 2017 18:52:24 UTC |
| 5a04a3e87cae22371c88a773 | succeeded (8s elapsed) | get_facts     | napalm.get_facts   | Thu, 09 Nov 2017 18:52:24 UTC |
| 5a04a3e87cae22371c88a774 | failed (6s elapsed)    | get_facts     | napalm.get_facts   | Thu, 09 Nov 2017 18:52:24 UTC |
| 5a04a3e87cae22371c88a775 | succeeded (3s elapsed) | get_facts     | napalm.get_facts   | Thu, 09 Nov 2017 18:52:24 UTC |
| 5a04a3f27cae22371c88a777 | succeeded (0s elapsed) | end_task      | core.noop          | Thu, 09 Nov 2017 18:52:34 UTC |
+--------------------------+------------------------+---------------+--------------------+-------------------------------+
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 execution get 5a04a3e67cae22371c88a76d
id: 5a04a3e67cae22371c88a76d
status: succeeded (2s elapsed)
parameters: 
  file_location: home/mab/mab_automate/napalm/inventory/inventory.yml
result: 
  exit_code: 0
  result:
    arista1:
      bgp_config: config_variables/arista1.yml
      driver: eos
      hostname: par.arista1
      mgmt_ip: 192.168.0.70
      password: admin123
      username: admin
    arista2:
      bgp_config: config_variables/arista2.yml
      driver: eos
      hostname: par.arista2
      mgmt_ip: 192.168.0.80
      password: admin123
      username: admin
    vmx1:
      bgp_config: config_variables/vmx1.yml
      driver: junos
      hostname: lon.vmx1
      mgmt_ip: 192.168.0.30
      password: mab123
      username: mab
    vmx2:
      bgp_config: config_variables/vmx2.yml
      driver: junos
      hostname: lon.vmx2
      mgmt_ip: 192.168.0.40
      password: mab123
      username: mab
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 execution get 5a04a3e87cae22371c88a775
id: 5a04a3e87cae22371c88a775
status: succeeded (3s elapsed)
parameters: 
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
      fqdn: arista1
      hostname: arista1
      interface_list:
      - Ethernet1
      - Management1
      model: vEOS
      os_version: 4.18.1F-4591672.4181F
      serial_number: ''
      uptime: 12477
      vendor: Arista
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 execution get 5a04a3e87cae22371c88a773
id: 5a04a3e87cae22371c88a773
status: succeeded (8s elapsed)
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      fqdn: vmx1
      hostname: vmx1
      interface_list:
      - ge-0/0/0
      - lc-0/0/0
      - pfe-0/0/0
      - pfh-0/0/0
      - ge-0/0/1
      - ge-0/0/2
      - ge-0/0/3
      - ge-0/0/4
      - ge-0/0/5
      - ge-0/0/6
      - ge-0/0/7
      - ge-0/0/8
      - ge-0/0/9
      - .local.
      - cbp0
      - demux0
      - dsc
      - em1
      - em2
      - em3
      - em4
      - em5
      - em6
      - em7
      - em8
      - em9
      - fxp0
      - gre
      - ipip
      - irb
      - lo0
      - lsi
      - mtun
      - pimd
      - pime
      - pip0
      - pp0
      - tap
      - vtep
      model: VMX
      os_version: 14.1R4.9
      serial_number: VM55E771B3CD
      uptime: 6228
      vendor: Juniper
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

- get_bgp_confg_all:
```
mab@mab-infra:~$ st2 run napalm.get_bgp_config_all
..............
id: 5a04a44c7cae22371c88a779
action.ref: napalm.get_bgp_config_all
parameters: None
status: failed
result_task: end_task
result: 
  failed: false
  return_code: 0
  succeeded: true
start_timestamp: 2017-11-09T18:54:04.555662Z
end_timestamp: 2017-11-09T18:54:31.267708Z
+--------------------------+------------------------+----------------+-----------------------+-------------------------------+
| id                       | status                 | task           | action                | start_timestamp               |
+--------------------------+------------------------+----------------+-----------------------+-------------------------------+
| 5a04a44c7cae22371c88a77c | succeeded (2s elapsed) | get_inventory  | napalm.file_to_obj    | Thu, 09 Nov 2017 18:54:04 UTC |
| 5a04a44e7cae22371c88a781 | failed (6s elapsed)    | get_bgp_config | napalm.get_bgp_config | Thu, 09 Nov 2017 18:54:06 UTC |
| 5a04a44e7cae22371c88a782 | succeeded (3s elapsed) | get_bgp_config | napalm.get_bgp_config | Thu, 09 Nov 2017 18:54:06 UTC |
| 5a04a44e7cae22371c88a783 | failed (6s elapsed)    | get_bgp_config | napalm.get_bgp_config | Thu, 09 Nov 2017 18:54:06 UTC |
| 5a04a44e7cae22371c88a784 | succeeded (3s elapsed) | get_bgp_config | napalm.get_bgp_config | Thu, 09 Nov 2017 18:54:06 UTC |
| 5a04a4547cae22371c88a786 | succeeded (0s elapsed) | end_task       | core.noop             | Thu, 09 Nov 2017 18:54:12 UTC |
+--------------------------+------------------------+----------------+-----------------------+-------------------------------+
mab@mab-infra:~$ 
```

- get_bgp_neighbors_all:
```
mab@mab-infra:~$ st2 run napalm.get_bgp_neighbors_all
.................
id: 5a04a4817cae22371c88a788
action.ref: napalm.get_bgp_neighbors_all
parameters: None
status: failed
result_task: end_task
result: 
  failed: false
  return_code: 0
  succeeded: true
start_timestamp: 2017-11-09T18:54:57.672457Z
end_timestamp: 2017-11-09T18:55:31.587391Z
+--------------------------+------------------------+-------------------+--------------------------+-------------------------------+
| id                       | status                 | task              | action                   | start_timestamp               |
+--------------------------+------------------------+-------------------+--------------------------+-------------------------------+
| 5a04a4827cae22371c88a78b | succeeded (1s elapsed) | get_inventory     | napalm.file_to_obj       | Thu, 09 Nov 2017 18:54:58 UTC |
| 5a04a4847cae22371c88a790 | failed (6s elapsed)    | get_bgp_neighbors | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:54:59 UTC |
| 5a04a4847cae22371c88a791 | failed (6s elapsed)    | get_bgp_neighbors | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:54:59 UTC |
| 5a04a4847cae22371c88a792 | succeeded (4s elapsed) | get_bgp_neighbors | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:54:59 UTC |
| 5a04a4847cae22371c88a793 | succeeded (3s elapsed) | get_bgp_neighbors | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:55:00 UTC |
| 5a04a48a7cae22371c88a795 | succeeded (0s elapsed) | end_task          | core.noop                | Thu, 09 Nov 2017 18:55:06 UTC |
+--------------------------+------------------------+-------------------+--------------------------+-------------------------------+
mab@mab-infra:~$ 
```

```
```

```
```

```
```

## Setters (configuration commands):

- cfg_bgp_all:
```
mab@mab-infra:~$ st2 run napalm.cfg_bgp_all
..................................
id: 5a04a4c17cae22371c88a797
action.ref: napalm.cfg_bgp_all
parameters: None
status: failed
result_task: end_task
result: 
  failed: false
  return_code: 0
  succeeded: true
start_timestamp: 2017-11-09T18:56:01.319129Z
end_timestamp: 2017-11-09T18:57:10.364035Z
+--------------------------+------------------------+---------------+--------------------------+-------------------------------+
| id                       | status                 | task          | action                   | start_timestamp               |
+--------------------------+------------------------+---------------+--------------------------+-------------------------------+
| 5a04a4c17cae22371c88a79a | succeeded (2s elapsed) | get_inventory | napalm.file_to_obj       | Thu, 09 Nov 2017 18:56:01 UTC |
| 5a04a4c37cae22371c88a79f | failed (3s elapsed)    | render_config | default.render_file      | Thu, 09 Nov 2017 18:56:03 UTC |
| 5a04a4c37cae22371c88a7a0 | succeeded (3s elapsed) | render_config | default.render_file      | Thu, 09 Nov 2017 18:56:03 UTC |
| 5a04a4c37cae22371c88a7a2 | failed (3s elapsed)    | render_config | default.render_file      | Thu, 09 Nov 2017 18:56:03 UTC |
| 5a04a4c37cae22371c88a7a1 | succeeded (3s elapsed) | render_config | default.render_file      | Thu, 09 Nov 2017 18:56:03 UTC |
| 5a04a4c77cae22371c88a7a7 | failed (6s elapsed)    | load_config   | napalm.loadconfig        | Thu, 09 Nov 2017 18:56:07 UTC |
| 5a04a4c77cae22371c88a7aa | succeeded (6s elapsed) | load_config   | napalm.loadconfig        | Thu, 09 Nov 2017 18:56:07 UTC |
| 5a04a4c77cae22371c88a7a8 | failed (7s elapsed)    | load_config   | napalm.loadconfig        | Thu, 09 Nov 2017 18:56:07 UTC |
| 5a04a4c77cae22371c88a7a9 | succeeded (5s elapsed) | load_config   | napalm.loadconfig        | Thu, 09 Nov 2017 18:56:07 UTC |
| 5a04a4de7cae22371c88a7af | succeeded (4s elapsed) | audit_config  | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:56:29 UTC |
| 5a04a4de7cae22371c88a7b0 | failed (6s elapsed)    | audit_config  | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:56:29 UTC |
| 5a04a4de7cae22371c88a7b2 | failed (5s elapsed)    | audit_config  | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:56:30 UTC |
| 5a04a4de7cae22371c88a7b1 | succeeded (2s elapsed) | audit_config  | napalm.get_bgp_neighbors | Thu, 09 Nov 2017 18:56:30 UTC |
| 5a04a4e47cae22371c88a7b4 | succeeded (0s elapsed) | end_task      | core.noop                | Thu, 09 Nov 2017 18:56:36 UTC |
+--------------------------+------------------------+---------------+--------------------------+-------------------------------+
```

## Validation:

```
```

```
```

