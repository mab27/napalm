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
	print dumps(arista1_device.get_config()['running'], indent=4)

print('-'*60)
print ('Device : ' + 'vmx1')
print('-'*60)

with junos_driver(**vmx1) as vmx1_device:
	print dumps(vmx1_device.get_config()['running'], indent=4)

print('-'*60)
print('-'*60)
