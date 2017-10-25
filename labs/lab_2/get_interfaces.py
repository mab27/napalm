from napalm_base import get_network_driver
from yaml import load
from json import dumps

# getting inventory in a python data structure. 
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

	# Create Device Object
	device_driver = get_network_driver(driver)
	device_connect = device_driver(hostname=mgmt_ip, username=username, password=password)

	try:
		device_connect.open()
		print "JSON dumps print: \n"
		print dumps(device_connect.get_interfaces(), indent=4)
		print "\n"
		device_connect.close()
	except:
		print " Not able to reach the device \n"
