"""
test write_out_html()
"""
import datetime
import os
from typing import Tuple
import pytest
from qsl_pdf_publisher.app import write_out_html
from qsl_pdf_publisher.qso import Qso
from qsl_pdf_publisher.user_config import InputSettings, MyStation, OutputSettings, UserConfig


def test_write_out_html_without_user_config(qso_log: Tuple[Qso, ...], html_file_path: str):
    """
    test write_out_html() without user_config attribute
    """
    write_out_html(qso_log, html_file_path)

    assert os.path.isfile(html_file_path)

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    assert 'A1B2C3' in html


def test_write_out_html_with_user_config(qso_log: Tuple[Qso, ...], html_file_path: str, user_config: UserConfig):
    """
    test write_out_html() with user_config
    """
    write_out_html(qso_log, html_file_path, user_config)

    assert os.path.isfile(html_file_path)

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    assert 'JTAIRA/3' in html
    assert '鍬形兜アンテナ' in html
    assert '須磨区' in html
    assert 'UTC+09:00' in html


@pytest.fixture
def qso_log() -> Tuple[Qso, ...]:
    """
    fixture returns list of qso
    """

    yield tuple([Qso(
        callsign='A1B2C3',
        transfer_callsign='A1B2C3',
        datetime=datetime.datetime(2001, 12, 1, 23, 43),
        rst_sent='599',
        band='70cm',
        mode='CW',
        comment='FB QSO TNX',
        frequency='430',
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


@pytest.fixture
def user_config() -> UserConfig:
    """
    fixture returns Userconfig object
    """

    yield UserConfig(
        my_station=MyStation(
            callsign='JTAIRA/3',
            op_name='Atsumori Taira',
            rig='TR-1184',
            ant={
                '70cm':'鍬形兜アンテナ',
            },
            qth='神戸市須磨区 乗馬中'
        ),
        input_settings=InputSettings(
            template_name='index.html',
        ),
        output_settings=OutputSettings(
            print_timezone=datetime.timezone(datetime.timedelta(hours=int('+9'))),
            sort_by_callsign=True,
        ),
    )
