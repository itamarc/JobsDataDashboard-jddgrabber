import unittest
from recursive_diff import recursive_eq
import jddgrabber.JDDConfigFileCreator as fc
import jddgrabber.JDDConfig as conf


class test_JDDConfig(unittest.TestCase):
    def test_create_load_config(self):
        config_file = r'config-test.yaml'
        default_config = fc.get_default_config()
        fc.create_config_file(config_file)
        config = conf.load_config(config_file)
        recursive_eq(default_config, config)
        fc.remove_config_file(config_file)


# if __name__ == '__main__':
#     test_create_load_config()
