from napalm_base import get_network_driver
import pprint
pp = pprint.PrettyPrinter(indent=4)

junos_driver =  get_network_driver('junos')

junos_configuration = {
	'hostname': '192.168.0.30',
	'username': 'mab',
	'password': 'mab123',
}

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**junos_configuration) as junos:
	pp.pprint(junos.get_facts())

