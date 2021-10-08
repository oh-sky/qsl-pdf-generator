"""
test user_config module
"""
import pytest
import os
import datetime
from pathlib import Path
from typing import Tuple
import yaml
from qsl_pdf_publisher.user_config import read_user_config_file


def test_user_config(config_file_and_dict: Tuple[Path, dict]) -> None:
    """
    test user_config module
    """
    config_file_path, config_dict = config_file_and_dict
    user_config = read_user_config_file(config_file_path)

    assert user_config.my_station.callsign == config_dict['my_station']['callsign']
    assert user_config.my_station.op_name == config_dict['my_station']['op_name']
    assert user_config.my_station.rig == config_dict['my_station']['rig']
    assert user_config.my_station.ant == config_dict['my_station']['ant']
    assert user_config.my_station.qth == config_dict['my_station']['qth']
    assert user_config.input_settings.template_name == config_dict['input_settings']['template']
    assert user_config.output_settings.print_timezone == datetime.timezone(datetime.timedelta(hours=int(config_dict['output_settings']['print_timezone'])))
    assert user_config.output_settings.sort_by_callsign == config_dict['output_settings']['sort_by_callsign']


@pytest.fixture
def config_file_and_dict(tmpdir: Path) -> Tuple[Path, dict]:
    """
    fixture create config file
    """
    config_file_path = os.path.join(tmpdir, 'config.yml')
    config = {
        'my_station': {
            'callsign': 'JJ1AYZ/1',
            'op_name': '那須 与一',
            'rig': 'TS-940',
            'ant': {
                '2200m': 'MY ANT NAME FOR 135kHz',
                '600m': 'MY ANT NAME FOR 475kHz',
                '160m': 'MY ANT NAME FOR 1.9MHz',
                '80m': 'MY ANT NAME FOR 3.5MHz',
                '40m': 'MY ANT NAME FOR 7MHz',
                '30m': 'MY ANT NAME FOR 10MHz',
                '20m': 'MY ANT NAME FOR 14MHz',
                '17m': 'MY ANT NAME FOR 18MHz',
                '15m': 'MY ANT NAME FOR 21MHz',
                '12m': 'MY ANT NAME FOR 24MHz',
                '10m': 'MY ANT NAME FOR 28MHz',
                '6m': 'MY ANT NAME FOR 50MHz',
                '2m': 'MY ANT NAME FOR 144MHz',
                '70cm': 'MY ANT NAME FOR 430MHz',
                '23cm': 'MY ANT NAME FOR 1200MHz',
                '12cm': 'MY ANT NAME FOR 2400MHz',
                '5cm': 'MY ANT NAME FOR 5.6GHz',
                '3cm': 'MY ANT NAME FOR 10GHz',
            },
            'qth': '東京都千代田区1-1-1'
        },
        'input_settings': {
            'template': 'index.html',
        },
        'output_settings': {
            'print_timezone': '+9',
            'sort_by_callsign': True,
        },
    }

    with open(config_file_path, 'w', encoding='utf-8') as file:
        yaml.dump(config, file)

    yield tuple([config_file_path, config])

    os.remove(config_file_path)
