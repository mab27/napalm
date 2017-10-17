### Parse native configuration and return and OpenConfig object

from napalm_base import get_network_driver
import napalm_yang
from json import dumps
from pprint import pprint

# Create Device Object
eos_driver = get_network_driver('eos')
junos_driver = get_network_driver('junos')

arista1 = {
	'hostname': '192.168.0.70',
	'username': 'admin',
	'password': 'admin123',
}

vmx1 = {
	'hostname': '192.168.0.30',
	'username': 'mab',
	'password': 'mab123',
}

print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

with eos_driver(**arista1) as eos:
	running_config = napalm_yang.base.Root()
	running_config.add_model(napalm_yang.models.openconfig_interfaces)
	running_config.parse_config(device=eos)

print dumps(running_config.get(filter=True), indent=4)

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**vmx1) as junos:
	running_config = napalm_yang.base.Root()
	running_config.add_model(napalm_yang.models.openconfig_interfaces)
	running_config.parse_config(device=junos)

print dumps(running_config.get(filter=True), indent=4)
