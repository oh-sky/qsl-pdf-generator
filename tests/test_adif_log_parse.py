""" test adif_log_parse() """
import datetime
import os
import pytest
from adif_log_parse import adif_log_parse
from qso import Qso

QSOS = (Qso(
    callsign='A1B2C3',
    datetime=datetime.datetime(2001, 12, 1, 23, 43),
    rst_sent='599',
    band='40m',
    mode='CW',
    comment='FB QSO TNX',
    frequency='7',
    my_antenna='Super Ultra Great Wonderful DP',
    my_qth='Top of Mt. Fuji (JCC#1807)',
    my_cq_zone='25',
    my_dxcc='339',
    my_gridsquare='PM95',
    my_iota='',
    my_rig='FTDX101MP',
), Qso(
    callsign='D4E5F6',
    datetime=datetime.datetime(2006, 9, 6, 17, 27),
    rst_sent='59',
    band='6m',
    mode='FM',
    comment='1st QSO THX',
    frequency='50',
    my_antenna='Super Ultra Great Wonderful HB9CV',
    my_qth='Chiyoda, Tokyo (JCC#100101)',
    my_cq_zone='25',
    my_dxcc='339',
    my_gridsquare='PM95',
    my_iota='',
    my_rig='IC-7851',
))


def test_adif_log_parse(filename: str):
    """ test adif_log_parse("""
    qsos = adif_log_parse(filename)
    assert qsos == QSOS


@pytest.fixture
def filename(tmpdir: str) -> str:
    """ fixture creating adif file """
    log_file_path = tmpdir.join('test_adif_log_file.adif')
    with open(log_file_path, 'w', encoding='utf-8') as file:
        file.write('<adif_ver:5>3.1.0<eoh>\n')
        for qso in QSOS:
            v = qso.callsign
            l = len(v)
            file.write(f'<CALL:{l}>{v}')
            v = qso.datetime.strftime('%Y%m%d')
            l = len(v)
            file.write(f'<QSO_DATE:{l}>{v}')
            v = qso.datetime.strftime('%H%M')
            l = len(v)
            file.write(f'<TIME_ON:{l}>{v}')
            v = qso.rst_sent
            l = len(v)
            file.write(f'<RST_SENT:{l}>{v}')
            v = qso.band
            l = len(v)
            file.write(f'<BAND:{l}>{v}')
            v = qso.mode
            l = len(v)
            file.write(f'<MODE:{l}>{v}')
            v = qso.comment
            l = len(v)
            file.write(f'<COMMENT:{l}>{v}')
            v = qso.frequency
            l = len(v)
            file.write(f'<FREQ:{l}>{v}')
            v = qso.my_antenna
            l = len(v)
            file.write(f'<MY_ANTENNA:{l}>{v}')
            v = qso.my_qth
            l = len(v)
            file.write(f'<MY_QTH:{l}>{v}')
            v = qso.my_cq_zone
            l = len(v)
            file.write(f'<MY_CQ_ZONE:{l}>{v}')
            v = qso.my_dxcc
            l = len(v)
            file.write(f'<MY_DXCC:{l}>{v}')
            v = qso.my_gridsquare
            l = len(v)
            file.write(f'<MY_GRIDSQUARE:{l}>{v}')
            v = qso.my_iota
            l = len(v)
            file.write(f'<MY_IOTA:{l}>{v}')
            v = qso.my_rig
            l = len(v)
            file.write(f'<MY_RIG:{l}>{v}<EOR>\n')

    yield log_file_path

    os.remove(log_file_path)
