- In order to allow scalability, this folder should be structured this was:
	- One directory per use-case. Example ```ebgp```.
	- Inside each directory one file per vendor, the name of the file should be the exact same name as the provider (in NAPALM). Example ```eos.j2``` for Arista, ```junos.j2``` for Juniper ...

This structure allows to expand both the templates for a given workflow as well as writing workflows for new use-cases.