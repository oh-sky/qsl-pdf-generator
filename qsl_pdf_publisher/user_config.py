"""
UserConfig & MyStation Class
"""
import datetime
import os
from pathlib import Path
from typing import NamedTuple
import yaml

CONFIG_FILE_PATH = '/work/input/config.yml'


class MyStation(NamedTuple):
    """
    MyStation Class
    """
    callsign: str
    op_name: str
    rig: str
    ant: dict
    qth: str


class InputSettings(NamedTuple):
    """
    Input Settings
    settings about files put into /input directory
    """
    template_name: str


class OutputSettings(NamedTuple):
    """
    OutputSettings
    settings about output html & pdf
    """
    print_timezone: datetime.timezone
    sort_by_callsign: bool



class UserConfig(NamedTuple):
    """
    UserConfig Class
    """
    my_station: MyStation
    input_settings: InputSettings
    output_settings: OutputSettings


def get_timezone_from_config(timezone_string: str) -> datetime.timezone:
    """
    Get datetime.timezone object from config.
    Allowed input variable range is from '-23' to '+23'.
    Based on utc.
    """
    return datetime.timezone(datetime.timedelta(hours=int(timezone_string)))


def read_user_config_file(config_file_path: Path=CONFIG_FILE_PATH) -> UserConfig:
    """
    Reads config yaml file and returns UserConfig
    If there isn't file, it returns None
    """
    if not os.path.isfile(config_file_path):
        return None

    with open(config_file_path, 'r', encoding='utf-8') as file:
        config: dict = yaml.load(file, Loader=yaml.SafeLoader)
    return UserConfig(
        my_station = MyStation(
            callsign = config['my_station']['callsign'],
            op_name = config['my_station']['op_name'],
            rig = config['my_station']['rig'],
            ant = config['my_station']['ant'],
            qth = config['my_station']['qth'],
        ),
        input_settings = InputSettings(
            template_name = config['input_settings']['template'],
        ),
        output_settings = OutputSettings(
            print_timezone = get_timezone_from_config(config['output_settings']['print_timezone']),
            sort_by_callsign = config['output_settings']['sort_by_callsign']
        ),
    )
