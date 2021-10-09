"""
test log sorting module
"""
import datetime
import pytest
from qsl_pdf_publisher.log_file_utils.sort import sort_by_callsign
from qsl_pdf_publisher.qso import Qso

QSOS = (Qso(
    callsign='CCCCCC',
    transfer_callsign='CCCCCC',
    datetime=datetime.datetime.now(),
    rst_sent='', band='', mode='', comment='', frequency='', my_antenna='',
    my_qth='', my_cq_zone='', my_dxcc='', my_gridsquare='', my_iota='', my_rig='',
),
Qso(
    callsign='CCBCCB',
    transfer_callsign='CCBCCB',
    datetime=datetime.datetime.now(),
    rst_sent='', band='', mode='', comment='', frequency='', my_antenna='',
    my_qth='', my_cq_zone='', my_dxcc='', my_gridsquare='', my_iota='', my_rig='',
),
Qso(
    callsign='DDDDDD',
    transfer_callsign='DDDDDD',
    datetime=datetime.datetime.now(),
    rst_sent='', band='', mode='', comment='', frequency='', my_antenna='',
    my_qth='', my_cq_zone='', my_dxcc='', my_gridsquare='', my_iota='', my_rig='',
),
Qso(
    callsign='ABCDEF',
    transfer_callsign='ABCDEF',
    datetime=datetime.datetime.now(),
    rst_sent='', band='', mode='', comment='', frequency='', my_antenna='',
    my_qth='', my_cq_zone='', my_dxcc='', my_gridsquare='', my_iota='', my_rig='',
))

def test_sort_by_callsign():
    sorted_qsos = sort_by_callsign(QSOS)
    assert len(sorted_qsos) == len(QSOS)
    for i in range(len(sorted_qsos)):
        if (i + 1) >= len(sorted_qsos):
            break
        assert sorted_qsos[i].transfer_callsign <= sorted_qsos[i+1].transfer_callsign
