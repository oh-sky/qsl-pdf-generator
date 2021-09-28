""" test app.py functions """
import datetime
import os
import pytest
from app import File, get_log_file_list
from app import write_out_html
from app import write_out_pdf
from qso import Qso


def test_get_log_file_list(adif_file_list: tuple, tmpdir):
    """ test get_log_file_list """
    assert set(adif_file_list) == set(get_log_file_list(tmpdir))


@pytest.fixture
def adif_file_list(tmpdir) -> tuple:
    """ fixture generates files and returns file list """
    files = []
    basename_list = ['a.adif', 'b.adi', 'c.adif', 'd.adi']
    for basename in basename_list:
        path = os.path.join(tmpdir, basename)
        files.append(File(
            basename=basename,
            path=path
        ))
        with open(path, 'w', encoding='utf-8') as file:
            file.write(basename)

    yield tuple(files)

    for basename in basename_list:
        os.remove(os.path.join(tmpdir, basename))


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


@pytest.fixture
def html_file_path(tmpdir) -> str:
    """ fixture returns path to html file """
    path = os.path.join(tmpdir, 'unittest_out.html')

    yield os.path.join(path)

    os.remove(path)


def test_write_out_pdf(html_file_path_to_write_out_pdf: str, css_file_path: str, pdf_file_path: str):
    """ test write_out_pdf() """
    write_out_pdf(html_file_path_to_write_out_pdf, css_file_path, pdf_file_path)

    assert os.path.isfile(pdf_file_path)

    with open(pdf_file_path, 'rb') as f:
        pdf = f.read()

    assert pdf.find('Body'.encode('utf-8'))


@pytest.fixture
def html_file_path_to_write_out_pdf(tmpdir) -> str:
    """ fixture creates html file and returns path for it """
    path = os.path.join(tmpdir, 'for_test_write_out_pdf.html')

    with open(path, 'w', encoding='utf-8') as f:
        f.write('<html><head><title>Title</title></head><body>Body</body></html>')

    yield path

    os.remove(path)


@pytest.fixture
def css_file_path(tmpdir) -> str:
    """ fixture creates css file and returns path for it """
    path = os.path.join(tmpdir, 'for_test_write_out_pdf.css')

    with open(path, 'w', encoding='utf-8') as f:
        f.write('body: {{color: #000}}')

    yield path

    os.remove(path)


@pytest.fixture
def pdf_file_path(tmpdir) -> str:
    """ fixture returns path to pdf file """
    path = os.path.join(tmpdir, 'unittest_out.pdf')

    yield os.path.join(path)

    os.remove(path)
