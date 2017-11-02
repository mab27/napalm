def change_configuration(device, filepath):
	device.open()
	device.load_merge_candidate(filename=filepath)
	print(device.compare_config())
	device.commit_config()