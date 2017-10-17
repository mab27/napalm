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
print('-'*20+ " Arista EOS " + '-'*28)
print('-'*60)

#oc_config =open('/home/mab/mab_automate/napalm/openconfig/models/interfaces.yml', 'r')

with eos_driver(**arista1) as eos:
    oc_config_file = open('/home/mab/mab_automate/napalm/openconfig/configs/interfaces/eos.yml', 'r')
    oc_config = oc_config_file.read()
    oc_config_file.close()
    config =load(oc_config)
    conf = napalm_yang.base.Root()
    conf.add_model(napalm_yang.models.openconfig_interfaces())
    conf.load_dict(config)
    print(conf.translate_config(eos.profile))

print('-'*60)
print('-'*20+ " Juniper JunOS " + '-'*25)
print('-'*60)

with junos_driver(**vmx1) as junos:
    oc_config_file = open('/home/mab/mab_automate/napalm/openconfig/configs/interfaces/junos.yml', 'r')
    oc_config = oc_config_file.read()
    oc_config_file.close()
    config =load(oc_config)
    conf = napalm_yang.base.Root()
    type(conf)
    conf.add_model(napalm_yang.models.openconfig_interfaces())
    conf.load_dict(config)
    print(conf.translate_config(junos.profile))
