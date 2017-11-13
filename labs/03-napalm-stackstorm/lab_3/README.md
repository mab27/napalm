# Lab_3

## Overview:
- Event-Driven automation
- Sections:
    - [Setters (configuration commands)](https://github.com/mab27/napalm/tree/master/labs/03-napalm-st2/lab_3#setters-configuration-commands)
    [Validation (configuration/state check)]()

## Setters (configuration commands):

### Fire a bgp configuration workflow from a Github Commit:

- This is about using the same previous workflow **cfg_bgp_all** and attaching a rule to automatically fire this workflow based on a specfic event. This is essentially is the event-driven functionality which is the crux of Stackstorm. It allows to perform workflow automation without the need to manually invoke the st2 corresponding action.
- As an event we are going to choose a commit on the github repo as our event. To do that, we'll rely on a built-in sensor from the **git** pack: **GitCommitSensor**. This sensor polls a given Git repository for new commits. When a new commit is detected, a trigger is dispatched. In StackStorm the word **trigger** refers to an object that is a representation of an event. When the event occurs, the sensor produces a trigger that flows to the rule Engine, which in turns checks it for any match against the existing rules.

- We create a rule that matches the trigger type **git.head_sha_monitor**, which is the trigger dispatched by the sensor **git.GitCommitSensor**. That rule will fire fire the **cfg_ebgp_iac** workflow.
	- [The_created_Rule]()

- Upon creation of the rule, make sure it is registered:
```
mab@mab-infra:~$ st2 rule list -p default
+---------------------------+---------+------------------------------------------+---------+
| ref                       | pack    | description                              | enabled |
+---------------------------+---------+------------------------------------------+---------+
| default.github_commit_iac | default | Fire cfg_ebgp_iac WF upon github commit. | True    |
+---------------------------+---------+------------------------------------------+---------+
```

- Follow the instructions [here](https://github.com/StackStorm-Exchange/stackstorm-git#git-integration-pack) to configure the sensor. Remember to re-load the config after each modification to that file with. To do that you can either use the ```st2ctl``` command or the ```pack register``` feature:

```
sudo st2ctl reload --register-configs
```
or:

```
mab@mab-infra:~$ st2 pack register git
+--------------+-------+
| Property     | Value |
+--------------+-------+
| actions      | 3     |
| aliases      | 0     |
| configs      | 1     |
| policies     | 0     |
| policy_types | 3     |
| rule_types   | 2     |
| rules        | 1     |
| runners      | 13    |
| sensors      | 1     |
| triggers     | 0     |
+--------------+-------+
```
- Make sure the sensor is enabled:
```
mab@mab-infra:~$ st2 sensor list -p git
+---------------------+------+-----------------------------------------------------+---------+
| ref                 | pack | description                                         | enabled |
+---------------------+------+-----------------------------------------------------+---------+
| git.GitCommitSensor | git  | Sensor which monitors git repositories for new      | True    |
|                     |      | commits                                             |         |
+---------------------+------+-----------------------------------------------------+---------+
mab@mab-infra:/opt/stackstorm/packs/git$
```
- Git add/commit/push this to the [remote repository](https://github.com/mab27/network_iac):
```
```
- Check if the rule has been enforced:
```
mab@mab-infra:~$ st2 rule-enforcement list -n 5
+--------------------------+----------------------------+--------------------------+--------------------------+-----------------------------+
| id                       | rule.ref                   | trigger_instance_id      | execution_id             | enforced_at                 |
+--------------------------+----------------------------+--------------------------+--------------------------+-----------------------------+
| 5a05a3127cae2204054481be | default.github_commit_iac  | 5a05a3127cae2204054481ba | 5a05a3127cae2204054481bd | 2017-11-10T13:01:06.522258Z |
| 5a05a21b7cae220405448165 | default.github_commit_iac  | 5a05a21a7cae22040544815e | 5a05a21a7cae220405448164 | 2017-11-10T12:56:58.656683Z |
| 5a05a21a7cae220405448162 | napalm_2.github_commit_iac | 5a05a21a7cae22040544815e | 5a05a21a7cae220405448161 | 2017-11-10T12:56:58.306501Z |
| 5a059c507cae22040544801f | napalm_2.github_commit_iac | 5a059c4f7cae22040544801b | 5a059c4f7cae22040544801e | 2017-11-10T12:32:15.901494Z |
| 5a0577847cae2203f1464ecf | napalm_2.github_commit_iac | 5a0577847cae2203f1464ecb | 5a0577847cae2203f1464ece | 2017-11-10T09:55:16.550030Z |
+--------------------------+----------------------------+--------------------------+--------------------------+-----------------------------+
+-------------------------------------------------------------------------------------------------------------------------------------------+
| Note: Only first 5 rule enforcements are displayed. Use -n/--last flag for more results.                                                  |
+-------------------------------------------------------------------------------------------------------------------------------------------+
mab@mab-infra:~$
```
- Check the details of the rule that has been enfored
```
mab@mab-infra:~$ st2 rule-enforcement get 5a05a3127cae2204054481be
+---------------------+-----------------------------+
| Property            | Value                       |
+---------------------+-----------------------------+
| id                  | 5a05a3127cae2204054481be    |
| rule.ref            | default.github_commit_iac   |
| trigger_instance_id | 5a05a3127cae2204054481ba    |
| execution_id        | 5a05a3127cae2204054481bd    |
| failure_reason      |                             |
| enforced_at         | 2017-11-10T13:01:06.522258Z |
+---------------------+-----------------------------+
mab@mab-infra:~$ 
```

- Check the content of the trigger that has been dispatched:
```
mab@mab-infra:~$ st2 trigger-instance get 5a05a3127cae2204054481ba
+-----------------+--------------------------------------------------------------+
| Property        | Value                                                        |
+-----------------+--------------------------------------------------------------+
| id              | 5a05a3127cae2204054481ba                                     |
| trigger         | git.head_sha_monitor                                         |
| occurrence_time | 2017-11-10T13:01:06.490000Z                                  |
| payload         | {                                                            |
|                 |     "author_tz_offset": -3600,                               |
|                 |     "committer": "mab27",                                    |
|                 |     "committer_email": "mehdi_abdelouahab@hotmail.com",      |
|                 |     "author": "mab27",                                       |
|                 |     "author_email": "mehdi_abdelouahab@hotmail.com",         |
|                 |     "committer_tz_offset": -3600,                            |
|                 |     "branch": "master",                                      |
|                 |     "committed_date": "2017-11-10T14:00:42Z",                |
|                 |     "repository_url":                                        |
|                 | "https://github.com/mab27/network_iac",                      |
|                 |     "commit_message": "1 st try iac                          |
|                 | ",                                                           |
|                 |     "authored_date": "2017-11-10T14:00:42Z",                 |
|                 |     "revision": "1d8f1b58a2f9d784286b3457ea25bfe1903c91a6"   |
|                 | }                                                            |
| status          | processed                                                    |
+-----------------+--------------------------------------------------------------+
mab@mab-infra:~$
```
- Notice the different fields included in this trigger-type (like **committer**, **branch**, **revision** etc ...). You can use them a a filtering criteria in your rule but also as information you can pass as parameters to the workflows.

- Check the details of the workflow that has been fired, as a result of the rule enforcement:
```
mab@mab-infra:~$ st2 execution get 5a05a3127cae2204054481bd
id: 5a05a3127cae2204054481bd
action.ref: napalm.cfg_bgp_all_iac
parameters: 
  hosted_repo: https://github.com/mab27/network_iac
status: failed (65s elapsed)
result_task: remove_local_content
result: 
  localhost:
    failed: false
    return_code: 0
    stderr: ''
    stdout: ''
    succeeded: true
start_timestamp: 2017-11-10T13:01:06.553219Z
end_timestamp: 2017-11-10T13:02:11.313099Z
+-----------------------------+------------------------+----------------------+--------------------------+-------------------------------+
| id                          | status                 | task                 | action                   | start_timestamp               |
+-----------------------------+------------------------+----------------------+--------------------------+-------------------------------+
|   5a05a3137cae220746b93021  | succeeded (2s elapsed) | git_clone            | git.clone                | Fri, 10 Nov 2017 13:01:07 UTC |
| + 5a05a3157cae220746b93023  | failed (43s elapsed)   | cfg_bgp_all          | napalm.cfg_bgp_all       | Fri, 10 Nov 2017 13:01:09 UTC |
|    5a05a3167cae220746b93025 | succeeded (2s elapsed) | get_inventory        | napalm.file_to_obj       | Fri, 10 Nov 2017 13:01:09 UTC |
|    5a05a3187cae220746b9302b | succeeded (3s elapsed) | render_config        | default.render_file      | Fri, 10 Nov 2017 13:01:12 UTC |
|    5a05a3187cae220746b9302a | failed (3s elapsed)    | render_config        | default.render_file      | Fri, 10 Nov 2017 13:01:12 UTC |
|    5a05a3187cae220746b9302c | failed (3s elapsed)    | render_config        | default.render_file      | Fri, 10 Nov 2017 13:01:12 UTC |
|    5a05a3187cae220746b9302d | succeeded (3s elapsed) | render_config        | default.render_file      | Fri, 10 Nov 2017 13:01:12 UTC |
|    5a05a31c7cae220746b9302f | succeeded (7s elapsed) | load_config          | napalm.loadconfig        | Fri, 10 Nov 2017 13:01:16 UTC |
|    5a05a31c7cae220746b93033 | failed (6s elapsed)    | load_config          | napalm.loadconfig        | Fri, 10 Nov 2017 13:01:16 UTC |
|    5a05a31c7cae220746b93034 | failed (7s elapsed)    | load_config          | napalm.loadconfig        | Fri, 10 Nov 2017 13:01:16 UTC |
|    5a05a31c7cae220746b93035 | succeeded (6s elapsed) | load_config          | napalm.loadconfig        | Fri, 10 Nov 2017 13:01:16 UTC |
|    5a05a3327cae220746b9303b | succeeded (4s elapsed) | audit_config         | napalm.get_bgp_neighbors | Fri, 10 Nov 2017 13:01:38 UTC |
|    5a05a3327cae220746b9303a | failed (6s elapsed)    | audit_config         | napalm.get_bgp_neighbors | Fri, 10 Nov 2017 13:01:38 UTC |
|    5a05a3327cae220746b9303c | failed (6s elapsed)    | audit_config         | napalm.get_bgp_neighbors | Fri, 10 Nov 2017 13:01:38 UTC |
|    5a05a3327cae220746b9303d | succeeded (3s elapsed) | audit_config         | napalm.get_bgp_neighbors | Fri, 10 Nov 2017 13:01:38 UTC |
|    5a05a3387cae220746b9303f | succeeded (0s elapsed) | end_task             | core.noop                | Fri, 10 Nov 2017 13:01:44 UTC |
|   5a05a3417cae220746b93041  | succeeded (2s elapsed) | remove_local_content | linux.rm                 | Fri, 10 Nov 2017 13:01:53 UTC |
+-----------------------------+------------------------+----------------------+--------------------------+-------------------------------+
mab@mab-infra:~$
```

## Validation (configuration/state check):

### React to a decrease in number of LLDP neighbors:

- First enable the ```NapalmLLDPSensor```:
```
mab@mab-infra:~$ st2 sensor enable napalm.NapalmLLDPSensor
+---------------+--------------------------------------------------------------+
| Property      | Value                                                        |
+---------------+--------------------------------------------------------------+
| id            | 59d3a00c7cae2206f9add1ed                                     |
| name          | NapalmLLDPSensor                                             |
| pack          | napalm                                                       |
| description   | Sensor that uses NAPALM to retrieve LLDP information from    |
|               | network devices                                              |
| artifact_uri  | file:///opt/stackstorm/packs/napalm/sensors/lldp_sensor.py   |
| enabled       | True                                                         |
| entry_point   | sensors.lldp_sensor.NapalmLLDPSensor                         |
| trigger_types | [                                                            |
|               |     "napalm.LLDPNeighborDecrease",                           |
|               |     "napalm.LLDPNeighborDecrease"                            |
|               | ]                                                            |
| uid           | sensor_type:napalm:NapalmLLDPSensor                          |
+---------------+--------------------------------------------------------------+
mab@mab-infra:~$
```
- Then shut down a device in order to create, on another device, the condition of a decrease of LLDP neighbor. In our case we are disconnecting the vMX.
- Check if the trigger has been dispatched:
```
mab@mab-infra:~$ st2 trigger-instance list -n 10
+--------------------------+--------------------------------+-------------------------------+-----------+
| id                       | trigger                        | occurrence_time               | status    |
+--------------------------+--------------------------------+-------------------------------+-----------+
| 5a05c7f67cae22047e60b324 | core.st2.sensor.process_spawn  | Fri, 10 Nov 2017 15:38:30 UTC | processed |
| 5a05c7fe7cae22047e60b326 | core.st2.generic.actiontrigger | Fri, 10 Nov 2017 15:38:38 UTC | processed |
| 5a05c8097cae22047e60b327 | core.st2.generic.actiontrigger | Fri, 10 Nov 2017 15:38:49 UTC | processed |
| 5a05c80c7cae22047e60b328 | core.st2.sensor.process_exit   | Fri, 10 Nov 2017 15:38:52 UTC | processed |
| 5a05c80f7cae22047e60b32a | core.st2.sensor.process_spawn  | Fri, 10 Nov 2017 15:38:55 UTC | processed |
| 5a05c8147cae22047e60b32c | core.st2.generic.actiontrigger | Fri, 10 Nov 2017 15:39:00 UTC | processed |
| 5a05c81f7cae22047e60b32d | napalm.LLDPNeighborDecrease    | Fri, 10 Nov 2017 15:39:11 UTC | processed |
| 5a05c8217cae22047e60b332 | core.st2.generic.actiontrigger | Fri, 10 Nov 2017 15:39:13 UTC | processed |
| 5a05c8227cae22047e60b333 | core.st2.generic.actiontrigger | Fri, 10 Nov 2017 15:39:14 UTC | processed |
| 5a05c8257cae22047e60b334 | core.st2.sensor.process_exit   | Fri, 10 Nov 2017 15:39:17 UTC | processed |
+--------------------------+--------------------------------+-------------------------------+-----------+
+-------------------------------------------------------------------------------------------------------+
| Note: Only first 10 triggerinstances are displayed. Use -n/--last flag for more results.              |
+-------------------------------------------------------------------------------------------------------+
mab@mab-infra:~$
```
- Or you can filter on the name of the trigger:

```
mab@mab-infra:~$ st2 trigger-instance list --trigger napalm.LLDPNeighborDecrease -n 10
+--------------------------+-----------------------------+-------------------------------+-----------+
| id                       | trigger                     | occurrence_time               | status    |
+--------------------------+-----------------------------+-------------------------------+-----------+
| 5a05c81f7cae22047e60b32d | napalm.LLDPNeighborDecrease | Fri, 10 Nov 2017 15:39:11 UTC | processed |
+--------------------------+-----------------------------+-------------------------------+-----------+
mab@mab-infra:~$
```

- Check the details of the rule that has been enfored
```
mab@mab-infra:~$ st2 rule-enforcement get 5a05d5227cae22047e60b57f
+---------------------+--------------------------------+
| Property            | Value                          |
+---------------------+--------------------------------+
| id                  | 5a05d5227cae22047e60b57f       |
| rule.ref            | default.lldp_neighbor_decrease |
| trigger_instance_id | 5a05d5217cae22047e60b578       |
| execution_id        | 5a05d5227cae22047e60b57e       |
| failure_reason      |                                |
| enforced_at         | 2017-11-10T16:34:41.979049Z    |
+---------------------+--------------------------------+
mab@mab-infra:~$ 
```

- Then you can check the details of the trigger-instance, it will give information like the **device** name, number of **OldPeers**, number of **NewPeers**:
```
mab@mab-infra:~$ st2 trigger-instance get 5a05c81f7cae22047e60b32d
+-----------------+-------------------------------------------------+
| Property        | Value                                           |
+-----------------+-------------------------------------------------+
| id              | 5a05c81f7cae22047e60b32d                        |
| trigger         | napalm.LLDPNeighborDecrease                     |
| occurrence_time | 2017-11-10T15:39:11.713000Z                     |
| payload         | {                                               |
|                 |     "device": "arista1",                        |
|                 |     "timestamp": "2017-11-10 16:39:11.708087",  |
|                 |     "oldpeers": 2,                              |
|                 |     "newpeers": 0                               |
|                 | }                                               |
| status          | processed                                       |
+-----------------+-------------------------------------------------+
mab@mab-infra:~$
```
- Check if the rule has been enforced:
```
mab@mab-infra:~$ st2 rule-enforcement list -n 10
+--------------------------+--------------------------------+--------------------------+--------------------------+-----------------------------+
| id                       | rule.ref                       | trigger_instance_id      | execution_id             | enforced_at                 |
+--------------------------+--------------------------------+--------------------------+--------------------------+-----------------------------+
| 5a05d5227cae22047e60b57f | default.lldp_neighbor_decrease | 5a05d5217cae22047e60b578 | 5a05d5227cae22047e60b57e | 2017-11-10T16:34:41.979049Z |
| 5a05d5217cae22047e60b57c | napalm.lldp_remediate          | 5a05d5217cae22047e60b578 | 5a05d5217cae22047e60b57b | 2017-11-10T16:34:41.736815Z |
| 5a05cf6b7cae22047e60b465 | default.github_commit_iac      | 5a05cf6b7cae22047e60b461 | 5a05cf6b7cae22047e60b464 | 2017-11-10T16:10:19.457252Z |
| 5a05c81f7cae22047e60b331 | napalm.lldp_remediate          | 5a05c81f7cae22047e60b32d | 5a05c81f7cae22047e60b330 | 2017-11-10T15:39:11.731455Z |
| 5a05c4527cae22047e60b271 | default.github_commit_iac      | 5a05c4527cae22047e60b26d | 5a05c4527cae22047e60b270 | 2017-11-10T15:22:58.059714Z |
| 5a05b1577cae22047e60af41 | default.github_commit_iac      | 5a05b1567cae22047e60af3d | 5a05b1577cae22047e60af40 | 2017-11-10T14:01:58.989730Z |
| 5a05a3127cae2204054481be | default.github_commit_iac      | 5a05a3127cae2204054481ba | 5a05a3127cae2204054481bd | 2017-11-10T13:01:06.522258Z |
| 5a05a21b7cae220405448165 | default.github_commit_iac      | 5a05a21a7cae22040544815e | 5a05a21a7cae220405448164 | 2017-11-10T12:56:58.656683Z |
| 5a05a21a7cae220405448162 | napalm_2.github_commit_iac     | 5a05a21a7cae22040544815e | 5a05a21a7cae220405448161 | 2017-11-10T12:56:58.306501Z |
| 5a059c507cae22040544801f | napalm_2.github_commit_iac     | 5a059c4f7cae22040544801b | 5a059c4f7cae22040544801e | 2017-11-10T12:32:15.901494Z |
+--------------------------+--------------------------------+--------------------------+--------------------------+-----------------------------+
+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Note: Only first 10 rule enforcements are displayed. Use -n/--last flag for more results.                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------+
mab@mab-infra:~$ 
```
- Check the content of the trigger that has been dispatched:
```
mab@mab-infra:~$ st2 trigger-instance get 5a05d5217cae22047e60b578
+-----------------+-------------------------------------------------+
| Property        | Value                                           |
+-----------------+-------------------------------------------------+
| id              | 5a05d5217cae22047e60b578                        |
| trigger         | napalm.LLDPNeighborDecrease                     |
| occurrence_time | 2017-11-10T16:34:41.714000Z                     |
| payload         | {                                               |
|                 |     "device": "arista1",                        |
|                 |     "timestamp": "2017-11-10 17:34:41.708999",  |
|                 |     "oldpeers": 2,                              |
|                 |     "newpeers": 0                               |
|                 | }                                               |
| status          | processed                                       |
+-----------------+-------------------------------------------------+
mab@mab-infra:~$ 
```
- Check the details of the workflow that has been fired, as a result of the rule enforcement:
```
mab@mab-infra:~$ st2 execution get 5a05d5227cae22047e60b57e
id: 5a05d5227cae22047e60b57e
status: succeeded (3s elapsed)
parameters: 
  hostname: arista1
  repository: https://github.com/mab27/network_iac.git
result: 
  exit_code: 0
  result:
    deviation: false
    diff_contents: ''
  stderr: ''
  stdout: ''
mab@mab-infra:~$ 
```

### Fire an investigation workflow from a generic Webhook:

- Systems that push data to the ST2 API when an event you are interested in occurs.
- Webhooks come handy is when you want to consume events from a 3rd party service which already offer webhooks integration - e.g. GitHub
- Webhooks aren't directly created --> they're created via rules.
- The rules in this pack are written using one of the default triggers: ```core.st2.webhook``` --> This means that the rule will be watching for incoming events that are in the form of a custom webhook.
- POST-ing data to a custom webhook will cause a trigger with the following attributes to be dispatched:
	- **trigger** - Trigger name.
	- **trigger.headers** - Dictionary containing the request headers.
	- **trigger.body** - Dictionary containing the request body.

- Obtain an authentication token. You'll need it to replace **$TOKEN** in the cURL commands below:
```
mab@mab-infra:~$ st2 auth username-goes-here -p password-goes-here
+----------+----------------------------------+
| Property | Value                            |
+----------+----------------------------------+
| user     | st2admin                         |
| token    | dfe66f29038c443eb5a7050be96857e8 |
| expiry   | 2017-11-14T10:49:24.539303Z      |
+----------+----------------------------------+
mab@mab-infra:~$
```

- Send the following HTTP call via cURL command:
```
curl -k -H "Content-Type:application/json" -H "X-Auth-Token:$TOKEN" -d '{"logsource":"vmx1","message":"BGP-EXCEED-LIMIT","neighbor":"192.168.0.40","asnum":"102","prefixes":"50"}' http://localhost:9101/v1/webhooks/napalm_bgp_prefix_exceeded
```

- Below an example with a real token:
```
mab@mab-infra:~$ curl -k -H "Content-Type:application/json" -H "X-Auth-Token:dfe66f29038c443eb5a7050be96857e8" -d '{"logsource":"vmx1","message":"BGP-EXCEED-LIMIT","neighbor":"192.168.0.40","asnum":"102","prefixes":"50"}' http://localhost:9101/v1/webhooks/napalm_bgp_prefix_exceeded
{
    "prefixes": "50",
    "message": "BGP-EXCEED-LIMIT",
    "logsource": "vmx1",
    "asnum": "102",
    "neighbor": "192.168.0.40"
}mab@mab-infra:~$
```

- Check if the rule has been enforced:
```
mab@mab-infra:~$ st2 rule-enforcement list -n 10+--------------------------+--------------------------------+--------------------------+--------------------------+-----------------------------+
| id                       | rule.ref                       | trigger_instance_id      | execution_id             | enforced_at                 |
+--------------------------+--------------------------------+--------------------------+--------------------------+-----------------------------+
| 5a0980af7cae224896857192 | napalm.bgp_prefix_exceeded     | 5a0980af7cae22489685718e | 5a0980af7cae224896857191 | 2017-11-13T11:23:27.356188Z |
| 5a0980507cae224896857172 | napalm.bgp_prefix_exceeded     | 5a09804f7cae22489685716e | 5a0980507cae224896857171 | 2017-11-13T11:21:51.938120Z |
| 5a097ee97cae224896857124 | napalm.bgp_prefix_exceeded     | 5a097ee97cae224896857120 | 5a097ee97cae224896857123 | 2017-11-13T11:15:53.346424Z |
| 5a097db07cae2248968570e7 | napalm.bgp_prefix_exceeded     | 5a097db07cae2248968570e3 | 5a097db07cae2248968570e6 | 2017-11-13T11:10:40.672397Z |
| 5a097c557cae22489685709b | napalm.bgp_prefix_exceeded     | 5a097c557cae224896857097 | 5a097c557cae22489685709a | 2017-11-13T11:04:53.602724Z |
| 5a097bf67cae224896857074 | napalm.bgp_prefix_exceeded     | 5a097bf67cae224896857072 |                          | 2017-11-13T11:03:18.108703Z |
| 5a0978c77cae22040cdeabc7 | napalm.bgp_prefix_exceeded     | 5a0978c77cae22040cdeabc5 |                          | 2017-11-13T10:49:43.112633Z |
| 5a0978ab7cae22040cdeabbe | napalm.bgp_prefix_exceeded     | 5a0978ab7cae22040cdeabbc |                          | 2017-11-13T10:49:15.032781Z |
| 5a05d5227cae22047e60b57f | default.lldp_neighbor_decrease | 5a05d5217cae22047e60b578 | 5a05d5227cae22047e60b57e | 2017-11-10T16:34:41.979049Z |
| 5a05d5217cae22047e60b57c | napalm.lldp_remediate          | 5a05d5217cae22047e60b578 | 5a05d5217cae22047e60b57b | 2017-11-10T16:34:41.736815Z |
+--------------------------+--------------------------------+--------------------------+--------------------------+-----------------------------+
+-----------------------------------------------------------------------------------------------------------------------------------------------+
| Note: Only first 10 rule enforcements are displayed. Use -n/--last flag for more results.                                                     |
+-----------------------------------------------------------------------------------------------------------------------------------------------+
mab@mab-infra:~$ 
```

- Check the details of the rule that has been enforced:
```
mab@mab-infra:~$ st2 rule-enforcement get 5a0981697cae2248968571be
+---------------------+-----------------------------+
| Property            | Value                       |
+---------------------+-----------------------------+
| id                  | 5a0981697cae2248968571be    |
| rule.ref            | napalm.bgp_prefix_exceeded  |
| trigger_instance_id | 5a0981697cae2248968571ba    |
| execution_id        | 5a0981697cae2248968571bd    |
| failure_reason      |                             |
| enforced_at         | 2017-11-13T11:26:33.452145Z |
+---------------------+-----------------------------+
```

- Check the details of the trigger-instance:
```
mab@mab-infra:~$ st2 trigger-instance get 5a0980af7cae22489685718e
+-----------------+--------------------------------------------------------------+
| Property        | Value                                                        |
+-----------------+--------------------------------------------------------------+
| id              | 5a0980af7cae22489685718e                                     |
| trigger         | core.6299082c-03f7-4d45-87c9-74095dd2d437                    |
| occurrence_time | 2017-11-13T11:23:27.301000Z                                  |
| payload         | {                                                            |
|                 |     "body": {                                                |
|                 |         "prefixes": "50",                                    |
|                 |         "message": "BGP-EXCEED-LIMIT",                       |
|                 |         "logsource": "vmx1",                                 |
|                 |         "asnum": "102",                                      |
|                 |         "neighbor": "172.16.0.40"                            |
|                 |     },                                                       |
|                 |     "headers": {                                             |
|                 |         "Content-Length": "104",                             |
|                 |         "X-Request-Id": "0fcd7623-f0ff-                      |
|                 | 46f1-be64-20641df0fe2d",                                     |
|                 |         "Accept": "*/*",                                     |
|                 |         "X-Auth-Token": "dfe66f29038c443eb5a7050be96857e8",  |
|                 |         "Host": "localhost:9101",                            |
|                 |         "User-Agent": "curl/7.47.0",                         |
|                 |         "Content-Type": "application/json"                   |
|                 |     }                                                        |
|                 | }                                                            |
| status          | processed                                                    |
+-----------------+--------------------------------------------------------------+
mab@mab-infra:~$
```

- Check the details of the action/workflow execution resulted from this trigger:
```
mab@mab-infra:~$ st2 execution get 5a0980af7cae224896857191
id: 5a0980af7cae224896857191
action.ref: napalm.bgp_prefix_exceeded_chain
parameters: 
  asnum: '102'
  hostname: vmx1
  message: BGP-EXCEED-LIMIT
  neighbor: 172.16.0.40
  prefixes: 50
status: failed (17s elapsed)
result_task: send_email
result: 
  failed: true
  return_code: 2
  stderr: Unable to find sendmail binary in PATH
  stdout: ''
  succeeded: false
start_timestamp: 2017-11-13T11:23:27.426076Z
end_timestamp: 2017-11-13T11:23:44.355119Z
+--------------------------+------------------------+--------------------+--------------------------+-------------------------------+
| id                       | status                 | task               | action                   | start_timestamp               |
+--------------------------+------------------------+--------------------+--------------------------+-------------------------------+
| 5a0980af7cae224869fa9108 | succeeded (3s elapsed) | show_bgp_neighbors | napalm.get_bgp_neighbors | Mon, 13 Nov 2017 11:23:27 UTC |
| 5a0980b37cae224869fa910a | succeeded (2s elapsed) | show_route         | napalm.get_route_to      | Mon, 13 Nov 2017 11:23:31 UTC |
| 5a0980b67cae224869fa910c | succeeded (5s elapsed) | show_log           | napalm.get_log           | Mon, 13 Nov 2017 11:23:34 UTC |
| 5a0980bc7cae224869fa910e | succeeded (0s elapsed) | get_html_header    | core.local               | Mon, 13 Nov 2017 11:23:40 UTC |
| 5a0980bd7cae224869fa9110 | succeeded (1s elapsed) | get_html_footer    | core.local               | Mon, 13 Nov 2017 11:23:41 UTC |
| 5a0980bf7cae224869fa9112 | failed (0s elapsed)    | send_email         | core.sendmail            | Mon, 13 Nov 2017 11:23:43 UTC |
+--------------------------+------------------------+--------------------+--------------------------+-------------------------------+
mab@mab-infra:~$
```
