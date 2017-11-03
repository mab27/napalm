### Translate OpenConfig to native configuration

from napalm_base import get_network_driver
import napalm_yang
from pprint import pprint
from json import dumps
from yaml import load

# Create Device Object
eos_driver = get_network_driver('eos')
junos_driver = get_network_driver('junos')

arista1 = {
    'hostname': '192.168.0.70',
    'username': 'admin',
    'password': 'admin123',
    'optional_args' : {'profile':["eos"]}
}

vmx1 = {
    'hostname': '192.168.0.30',
    'username': 'mab',
    'password': 'mab123',
    'optional_args' : {'profile':["junos"]}
}

print('-'*60)
print ('Device : ' + 'arista1')
print('-'*60)

with eos_driver(**arista1) as arista1_device:
    oc_config_file = open('/home/mab/mab_automate/napalm/openconfig/configs/interfaces/eos.yml', 'r')
    oc_config = oc_config_file.read()
    oc_config_file.close()
    config =load(oc_config)
    conf = napalm_yang.base.Root()
    conf.add_model(napalm_yang.models.openconfig_interfaces())
    conf.load_dict(config)
    print(conf.translate_config(arista1_device.profile))

print('-'*60)
print ('Device : ' + 'vmx1')
print('-'*60)

with junos_driver(**vmx1) as vmx1_device:
    oc_config_file = open('/home/mab/mab_automate/napalm/openconfig/configs/interfaces/junos.yml', 'r')
    oc_config = oc_config_file.read()
    oc_config_file.close()
    config =load(oc_config)
    conf = napalm_yang.base.Root()
    type(conf)
    conf.add_model(napalm_yang.models.openconfig_interfaces())
    conf.load_dict(config)
    print(conf.translate_config(vmx1_device.profile))
