# Lab3

## Overview:
- Event-Driven automation
- Sections:
    - [Setters (configuration commands)]()

## Setters (configuration commands):

### Fire cfg_bgp_all_iac from a Github Commit:

- This is about using the same previous workflow ```cfg_bgp_all``` and attaching a rule to automatically fire this workflow based on a specfic event. This is essentially is the event-driven functionality which is the crux of Stackstorm. It allows to perform workflow automation without the need to manually invoke the st2 corresponding action.
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
- Check 1) if the trigger has been dispatched, 2) if the rule matched and 3) if the corresponding workflow has been fired:

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

### Fire cfg_bgp_all_iac from a generic Webhook:

