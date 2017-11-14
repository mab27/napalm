# Lab_1

## Overview:
- Invoking standard actions from the NAPALM pack.
- Sections:
    - [Getters (show commands)](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab1#getters-show-commands)
    	- [get_facts](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_facts)
      	- [get_bgp_config](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_bgp_config)
    	- [get_bgp_neighbors](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_bgp_neighbors)
      	- [get_bgp_neighbors_detail](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_bgp_neighbors_detail)
      	- [get_interfaces](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_interfaces)
      	- [get_interfaces_ip](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_interfaces_ip)
      	- [get_interfaces_counters](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_interfaces_counters)
      	- [get_lldp_neighbors](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_lldp_neighbors)
      	- [get_arp_table](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#get_arp_table)
      	- [ping](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#ping)
    - [Setters (configuration commands)](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#setters-configuration-commands)
    	- [loadconfig](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1#loadconfig)

## Getters (show commands):

### get_facts:
```
mab@mab-infra:~$ st2 run napalm.get_facts hostname=arista1 
.
id: 59fc26167cae22068a51a720
status: succeeded
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
      uptime: -5410
      vendor: Arista
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$
mab@mab-infra:~$ st2 execution get 59fc26167cae22068a51a720 -k result.raw.os_version
4.18.1F-4591672.4181F
mab@mab-infra:~$ 
mab@mab-infra:~$
mab@mab-infra:~$ st2 run napalm.get_facts hostname=vmx1 
...
id: 59fc261d7cae22068a51a723
status: succeeded
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
      uptime: 2000
      vendor: Juniper
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$
mab@mab-infra:~$ st2 execution get 59fc261d7cae22068a51a723 -k result.raw.os_version
14.1R4.9
mab@mab-infra:~$
```

### get_bgp_config:
```
mab@mab-infra:~$ st2 run napalm.get_bgp_config hostname=arista1
.
id: 59fc21b17cae22068a51a6d5
status: succeeded
parameters: 
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
      _:
        apply_groups: []
        description: ''
        export_policy: ''
        import_policy: ''
        local_address: ''
        local_as: 65070
        multihop_ttl: 0
        multipath: false
        neighbors:
          172.16.0.30:
            authentication_key: ''
            description: vmx1
            export_policy: ''
            import_policy: ''
            local_address: ''
            local_as: 65070
            nhs: false
            prefix_limit: {}
            remote_as: 65030
            route_reflector_client: false
          172.16.0.40:
            authentication_key: ''
            description: vmx2
            export_policy: ''
            import_policy: ''
            local_address: ''
            local_as: 65070
            nhs: false
            prefix_limit: {}
            remote_as: 65040
            route_reflector_client: false
          172.16.0.80:
            authentication_key: ''
            description: aritsa2
            export_policy: ''
            import_policy: ''
            local_address: ''
            local_as: 65070
            nhs: false
            prefix_limit: {}
            remote_as: 65080
            route_reflector_client: false
        prefix_limit: {}
        remote_as: 0
        remove_private_as: false
        type: ''
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_bgp_config hostname=vmx1
.
id: 59fc21b87cae22068a51a6d8
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      underlay:
        apply_groups: []
        description: ''
        export_policy: bgp-out
        import_policy: bgp-in
        local_address: ''
        local_as: 65030
        multihop_ttl: 0
        multipath: true
        neighbors:
          172.16.0.40:
            authentication_key: ''
            description: vmx2
            export_policy: ''
            import_policy: ''
            local_address: ''
            local_as: 0
            nhs: false
            prefix_limit: {}
            remote_as: 65040
            route_reflector_client: false
          172.16.0.70:
            authentication_key: ''
            description: aritsa1
            export_policy: ''
            import_policy: ''
            local_address: ''
            local_as: 0
            nhs: false
            prefix_limit: {}
            remote_as: 65070
            route_reflector_client: false
          172.16.0.80:
            authentication_key: ''
            description: aritsa2
            export_policy: ''
            import_policy: ''
            local_address: ''
            local_as: 0
            nhs: false
            prefix_limit: {}
            remote_as: 65080
            route_reflector_client: false
        prefix_limit: {}
        remote_as: 0
        remove_private_as: false
        type: external
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

### get_bgp_neighbors:
```
mab@mab-infra:~$ st2 run napalm.get_bgp_neighbors hostname=arista1
.
id: 59fc221d7cae22068a51a6db
status: succeeded
parameters: 
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
      172.16.0.30:
        address_family:
          ipv4:
            accepted_prefixes: -1
            received_prefixes: 2
            sent_prefixes: 0
          ipv6:
            accepted_prefixes: -1
            received_prefixes: 0
            sent_prefixes: 0
        description: ''
        is_enabled: true
        is_up: true
        local_as: 65070
        remote_as: 65030
        remote_id: 30.30.30.30
        uptime: -6517
      172.16.0.40:
        address_family:
          ipv4:
            accepted_prefixes: -1
            received_prefixes: 0
            sent_prefixes: 0
          ipv6:
            accepted_prefixes: -1
            received_prefixes: 0
            sent_prefixes: 0
        description: ''
        is_enabled: true
        is_up: false
        local_as: 65070
        remote_as: 65040
        remote_id: 0.0.0.0
        uptime: -6515
      172.16.0.80:
        address_family:
          ipv4:
            accepted_prefixes: -1
            received_prefixes: 0
            sent_prefixes: 0
          ipv6:
            accepted_prefixes: -1
            received_prefixes: 0
            sent_prefixes: 0
        description: ''
        is_enabled: true
        is_up: false
        local_as: 65070
        remote_as: 65080
        remote_id: 0.0.0.0
        uptime: -6515
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_bgp_neighbors hostname=vmx1
..
id: 59fc222a7cae22068a51a6de
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      172.16.0.40:
        address_family:
          ipv4:
            accepted_prefixes: -1
            received_prefixes: -1
            sent_prefixes: -1
          ipv6:
            accepted_prefixes: -1
            received_prefixes: -1
            sent_prefixes: -1
        description: vmx2
        is_enabled: true
        is_up: false
        local_as: 65030
        remote_as: 65040
        remote_id: ''
        uptime: 948
      172.16.0.70:
        address_family:
          ipv4:
            accepted_prefixes: 0
            received_prefixes: 0
            sent_prefixes: 2
          ipv6:
            accepted_prefixes: -1
            received_prefixes: -1
            sent_prefixes: -1
        description: aritsa1
        is_enabled: true
        is_up: true
        local_as: 65030
        remote_as: 65070
        remote_id: 70.70.70.70
        uptime: 697
      172.16.0.80:
        address_family:
          ipv4:
            accepted_prefixes: -1
            received_prefixes: -1
            sent_prefixes: -1
          ipv6:
            accepted_prefixes: -1
            received_prefixes: -1
            sent_prefixes: -1
        description: aritsa2
        is_enabled: true
        is_up: false
        local_as: 65030
        remote_as: 65080
        remote_id: ''
        uptime: 948
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

### get_bgp_neighbors_detail:
```
mab@mab-infra:~$ st2 run napalm.get_bgp_neighbors_detail hostname=arista1 neighbor=172.16.0.30
.
id: 59fc22bd7cae22068a51a6e4
status: succeeded
parameters: 
  hostname: arista1
  neighbor: 172.16.0.30
result: 
  exit_code: 0
  result:
    raw:
      default:
        '65030':
        - accepted_prefix_count: 2
          active_prefix_count: 0
          advertised_prefix_count: 0
          configured_holdtime: 180
          configured_keepalive: 60
          connection_state: Established
          export_policy: ''
          flap_count: 0
          holdtime: 90
          import_policy: ''
          input_messages: 36
          input_updates: 2
          keepalive: 30
          last_event: RecvKeepAlive
          local_address: 172.16.0.70
          local_address_configured: true
          local_as: 65070
          local_as_prepend: false
          local_port: 49575
          messages_queued_out: 0
          multihop: true
          multipath: false
          output_messages: 32
          output_updates: 1
          previous_connection_state: OpenConfirm
          received_prefix_count: 2
          remote_address: 172.16.0.30
          remote_as: 65030
          remote_port: 179
          remove_private_as: false
          router_id: 30.30.30.30
          routing_table: default
          suppress_4byte_as: false
          suppressed_prefix_count: 0
          up: true
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_bgp_neighbors_detail hostname=vmx1 neighbor=172.16.0.70
..
id: 59fc22ca7cae22068a51a6e7
status: succeeded
parameters: 
  hostname: vmx1
  neighbor: 172.16.0.70
result: 
  exit_code: 0
  result:
    raw:
      global:
        '65070':
        - accepted_prefix_count: 0
          active_prefix_count: 0
          advertised_prefix_count: 2
          configured_holdtime: 90
          configured_keepalive: 30
          connection_state: Established
          export_policy: bgp-out
          flap_count: 0
          holdtime: 90
          import_policy: bgp-in
          input_messages: 31
          input_updates: 1
          keepalive: 30
          last_event: RecvKeepAlive
          local_address: 172.16.0.30
          local_address_configured: false
          local_as: 65030
          local_as_prepend: false
          local_port: 179
          messages_queued_out: 0
          multihop: false
          multipath: true
          output_messages: 35
          output_updates: 1
          previous_connection_state: OpenConfirm
          received_prefix_count: 0
          remote_address: 172.16.0.70
          remote_as: 65070
          remote_port: 49575
          remove_private_as: false
          router_id: 70.70.70.70
          routing_table: global
          suppress_4byte_as: false
          suppressed_prefix_count: 0
          up: true
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

### get_interfaces:
```
mab@mab-infra:~$ st2 run napalm.get_interfaces hostname=arista1
.
id: 59fc23487cae22068a51a6ea
status: succeeded
parameters: 
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
      Ethernet1:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1509702540.0864758
        mac_address: 00:0C:29:FA:C2:C1
        speed: 0
      Management1:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1509702537.0901725
        mac_address: 00:0C:29:69:72:9E
        speed: 1000
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 execution get 59fc23487cae22068a51a6ea -k result.raw.Ethernet1.is_up
True
mab@mab-infra:~$ 
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_interfaces hostname=vmx1
..
id: 59fc234f7cae22068a51a6ed
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      .local.:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      cbp0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:05:86:71:AC:11
        speed: -1
      demux0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      dsc:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      em1:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:CE
        speed: 1000
      em2:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:D8
        speed: 1000
      em3:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:E2
        speed: 1000
      em4:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:EC
        speed: 1000
      em5:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:F6
        speed: 1000
      em6:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:00
        speed: 1000
      em7:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:0A
        speed: 1000
      em8:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:14
        speed: 1000
      em9:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:0C:29:88:F0:1E
        speed: 1000
      fxp0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1236.0
        mac_address: 00:0C:29:88:F0:C4
        speed: 1000
      ge-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1193.0
        mac_address: 00:05:86:71:AC:00
        speed: 1000
      ge-0/0/1:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:01
        speed: 1000
      ge-0/0/2:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:02
        speed: 1000
      ge-0/0/3:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:03
        speed: 1000
      ge-0/0/4:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:04
        speed: 1000
      ge-0/0/5:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:05
        speed: 1000
      ge-0/0/6:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:06
        speed: 1000
      ge-0/0/7:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:07
        speed: 1000
      ge-0/0/8:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:08
        speed: 1000
      ge-0/0/9:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: 1192.0
        mac_address: 00:05:86:71:AC:09
        speed: 1000
      gre:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      ipip:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      irb:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:05:86:71:AF:F0
        speed: -1
      lc-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: 800
      lo0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      lsi:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      mtun:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      pfe-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: 800
      pfh-0/0/0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: 800
      pimd:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      pime:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: None
        speed: -1
      pip0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: 00:05:86:71:AF:B0
        speed: -1
      pp0:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      tap:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
      vtep:
        description: ''
        is_enabled: true
        is_up: true
        last_flapped: -1.0
        mac_address: Unspecified
        speed: -1
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

### get_interfaces_ip:
```
mab@mab-infra:~$ st2 run napalm.get_interfaces hostname=arista1 ipaddresses=true
.
id: 59fc23977cae22068a51a6f0
status: succeeded
parameters: 
  hostname: arista1
  ipaddresses: true
result: 
  exit_code: 0
  result:
    raw:
      Ethernet1:
        ipv4:
          172.16.0.70:
            prefix_length: 24
        ipv6: {}
      Management1:
        ipv4:
          192.168.0.70:
            prefix_length: 24
        ipv6: {}
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_interfaces hostname=vmx1 ipaddresses=true
..
id: 59fc23a07cae22068a51a6f3
status: succeeded
parameters: 
  hostname: vmx1
  ipaddresses: true
result: 
  exit_code: 0
  result:
    raw:
      em1.0:
        ipv4:
          172.16.0.1:
            prefix_length: 16
        ipv6:
          fe80::20c:29ff:fe88:f0ce:
            prefix_length: 64
      ge-0/0/0.0:
        ipv4:
          192.168.0.30:
            prefix_length: 24
      ge-0/0/1.0:
        ipv4:
          172.16.0.30:
            prefix_length: 24
      lo0.16384:
        ipv4:
          127.0.0.1:
            prefix_length: 32
      lo0.16385:
        ipv4:
          128.0.0.1:
            prefix_length: 32
          128.0.0.4:
            prefix_length: 32
        ipv6:
          fe80::20c:290f:fc88:f0c4:
            prefix_length: 128
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

### get_interfaces_counters:
```
mab@mab-infra:~$ st2 run napalm.get_interfaces hostname=arista1 counters=true
.
id: 59fc23fe7cae22068a51a6fc
status: succeeded
parameters: 
  counters: true
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
      Ethernet1:
        rx_broadcast_packets: 159
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 42
        rx_octets: 25022
        rx_unicast_packets: 93
        tx_broadcast_packets: 97
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 39
        tx_octets: 18563
        tx_unicast_packets: 94
      Management1:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 47857
        rx_unicast_packets: 262
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 73508
        tx_unicast_packets: 266
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_interfaces hostname=vmx1 counters=true
..
id: 59fc24067cae22068a51a6ff
status: succeeded
parameters: 
  counters: true
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      em1:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7544
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 120
        tx_unicast_packets: -1
      em2:
        rx_broadcast_packets: -1
        rx_discards: 059fc22bd7cae22068a51a6e4
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 224881
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 950522
        tx_unicast_packets: -1
      em3:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 20671
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 24668
        tx_unicast_packets: -1
      em4:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7690
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      em5:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7690
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      em6:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7690
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      em7:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7690
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      em8:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7526
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      em9:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 7526
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      ge-0/0/0:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 78251
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 783078
        tx_unicast_packets: 0
      ge-0/0/1:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 18359
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 26810
        tx_unicast_packets: 0
      ge-0/0/2:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/3:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/4:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/5:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/6:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/7:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/8:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      ge-0/0/9:
        rx_broadcast_packets: 0
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: 0
        rx_octets: 0
        rx_unicast_packets: 0
        tx_broadcast_packets: 0
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: 0
        tx_octets: 0
        tx_unicast_packets: 0
      mtun:
        rx_broadcast_packets: -1
        rx_discards: -1
        rx_errors: -1
        rx_multicast_packets: -1
        rx_octets: 0
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: -1
        tx_errors: -1
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
      vtep:
        rx_broadcast_packets: -1
        rx_discards: 0
        rx_errors: 0
        rx_multicast_packets: -1
        rx_octets: 0
        rx_unicast_packets: -1
        tx_broadcast_packets: -1
        tx_discards: 0
        tx_errors: 0
        tx_multicast_packets: -1
        tx_octets: 0
        tx_unicast_packets: -1
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```


### get_lldp_neighbors:
```
mab@mab-infra:~$ st2 run napalm.get_lldp_neighbors hostname=arista1 
.
id: 59fc24a47cae22068a51a702
status: succeeded
parameters: 
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
      Ethernet1:
      - hostname: vmx1
        port: '515'
      Management1:
      - hostname: vmx1
        port: '514'
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 execution get 59fc24a47cae22068a51a702 -k result.raw.Ethernet1[0].hostname
vmx1
mab@mab-infra:~$ 
mab@mab-infra:~$ st2 run napalm.get_lldp_neighbors hostname=vmx1 
.
id: 59fc24ab7cae22068a51a705
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      ge-0/0/0:
      - hostname: arista1
        port: Management1
      ge-0/0/1:
      - hostname: arista1
        port: Ethernet1
  stderr: ''
  stdout: ''
mab@mab-infra:~$
```

### get_arp_table:
```
mab@mab-infra:~$ st2 run napalm.get_arp_table hostname=arista1 
.
id: 59fc24cd7cae22068a51a708
status: succeeded
parameters: 
  hostname: arista1
result: 
  exit_code: 0
  result:
    raw:
    - age: 0.0
      interface: Ethernet1
      ip: 172.16.0.30
      mac: 00:05:86:71:AC:01
    - age: 0.0
      interface: Management1
      ip: 192.168.0.125
      mac: 00:0C:29:62:D7:0D
  stderr: ''
  stdout: ''
mab@mab-infra:~$ st2 run napalm.get_arp_table hostname=vmx1 
.
id: 59fc24d37cae22068a51a70b
status: succeeded
parameters: 
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
    - age: 1237.0
      interface: ge-0/0/1.0
      ip: 172.16.0.70
      mac: 00:0C:29:FA:C2:C1
    - age: 1294.0
      interface: ge-0/0/0.0
      ip: 192.168.0.125
      mac: 00:0C:29:62:D7:0D
  stderr: ''
  stdout: ''
mab@mab-infra:~$
```

### ping:
- Failing on Arista EOS for now

```
mab@mab-infra:~$ st2 run napalm.ping hostname=vmx1 destination=172.16.0.70
...
id: 5a0967b57cae220660295b6e
status: succeeded
parameters: 
  destination: 172.16.0.70
  hostname: vmx1
result: 
  exit_code: 0
  result:
    raw:
      success:
        packet_loss: 0
        probes_sent: 5
        results:
        - ip_address: 172.16.0.70
          rtt: 10.222
        - ip_address: 172.16.0.70
          rtt: 9.54
        - ip_address: 172.16.0.70
          rtt: 16.273
        - ip_address: 172.16.0.70
          rtt: 5.577
        - ip_address: 172.16.0.70
          rtt: 7.135
        rtt_avg: 9.749
        rtt_max: 16.273
        rtt_min: 5.577
        rtt_stddev: 3.662
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

## Setters (configuration commands):

### loadconfig:

```
mab@mab-infra:~$ cat ~/mab_automate/napalm/labs/napalm-st2/lab1/config_files/arista1_bgp.txt 
router bgp 65070
   router-id 70.70.70.70
   neighbor 172.16.0.30 remote-as 65030
   neighbor 172.16.0.30 description vmx1
   neighbor 172.16.0.30 maximum-routes 12000 
mab@mab-infra:~$
mab@mab-infra:~$
mab@mab-infra:/opt/stackstorm/packs$ cat ~/mab_automate/napalm/labs/napalm-st2/lab1/config_files/vmx1_bgp.txt 
protocols {
    bgp {
        group underlay {
            type external;
            import bgp-in;
            export bgp-out;
            local-as 65030;
            multipath multiple-as;
            neighbor 172.16.0.70 {
                description arista1;
                peer-as 65070;
            }
        }
    }
    lldp {
        interface all;
        interface ge-0/0/0;
    }
}
mab@mab-infra:~$
mab@mab-infra:~$
mab@mab-infra:~$ st2 run napalm.loadconfig hostname=arista1 config_file=~/mab_automate/napalm/labs/napalm-st2/lab1/config_files/arista1_bgp.txt
..
id: 59fc299f7cae22068a51a72c
status: succeeded
parameters: 
  config_file: /home/mab/mab_automate/napalm/labs/napalm-st2/lab1/config_files/arista1_bgp.txt
  hostname: arista1
result: 
  exit_code: 0
  result: load (merge) successful on arista1
  stderr: ''
  stdout: ''
mab@mab-infra:~$
mab@mab-infra:~$
mab@mab-infra:~$ st2 run napalm.loadconfig hostname=vmx1 config_file=~/mab_automate/napalm/labs/napalm-st2/lab1/config_files/vmx1_bgp.txt
..
id: 59fc29ce7cae22068a51a72f
status: succeeded
parameters: 
  config_file: /home/mab/mab_automate/napalm/labs/napalm-st2/lab1/config_files/vmx1_bgp.txt
  hostname: vmx1
result: 
  exit_code: 0
  result: load (merge) successful on vmx1
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```