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
	pp.pprint(eos.get_bgp_neighbors_detail(neighbor_address='172.16.0.30'))
	print "\n"
	print "JSON dumps print: \n"
	print dumps(eos.get_bgp_neighbors_detail(neighbor_address='172.16.0.30'), indent=4)
	print "\n"
	print ('Connection state for remote AS 65030 : ' + eos.get_bgp_neighbors_detail()['default'][65030][0]['connection_state'])
	print "\n"
	for item in eos.get_bgp_neighbors_detail()['default']:
		print ('Facing ' + eos.get_bgp_neighbors_detail()['default'][item][0]['remote_address'] + '  connection is in state :' + eos.get_bgp_neighbors_detail()['default'][item][0]['connection_state'])
	print "\n"
	#assert(eos.get_bgp_neighbors_detail()['default'][65030][0]["connection_state"] == "Established"), "BGP is not established"
	#if eos.get_bgp_neighbors_detail()['default'][65030][0]["connection_state"] == "Established":
	#	print ("BGP is established")

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**vmx1) as junos:
	print "Raw print: \n"
	pp.pprint(junos.get_bgp_neighbors_detail(neighbor_address='172.16.0.70'))
	print "\n"
	print "JSON dumps print: \n"
	print dumps(junos.get_bgp_neighbors_detail(neighbor_address='172.16.0.70'), indent=4)
	print ('Connection state for remote AS 65070 : ' + junos.get_bgp_neighbors_detail()['global'][65070][0]['connection_state'])
	print "\n"
	for item in junos.get_bgp_neighbors_detail()['global']:
		print ('Facing ' + junos.get_bgp_neighbors_detail()['global'][item][0]['remote_address'] + ' connection is in state :' + junos.get_bgp_neighbors_detail()['global'][item][0]['connection_state'])
	print "\n"
	#assert(junos.get_bgp_neighbors_detail()['global'][65070][0]["connection_state"] == "Established"), "BGP is not established"
	#if junos.get_bgp_neighbors_detail()['global'][65070][0]["connection_state"] == "Established":
	#	print ("BGP is established")
 

print('-'*60)
print('-'*60)