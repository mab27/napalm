from my_repo_functions import change_configuration
from napalm_base import get_network_driver
from jinja2 import Template
from yaml import load
import time

# Path to folders 
inventory_file_path = "/home/mab/mab_automate/napalm/inventory/inventory.yml"
path_template_files = "/home/mab/mab_automate/napalm/template_files/"
path_vars_files = "/home/mab/mab_automate/napalm/host_vars/"
path_render_files = "/home/mab/mab_automate/napalm/render_files/"

# Getting inventory in a python data structure. 
inventory_file =open(inventory_file_path, 'r')
inventory_structure =inventory_file.read()
inventory_file.close()
inventory =load(inventory_structure)

for device_item in inventory:
	print('-'*60)
	print ('Device : ' + device_item)
	print('-'*60)

	mgmt_ip = inventory[device_item]['mgmt_ip']
	username = inventory[device_item]['username']
	password = inventory[device_item]['password']
	driver = inventory[device_item]['driver']

	# Getting template
	print ' - Getting template'
	template_file=open(path_template_files + 'bgp_configure/' + driver + '.j2')
	s=template_file.read()
	template_file.close()
	bgp_template=Template(s)


	try:
		# Getting variables
		print ' - Getting variables'
		variables=open(path_vars_files + device_item + '.yml')
		s=variables.read()
		variables.close()
		bgp_vars=load(s)

		# Rendering the template
		print ' - Rendering bgp template'
		bgp_conf=open(path_render_files + 'bgp_' + device_item + '.txt','w')
		bgp_conf.write(bgp_template.render(bgp_vars))
		bgp_conf.close()
		
		# Create Device Object
		print ' - Creating Device object'
		device_driver = get_network_driver(driver)
		device_connect = device_driver(hostname=mgmt_ip, username=username, password=password)

		# Configuring the device
		print ' - Configuring Device'
		try:
			filepath = path_render_files + "bgp_" + device_item + ".txt"
			change_configuration(device_connect, filepath)
		except:
			print " Not able to reach the device \n"
	except:
		print " Not able to find variables for the device \n"


# Audit the devices
print '-'*60
print ('Audit will start in 15 seconds')
print '-'*60
print('\n')
time.sleep(15)

for device_item in inventory:
	print('-'*60)
	print ('Printing bgp sessions state for device '+ device_item)
	print('-'*60)

	mgmt_ip = inventory[device_item]['mgmt_ip']
	username = inventory[device_item]['username']
	password = inventory[device_item]['password']
	driver = inventory[device_item]['driver']
	
	if driver == "eos":
		vrf_name = "default"
	elif driver == "junos":
		vrf_name = "global"

	# Create Device Object
	device_driver = get_network_driver(driver)
	device_connect = device_driver(hostname=mgmt_ip, username=username, password=password)

	try:
		device_connect.open()
		for bgp_item in device_connect.get_bgp_neighbors_detail()[vrf_name]:
			print (' Peer ' + device_connect.get_bgp_neighbors_detail()[vrf_name][bgp_item][0]['remote_address'] + ' is ' + device_connect.get_bgp_neighbors_detail()[vrf_name][bgp_item][0]['connection_state'])
		device_connect.close()
	except:
		print " Not able to find variables for the device \n"
