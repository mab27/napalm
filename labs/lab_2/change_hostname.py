from napalm_base import get_network_driver
from yaml import load
from json import dumps
import pprint

pp = pprint.PrettyPrinter(indent=4)

# getting inventory in a python data structure. 
inventory_file =open('/home/mab/mab_automate/napalm/inventory/inventory.yml', 'r')


inventory_structure =inventory_file.read()
inventory_file.close()
inventory =load(inventory_structure)

def change_configuration(device, configuration):
	device.load_merge_candidate(config=configuration)
	print(device.compare_config())
	device.commit_config()


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

	device_hostname = inventory[device_item]['hostname']

	if driver == "eos":
		command = "hostname " + device_hostname
	elif driver == "junos":
		command = "system {host-name " + device_hostname + ";}"

	try:
		device_connect.open()
		change_configuration(device_connect,command)
		device_connect.close()
		print "\n"
	except:
		print " Not able to reach the device \n"
