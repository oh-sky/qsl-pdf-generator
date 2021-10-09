"""
parse_qso_log module
"""
import sys
import typing
from qsl_pdf_publisher.qso import Qso
from qsl_pdf_publisher.log_file_utils.adif_log_parse import adif_log_parse


def parse_qso_log(log_file_path: str) -> typing.Tuple[Qso, ...]:
    """
    parse qso log from log file
    """
    print('  Parsing log ...', file=sys.stderr)
    return adif_log_parse(filename=log_file_path)
