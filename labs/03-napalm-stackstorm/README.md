# NAPALM with StackStorm:
- This is about consuming napalm from StackStorm.

## Content:

- [Lab_1](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_1): Manual-Driven automation, with standalone ST2 actions.
- [Lab_2](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_2): Manual-Driven automation, with ST2 workflows (to handle network inventory).
- [Lab_3](https://github.com/mab27/napalm/tree/master/labs/03-napalm-stackstorm/lab_3): Event-Driven automation.


## How to install NAPALM pack:
- 1) Use stackstorm command to install the pack (includes git clone, install dependencies, registration etc ...):
```
st2 pack install napalm
```
- 2) Edit the ```napalm.yaml``` configuration file, you'll find in this repo the [example I used]().
	- A reload of the config is required upon each modificatiton to that file. To do that you can either use the ```st2ctl``` command: ```sudo st2ctl reload --register-configs``` or the use the pack register feature: ```st2 pack register napalm```.
- 3) Copy the content of ```my_pack``` folder in ```/opt/stacksotrm/packs/default/``` and register the content ```st2ctl reload --register-actions```.

