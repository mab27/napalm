import yaml
from st2actions.runners.pythonrunner import Action


class fileToObj(Action):
    def run(self, file_location):

        with open(file_location) as data:
            data_loaded = yaml.safe_load(data)

        result = data_loaded
        return result

