"""
UserConfig & MyStation Class
"""
import yaml

CONFIG_FILE_PATH = '/work/input/config.yml'

frequency_band_map: dict = {
    '135kHz' : '2200m',
    '475kHz' : '600m',
    '1.9MHz' : '160m',
    '3.5MHz' : '80m',
    '7MHz' : '40m',
    '10MHz' : '30m',
    '14MHz' : '20m',
    '18MHz' : '17m',
    '21MHz' : '15m',
    '24MHz' : '12m',
    '28MHz' : '10m',
    '50MHz' : '6m',
    '144MHz' : '2m',
    '430MHz' : '70cm',
    '1200MHz' : '23cm',
    '2400MHz' : '12cm',
    '5.6GHz' : '5cm',
    '10GHz' : '3cm',
}


class MyStation:
    """
    MyStation Class
    """
    callsign: str = None
    op_name: str = None
    rig: str = None
    ant: dict = {}


    def __init__(self, station_settings: dict) -> None:
        self.callsign = station_settings['callsign']
        self.op_name = station_settings['op_name']
        self.rig = station_settings['rig']
        self.ant = station_settings['ant']


    def get_ant_by_band(self, band: str) -> str:
        return self.ant[band]


    def get_ant_by_frequency(self, frequency: str) -> str:
        return self.ant[frequency_band_map[frequency]]


class UserConfig:
    """
    UserConfig Class
    """
    mystation: MyStation = None
    template: str = None
    timezone: str = None
    qth: str = None
    sort_by_callsign: bool = None


    def __init__(self) -> None:
        """
        constructor
        Set properties from input/config.yml
        """
        with open(CONFIG_FILE_PATH, 'r') as yml:
            config = yaml.load(yml)
        self.mystation = MyStation(config['mystation'])
        self.template = config['template']
        self.timezone = config['timezone']
        self.qth = config['qth']
        self.sort_by_callsign = config['sort_by_callsign']
