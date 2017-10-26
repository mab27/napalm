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

# Paths to folders
path_template_files = "/home/mab/mab_automate/napalm/template_files/"
path_vars_files = "/home/mab/mab_automate/napalm/vars_inputs/"
path_render_files = "/home/mab/mab_automate/napalm/render_files/"

# Getting template
eos_template_file_path = path_template_files + "cfg_ebgp/eos.j2"
eos_template_file=open(eos_template_file_path)
s_eos=eos_template_file.read()
eos_template_file.close()
bgp_template_arista1=Template(s_eos)

junos_template_file_path = path_template_files + "cfg_ebgp/junos.j2"
junos_template_file=open(junos_template_file_path)
s_junos=junos_template_file.read()
junos_template_file.close()
bgp_template_vmx1=Template(s_junos)


# Getting variables
arista1_vars_file_path = path_vars_files + "arista1.yml"
arista1_variables=open(arista1_vars_file_path)
s_eos=arista1_variables.read()
arista1_variables.close()
bgp_vars_arista1=load(s_eos)

vmx1_vars_file_path = path_vars_files + "vmx1.yml"
vmx1_variables=open(vmx1_vars_file_path)
s_junos=vmx1_variables.read()
vmx1_variables.close()
bgp_vars_vmx1=load(s_junos)


def change_configuration(device, filepath):
	device.open()
	device.load_merge_candidate(filename=filepath)
	print(device.compare_config())
	device.commit_config()

print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

# Rendering the template
print 'rendering bgp template'
arista1_render_file_path = path_render_files + "bgp_arista1.txt"
bgp_conf_arista1=open(arista1_render_file_path,'w')
bgp_conf_arista1.write(bgp_template_arista1.render(bgp_vars_arista1))
bgp_conf_arista1.close()


# Configuring the device
with eos_driver(**arista1) as arista1_device:
	filepath = arista1_render_file_path
	change_configuration(arista1_device, filepath)

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

# Rendering the template
print 'rendering bgp template'
vmx1_render_file_path = path_render_files + "bgp_vmx1.txt"
bgp_conf_vmx1=open(vmx1_render_file_path,'w')
bgp_conf_vmx1.write(bgp_template_vmx1.render(bgp_vars_vmx1))
bgp_conf_vmx1.close()

# Configuring the device
with junos_driver(**vmx1) as vmx1_device:
	filepath = vmx1_render_file_path
	change_configuration(vmx1_device, filepath)

print('-'*60)
print('-'*60)
