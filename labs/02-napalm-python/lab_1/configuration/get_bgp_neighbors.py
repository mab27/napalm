from napalm_base import get_network_driver
from json import dumps
import pprint

pp = pprint.PrettyPrinter(indent=4)

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
print ('Device : ' + 'arista1')
print('-'*60)

with eos_driver(**arista1) as arista1_device:
	print"\n"
	print"JSON dumps print: \n"
	print dumps(arista1_device.get_bgp_neighbors(), indent=4)
	print"\n"
	print ('Uptime for neighbor 172.16.0.30 : ' + str(arista1_device.get_bgp_neighbors()['global']['peers']['172.16.0.30']['uptime']))
	print"\n"

print('-'*60)
print ('Device : ' + 'vmx1')
print('-'*60)

with junos_driver(**vmx1) as vmx1_device:
	print"\n"
	print"JSON dumps print: \n"
	print dumps(vmx1_device.get_bgp_neighbors(), indent=4)
	print"\n"
	print ('Uptime for neighbor 172.16.0.70 : ' + str(vmx1_device.get_bgp_neighbors()['global']['peers']['172.16.0.70']['uptime']))
	print"\n"

print('-'*60)
print('-'*60)




