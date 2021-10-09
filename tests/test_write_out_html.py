"""
test write_out_html()
"""
import datetime
import os
import typing
import pytest
from qsl_pdf_publisher.app import write_out_html
from qsl_pdf_publisher.qso import Qso


def test_write_out_html(qso_log: typing.Tuple[Qso, ...], html_file_path: str):
    """
    test write_out_html()
    """
    write_out_html(qso_log, html_file_path)

    assert os.path.isfile(html_file_path)

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    assert 'A1B2C3' in html


@pytest.fixture
def qso_log() -> typing.Tuple[Qso, ...]:
    """
    fixture returns list of qso
    """

    yield tuple([Qso(
        callsign='A1B2C3',
        transfer_callsign='A1B2C3',
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
    )])


@pytest.fixture
def html_file_path(tmpdir) -> str:
    """
    fixture returns path to html file
    """
    path = os.path.join(tmpdir, 'unittest_out.html')

    yield os.path.join(path)

    os.remove(path)

