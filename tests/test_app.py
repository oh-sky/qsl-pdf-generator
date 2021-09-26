""" test app.py functions """
import os
import pytest
from app import File, get_log_file_list


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
