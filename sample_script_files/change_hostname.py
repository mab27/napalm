from napalm_base import get_network_driver
import pprint
pp = pprint.PrettyPrinter(indent=4)

eos_driver = get_network_driver('eos')
junos_driver = get_network_driver('junos')

eos_configuration = {
	'hostname': '192.168.0.70',
	'username': 'admin',
	'password': 'admin123',
}

junos_configuration = {
	'hostname': '192.168.0.30',
	'username': 'mab',
	'password': 'mab123',
}

def change_configuration(device, configuration):
	device.load_merge_candidate(config=configuration)
	print(device.compare_config())
	device.commit_config()

print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

with eos_driver(**eos_configuration) as eos:
	change_configuration(eos,'hostname lon.arista1')

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)


with junos_driver(**junos_configuration) as junos:
	change_configuration(junos,"system {host-name par.vmx1;}")

print('-'*60)
print('-'*60)



device = junos_driver(hostname='192.168.0.30', username='mab', password='mab123')
device.open()
change_configuration(device,"system {host-name par.vmx2;}")





