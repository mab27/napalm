from napalm_base import get_network_driver
import pprint

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


arista1_validate_file_path = "/home/mab/mab_automate/napalm/labs/validation/validate_files/arista1_basic_env.yml"
vmx1_validate_file_path = "/home/mab/mab_automate/napalm/labs/validation/validate_files/vmx1_basic_env.yml"


# Validating the device state
print('-'*60)
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

with eos_driver(**arista1) as arista1_device:
	pprint.pprint(arista1_device.compliance_report(arista1_validate_file_path))

# Validating the device state
print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**vmx1) as vmx1_device:
	pprint.pprint(vmx1_device.compliance_report(vmx1_validate_file_path))
