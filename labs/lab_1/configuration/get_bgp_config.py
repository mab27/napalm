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

with eos_driver(**arista1) as arista1_device:
	print "Raw print: \n"
	pp.pprint(arista1_device.get_bgp_config())
	print "\n"
	print "JSON dumps print: \n"
	print dumps(arista1_device.get_bgp_config(), indent=4)
	print"\n"
	print ('Configured remote AS for peer 172.16.0.30 : ' + str(arista1_device.get_bgp_config()['_']['neighbors']['172.16.0.30']['remote_as']))


print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**vmx1) as vmx1_device:
	print "Raw print: \n"
	pp.pprint(vmx1_device.get_bgp_config())
	print "\n"
	print "JSON dumps print: \n"
	print dumps(vmx1_device.get_bgp_config(), indent=4)
	print"\n"
	print ('Configured remote AS for peer 172.16.0.70 : ' + str(vmx1_device.get_bgp_config()['underlay']['neighbors']['172.16.0.70']['remote_as']))


print('-'*60)
print('-'*60)


