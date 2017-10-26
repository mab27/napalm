### Translate OpenConfig to native configuration

from napalm_base import get_network_driver
import napalm_yang
from yaml import load
from json import dumps

# Path to folders 
inventory_file_path = "/home/mab/mab_automate/napalm/inventory/inventory.yml"

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

	# Create Device Object
	device_driver = get_network_driver(driver)
	device_connect = device_driver(hostname=mgmt_ip, username=username, password=password)

	try:
		path = '/home/mab/mab_automate/napalm/openconfig/configs/interfaces/' + driver + '.yml'
		oc_config_file = open(path, 'r')
		oc_config = oc_config_file.read()
		oc_config_file.close()
		config =load(oc_config)
		conf = napalm_yang.base.Root()
		conf.add_model(napalm_yang.models.openconfig_interfaces())
		conf.load_dict(config)
		print(conf.translate_config(device_connect.profile))
	except:
		print " Not able to reach the device \n"
