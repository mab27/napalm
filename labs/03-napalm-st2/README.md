# NAPALM with StackStorm:
- This is about consuming napalm from StackStorm

## How to (in order):
- 1) Use stackstorm command to install the pack (includes git clone, install dependencies, registration etc ...):
```
st2 pack install napalm
```
- 2) Edit the ```napalm.yaml``` configuration file, you'll find in this repo the [example I used]().
	- A reload of the config is required upon each modificatiton to that file. To do that you can either use the ```st2ctl``` command: ```sudo st2ctl reload --register-configs``` or the use the pack register feature: ```st2 pack register napalm```.
- 3) Copy the content of ```my_pack``` folder in ```/opt/stacksotrm/packs/default/``` and register the content ```st2ctl reload --register-actions```.
