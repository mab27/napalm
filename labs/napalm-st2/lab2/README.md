# Lab2

## Overview:
- Writing custom workflows based on standard actions from the NAPALM pack.
- Goal is to iterate againse the list of device in the inveotry list

## Getters (show commands):

- get_facts:
```
mab@mab-infra:/opt/stackstorm/packs/napalm/actions$ st2 run napalm.get_facts_all 
.............
id: 59fc66727cae22068a51a900
action.ref: napalm.get_facts_all
parameters: None
status: failed
result_task: get_facts_all
result: - result: "Failure caused by error in tasks: get_facts\n\n  get_facts [task_ex_id=6e5630dd-230c-4f7f-a8cc-1d00d17fa20d] -> {result: None, exit_code: 1, stderr: Traceback (most recent call last):\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 259, in <module>\\n    obj.run()\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 155, in run\\n    output = action.run(**self._parameters)\\n  File \"/opt/stackstorm/packs/napalm/actions/get_facts.py\", line 10, in run\\n    with self.get_driver(**std_kwargs) as device:\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_base/base.py\", line 47, in __enter__\\n    self.open()\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_junos/junos.py\", line 107, in open\\n    self.device.open()\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/jnpr/junos/device.py\", line 1267, in open\\n    raise EzErrors.ConnectRefusedError(self)\\njnpr.junos.exception.ConnectRefusedError: ConnectRefusedError(vmx2)\\n, stdout: }\n    [action_ex_id=59e43c3e-bfa9-4a2e-a38b-8bca200bf3fe, idx=0]: {u'stdout': u'', u'result': u'None', u'stderr': u'Traceback (most recent call last):\\\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 259, in <module>\\\\n    obj.run()\\\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 155, in run\\\\n    output = action.run(**self._parameters)\\\\n  File \"/opt/stackstorm/packs/napalm/actions/get_facts.py\", line 10, in run\\\\n    with self.get_driver(**std_kwargs) as device:\\\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_base/base.py\", line 47, in __enter__\\\\n    self.open()\\\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_junos/junos.py\", line 107, in open\\\\n    self.device.open()\\\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/jnpr/junos/device.py\", line 1267, in open\\\\n    raise EzErrors.ConnectRefusedError(self)\\\\njnpr.junos.exception.ConnectRefusedError: ConnectRefusedError(vmx2)\\\\n', u'exit_code': 1}\n"
- {}
- result: "Failure caused by error in tasks: get_facts\n\n  get_facts [task_ex_id=02d7e9c2-f7a0-4079-94f3-de4b15b1707a] -> {result: None, exit_code: 1, stderr: No handlers could be found for logger \"pyeapi.eapilib\"\\nTraceback (most recent call last):\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 259, in <module>\\n    obj.run()\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 155, in run\\n    output = action.run(**self._parameters)\\n  File \"/opt/stackstorm/packs/napalm/actions/get_facts.py\", line 10, in run\\n    with self.get_driver(**std_kwargs) as device:\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_base/base.py\", line 47, in __enter__\\n    self.open()\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_eos/eos.py\", line 118, in open\\n    raise ConnectionException(ce.message)\\nnapalm_base.exceptions.ConnectionException: Socket error during eAPI connection: [Errno 113] No route to host\\n, stdout: }\n    [action_ex_id=b4bcaf96-bcfc-47e4-80a0-3b66d525a8c2, idx=0]: {u'stdout': u'', u'result': u'None', u'stderr': u'No handlers could be found for logger \"pyeapi.eapilib\"\\\\nTraceback (most recent call last):\\\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 259, in <module>\\\\n    obj.run()\\\\n  File \"/opt/stackstorm/st2/local/lib/python2.7/site-packages/st2common/runners/python_action_wrapper.py\", line 155, in run\\\\n    output = action.run(**self._parameters)\\\\n  File \"/opt/stackstorm/packs/napalm/actions/get_facts.py\", line 10, in run\\\\n    with self.get_driver(**std_kwargs) as device:\\\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_base/base.py\", line 47, in __enter__\\\\n    self.open()\\\\n  File \"/opt/stackstorm/virtualenvs/napalm/lib/python2.7/site-packages/napalm_eos/eos.py\", line 118, in open\\\\n    raise ConnectionException(ce.message)\\\\nnapalm_base.exceptions.ConnectionException: Socket error during eAPI connection: [Errno 113] No route to host\\\\n', u'exit_code': 1}\n"
- {}
start_timestamp: 2017-11-03T12:52:02.736584Z
end_timestamp: 2017-11-03T12:52:28.287761Z
+--------------------------+------------------------+---------------+--------------------+-------------------------------+
| id                       | status                 | task          | action             | start_timestamp               |
+--------------------------+------------------------+---------------+--------------------+-------------------------------+
| 59fc66737cae22068a51a903 | succeeded (1s elapsed) | get_inventory | napalm.file_to_obj | Fri, 03 Nov 2017 12:52:03 UTC |
| 59fc66757cae22068a51a908 | failed (6s elapsed)    | get_facts     | napalm.get_facts   | Fri, 03 Nov 2017 12:52:05 UTC |
| 59fc66757cae22068a51a909 | succeeded (6s elapsed) | get_facts     | napalm.get_facts   | Fri, 03 Nov 2017 12:52:05 UTC |
| 59fc66757cae22068a51a90a | failed (6s elapsed)    | get_facts     | napalm.get_facts   | Fri, 03 Nov 2017 12:52:05 UTC |
| 59fc66757cae22068a51a90b | succeeded (2s elapsed) | get_facts     | napalm.get_facts   | Fri, 03 Nov 2017 12:52:05 UTC |
+--------------------------+------------------------+---------------+--------------------+-------------------------------+
mab@mab-infra:/opt/stackstorm/packs/napalm/actions$ 
```

```
```

```
```

```
```

```
```

```
```

## Setters (configuration commands):

```
```

## Validation:

```
```

```
```
