import os
import configparser


def get_config(section=None):
    """
    Get the config settings from the config.ini file
    
    :param section: The section of the config file to read.
    :return: A dictionary of the configuration settings.
    """

    Config = configparser.ConfigParser()
    Config.read('data/config.ini')

    if not section:
        try:
            section = 'DEFAULT'
        except:
            raise Exception('Config file does not contain DEFAULT. Please check the config and try again')

    config = Config[section]
    return config