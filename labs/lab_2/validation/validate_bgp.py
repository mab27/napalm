from napalm_base import get_network_driver
from yaml import load
import pprint

# Getting inventory in a python data structure. 
inventory_file =open('/home/mab/mab_automate/napalm/inventory/inventory.yml', 'r')
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

	validate_file_path = "validate_files/" + device_item + "_bgp.yml"

	# Create Device Object
	device_driver = get_network_driver(driver)
	device_connect = device_driver(hostname=mgmt_ip, username=username, password=password)

	try:
		print " Validation file : " + validate_file_path
		device_connect.open()
		pprint.pprint(device_connect.compliance_report(validate_file_path))
		device_connect.close()
	except:
		print " Not able to reach the device \n"