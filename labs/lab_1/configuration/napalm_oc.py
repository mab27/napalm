from napalm_base import get_network_driver
import napalm_yang
from json import dumps
from pprint import pprint

# Create Device Object
junos_driver = get_network_driver('junos')

junos_device = {
	'hostname': '192.168.0.30',
	'username': 'mab',
	'password': 'mab123',
}

with junos_driver(**junos_device) as d:
	running_config = napalm_yang.base.Root()
	running_config.add_model(napalm_yang.models.openconfig_interfaces)
	running_config.parse_config(device=d)

print dumps(running_config.get(filter=True), indent=4)
