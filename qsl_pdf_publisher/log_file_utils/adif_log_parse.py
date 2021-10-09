"""
ADIF log parser
"""
import datetime
import typing
import adif_io
from qsl_pdf_publisher.qso import Qso
from qsl_pdf_publisher.callsign import Callsign


def adif_log_parse(filename: str) -> typing.Tuple[Qso, ...]:
    """ parse ADIF log """
    qso_list = []
    items = adif_io.read_from_file(filename)[0]
    for item in items:
        callsign = Callsign(item.get('CALL'))
        qso_list.append(Qso(
            callsign=callsign.get(),
            transfer_callsign=callsign.get_transfer(),
            datetime=datetime.datetime(
                int(item.get('QSO_DATE')[:4]),
                int(item.get('QSO_DATE')[4:6]),
                int(item.get('QSO_DATE')[6:8]),
                int(item.get('TIME_ON')[:2]),
                int(item.get('TIME_ON')[2:4])),
            rst_sent=item.get('RST_SENT'),
            band=item.get('BAND'),
            mode=item.get('MODE'),
            comment=item.get('COMMENT') or '',
            frequency=item.get('FREQ') or '',
            my_antenna=item.get('MY_ANTENNA') or '',
            my_qth=item.get('MY_QTH') or '',
            my_cq_zone=item.get('MY_CQ_ZONE') or '',
            my_dxcc=item.get('MY_DXCC') or '',
            my_gridsquare=item.get('MY_GRIDSQUARE') or '',
            my_iota=item.get('MY_IOTA') or '',
            my_rig=item.get('MY_RIG') or ''
        ))
    return tuple(qso_list)
