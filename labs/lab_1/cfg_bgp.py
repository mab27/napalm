from napalm_base import get_network_driver
from jinja2 import Template
from yaml import load
import pprint
import time

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


# getting template
eos_template_file=open('/home/mab/mab_automate/napalm/template_files/cfg_ebgp/eos.j2')
s_eos=eos_template_file.read()
eos_template_file.close()
bgp_template_arista1=Template(s_eos)

junos_template_file=open('/home/mab/mab_automate/napalm/template_files/cfg_ebgp/junos.j2')
s_junos=junos_template_file.read()
junos_template_file.close()
bgp_template_vmx1=Template(s_junos)


# getting variables
arista1_variables=open('/home/mab/mab_automate/napalm/vars_inputs/arista1.yml')
s_eos=arista1_variables.read()
arista1_variables.close()
bgp_vars_arista1=load(s_eos)

vmx1_variables=open('/home/mab/mab_automate/napalm/vars_inputs/vmx1.yml')
s_junos=vmx1_variables.read()
vmx1_variables.close()
bgp_vars_vmx1=load(s_junos)

def change_configuration(device, configuration):
	device.open()
	device.load_merge_candidate(config=configuration)
	print(device.compare_config())
	device.commit_config()

print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

# rendering the template
print 'rendering bgp template'
bgp_conf_arista1=open('/home/mab/mab_automate/napalm/output/bgp_arista1.txt','w')
bgp_conf_arista1.write(bgp_template_arista1.render(bgp_vars_arista1))
bgp_conf_arista1.close()


# configuring the device
with eos_driver(**arista1) as eos:
	#file_path = '/home/mab/mab_automate/napalm/output/bgp_arista1.txt'
	#change_configuration(eos, file_path)
	with open('/home/mab/mab_automate/napalm/output/bgp_arista1.txt', "r") as config:
		change_configuration(eos, config.read())


print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

# rendering the template
print 'rendering bgp template'
bgp_conf_vmx1=open('/home/mab/mab_automate/napalm/output/bgp_vmx1.txt','w')
bgp_conf_vmx1.write(bgp_template_vmx1.render(bgp_vars_vmx1))
bgp_conf_vmx1.close()

# configuring the device
with junos_driver(**vmx1) as junos:
	#file_path = "/home/mab/mab_automate/napalm/output/bgp_vmx1.txt"
	#change_configuration(junos, "/home/mab/mab_automate/napalm/output/bgp_vmx1.txt")
	with open('/home/mab/mab_automate/napalm/output/bgp_vmx1.txt', "r") as config:
		print config.read()
		change_configuration(junos, config.read())


print('-'*60)
print('-'*60)
