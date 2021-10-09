"""
module to sort log
"""
from typing import Tuple
from qsl_pdf_publisher.qso import Qso


def sort_by_callsign(qso_log: Tuple[Qso, ...]) -> Tuple[Qso, ...]:
    """
    sort QSO List by transfer callsign
    """
    return tuple(sorted(qso_log, key=lambda qso:qso.transfer_callsign))
