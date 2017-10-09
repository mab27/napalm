from napalm_base import get_network_driver
import pprint
from json import dumps

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

print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

with eos_driver(**eos_configuration) as eos:
	pp.pprint(eos.get_bgp_neighbors_detail(neighbor_address='172.16.0.30'))
	print('-'*60)
	print('-'*60)
	print dumps(eos.get_bgp_neighbors_detail(), indent=4)
	assert(eos.get_bgp_neighbors_detail()['default'][65030][0]["connection_state"] == "Established"), "BGP is not established"
	if eos.get_bgp_neighbors_detail()['default'][65030][0]["connection_state"] == "Established":
		print ("BGP is established")

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**junos_configuration) as junos:
	pp.pprint(junos.get_bgp_neighbors_detail(neighbor_address='172.16.0.70'))
	print('-'*60)
	print('-'*60)
	print dumps(junos.get_bgp_neighbors_detail(), indent=4)
	pprint.pprint (junos.get_bgp_neighbors_detail()['global'][65070][0]["connection_state"])
	assert(junos.get_bgp_neighbors_detail()['global'][65070][0]["connection_state"] == "Established"), "BGP is not established"
	if junos.get_bgp_neighbors_detail()['global'][65070][0]["connection_state"] == "Established":
		print ("BGP is established")
 

print('-'*60)
print('-'*60)