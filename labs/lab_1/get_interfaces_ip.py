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
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

with eos_driver(**arista1) as eos:
	print "Raw print: \n"
	pp.pprint(eos.get_interfaces_ip())
	print "\n"
	print "JSON dumps print: \n"
	print dumps(eos.get_interfaces_ip(), indent=4)
	#print "\n"
	#print ('Interface Ethernet1 has IP address : ' + eos.get_interfaces_ip()['Ethernet1']['ipv4'][0])
	#print "\n"


print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**vmx1) as junos:
	print "Raw print: \n"
	pp.pprint(junos.get_interfaces_ip())
	print "\n"
	print "JSON dumps print: \n"
	print dumps(junos.get_interfaces_ip(), indent=4)
	#print "\n"
	#print ('Interface ge-0/0/0 has IP address : ' + junos.get_interfaces_ip()['ge-0/0/0']['ipv4'][0])
	#print "\n"

print('-'*60)
print('-'*60)