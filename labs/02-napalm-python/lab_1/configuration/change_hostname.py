from napalm_base import get_network_driver
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

def change_configuration(device, configuration):
	device.load_merge_candidate(config=configuration)
	print(device.compare_config())
	device.commit_config()

print('-'*60)
print ('Device : ' + 'arista1')
print('-'*60)

with eos_driver(**arista1) as arista1_device:
	change_configuration(arista1_device,'hostname arista1')

print('-'*60)
print ('Device : ' + 'vmx1')
print('-'*60)


with junos_driver(**vmx1) as vmx1_device:
	change_configuration(vmx1_device,"system {host-name vmx1;}")

print('-'*60)
print('-'*60)



