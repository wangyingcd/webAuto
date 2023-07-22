from Common.file_config import FileConfig
from Common.logger import Log
import json

global_config_keys = ['VISIT_RESULT_POSITION', 'MAX_SWIPE_TIMES', 'INPUT_IMAGE_NAME', 'INPUT_IMAGE_KEYWORDS']
log = Log()


class TestConfig:
    def __init__(self):
        self.file_name = 'config.json'
        self.file_full_path = FileConfig().get_path(type="testdata") + '/' + self.file_name
        self.test_config_dic = {}

        with open(self.file_full_path) as json_file:
            data = json.load(json_file)
            json_string = json.dumps(data)
            self.test_config_dic = json.loads(json_string)

        self.check_test_config_exist()
        self.check_visit_result_position_config()
        self.check_max_swipe_times_config()

    def check_test_config_exist(self):
        for k in global_config_keys:
            if k not in self.test_config_dic.keys():
                message = "Error: The config value {} doesn't exist".format(k)
                log.error(message)
                raise Exception()

    def check_visit_result_position_config(self):
        value = self.test_config_dic[global_config_keys[0]]
        if value is not None and type(value) is int and value > 0:
            return value
        else:
            message = "Error: the config VISIT_RESULT_POSITION doesn't exist or invalid"
            log.error(message)
            raise Exception(message)

    def check_max_swipe_times_config(self):
        value = self.test_config_dic[global_config_keys[1]]
        if value is not None and type(value) is int and value > 0:
            return value
        else:
            message = "Error: the config MAX_SWIPE_TIMES doesn't exist or invalid"
            log.error(message)
            raise Exception(message)
