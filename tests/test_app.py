""" test app.py functions """
import datetime
import os
import pytest
from app import File, get_log_file_list
from app import write_out_html
from qso import Qso


def test_get_log_file_list(adif_file_list: tuple, tmpdir):
    """ test get_log_file_list """
    assert set(adif_file_list) == set(get_log_file_list(tmpdir))


@pytest.fixture
def adif_file_list(tmpdir) -> tuple:
    """ fixture generates files and returns file list """
    files = []
    for basename in ['a.adif', 'b.adi', 'c.adif', 'd.adi']:
        path = os.path.join(tmpdir, basename)
        files.append(File(
            basename=basename,
            path=path
        ))
        with open(path, 'w', encoding='utf-8') as file:
            file.write(basename)
    yield tuple(files)


def test_write_out_html(qso_log: list, html_file_path: str):
    """ test write_out_html() """
    write_out_html(qso_log, html_file_path)

    assert os.path.isfile(html_file_path)

    with open(html_file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    assert 'A1B2C3' in html


@pytest.fixture
def qso_log() -> list:
    """ fixture returns list of qso """

    yield tuple([Qso(
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
    )])


@ pytest.fixture
def html_file_path(tmpdir) -> str:
    """ fixture returns path to html file """
    path = os.path.join(tmpdir, 'unittest_out.html')

    yield os.path.join(path)

    os.remove(path)
