""" QSO information """
from typing import NamedTuple
import datetime


class Qso(NamedTuple):
    """ QSO information NamedTuple """
    callsign: str
    datetime: datetime.datetime
    rst_sent: str
    band: str
    mode: str
    comment: str
    frequency: str
    my_antenna: str
    my_qth: str
    my_cq_zone: str
    my_dxcc: str
    my_gridsquare: str
    my_iota: str
    my_rig: str
