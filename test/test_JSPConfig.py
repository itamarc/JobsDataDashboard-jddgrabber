from recursive_diff import recursive_eq
import jspgrabber.JSPConfigFileCreator as fc
import jspgrabber.JSPConfig as conf
import os

def test_create_load_config():
    config_file = r'config-test.yaml'
    default_config = fc.get_default_config()
    fc.create_config_file(config_file)
    config = conf.load_config(config_file)
    recursive_eq(default_config, config)
    os.remove(config_file)

if __name__ == '__main__':
    test_create_load_config()
