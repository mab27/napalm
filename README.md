# NAPALM

## Introduction:
- NAPALM stands for Network Automation and Programmability Abstraction Layer with Multivendor support.
- It is a Python library that implements a set of functions to interact with different network device Operating Systems using a unified API.
- NAPALM supports several methods to connect to the devices, in order to manipulate/validate configurations or get operationnal data.
- Few links:
	- [NAPALM Blog page](https://napalm-automation.net/)
	- [NAPALM documentation](https://napalm.readthedocs.io/en/latest/index.html)

## Why NAPALM is cool ?
- Multivendor: It abstracts for you the different Network Automation libraries of the vendors.
- Support configuration and validatiton
- Integrates with Ansible, Salt and StackStorm

## Content of this repo:
- Code examples on how to use NAPALM via various methods:
	- [via CLI](https://github.com/mab27/napalm/tree/master/labs/01-napalm-cli)
	- [python script files](https://github.com/mab27/napalm/tree/master/labs/02-napalm-python)
	- [via StackStorm](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm)
	- [via Ansible](https://github.com/mab27/napalm/tree/master/labs/04-napalm-ansible)
- The examples are performed on two seperate network operating stems:
	- Juniper Junos
	- Arista EOS
