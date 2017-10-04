from napalm_base import get_network_driver
import pprint
pp = pprint.PrettyPrinter(indent=4)

eos_driver =  get_network_driver('eos')

eos_configuration = {
	'hostname': '192.168.0.70',
	'username': 'admin',
	'password': 'admin123',
}

print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

with eos_driver(**eos_configuration) as eos:
	pp.pprint(eos.get_facts())
