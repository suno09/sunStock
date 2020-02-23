import configparser


def load_config(file_name):
    """
    Load config information
    :return: dictionary object
    """

    config = configparser.ConfigParser()
    config.read(file_name)

    return config
