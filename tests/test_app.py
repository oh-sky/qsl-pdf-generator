""" test app.py functions """
import os
import typing
import pytest
from qsl_pdf_publisher.log_file_utils.log_file import LogFile
from qsl_pdf_publisher.log_file_utils.get_log_file_list import get_log_file_list
from qsl_pdf_publisher.app import get_log_file_list, write_out_pdf


def test_get_log_file_list(adif_file_list: typing.Tuple[LogFile, ...], tmpdir) -> None:
    """ test get_log_file_list """
    assert set(adif_file_list) == set(get_log_file_list(tmpdir))


@pytest.fixture
def adif_file_list(tmpdir) -> typing.Tuple[LogFile, ...]:
    """ fixture generates files and returns file list """
    files = []
    basename_list = ['a.adif', 'b.adi', 'c.adif', 'd.adi']
    for basename in basename_list:
        path = os.path.join(tmpdir, basename)
        files.append(LogFile(
            basename=basename,
            path=path
        ))
        with open(path, 'w', encoding='utf-8') as file:
            file.write(basename)

    yield tuple(files)

    for basename in basename_list:
        os.remove(os.path.join(tmpdir, basename))


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
