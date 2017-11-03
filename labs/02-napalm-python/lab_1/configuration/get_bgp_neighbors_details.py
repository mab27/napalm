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
	print "Raw print: \n"
	pp.pprint(arista1_device.get_bgp_neighbors_detail(neighbor_address='172.16.0.30'))
	print "\n"
	print "JSON dumps print: \n"
	print dumps(arista1_device.get_bgp_neighbors_detail(neighbor_address='172.16.0.30'), indent=4)
	print "\n"
	print ('Connection state for remote AS 65030 : ' + arista1_device.get_bgp_neighbors_detail()['default'][65030][0]['connection_state'])
	print "\n"
	for item in arista1_device.get_bgp_neighbors_detail()['default']:
		print ('Facing ' + arista1_device.get_bgp_neighbors_detail()['default'][item][0]['remote_address'] + '  connection is in state :' + arista1_device.get_bgp_neighbors_detail()['default'][item][0]['connection_state'])
	print "\n"

print('-'*60)
print ('Device : ' + 'vmx1')
print('-'*60)

with junos_driver(**vmx1) as vmx1_device:
	print "Raw print: \n"
	pp.pprint(vmx1_device.get_bgp_neighbors_detail(neighbor_address='172.16.0.70'))
	print "\n"
	print "JSON dumps print: \n"
	print dumps(vmx1_device.get_bgp_neighbors_detail(neighbor_address='172.16.0.70'), indent=4)
	print ('Connection state for remote AS 65070 : ' + vmx1_device.get_bgp_neighbors_detail()['global'][65070][0]['connection_state'])
	print "\n"
	for item in vmx1_device.get_bgp_neighbors_detail()['global']:
		print ('Facing ' + vmx1_device.get_bgp_neighbors_detail()['global'][item][0]['remote_address'] + ' connection is in state :' + vmx1_device.get_bgp_neighbors_detail()['global'][item][0]['connection_state'])
	print "\n"
 

print('-'*60)
print('-'*60)