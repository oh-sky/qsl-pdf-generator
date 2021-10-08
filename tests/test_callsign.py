"""
test Callsign class
"""
import pytest
from qsl_pdf_publisher.callsign import Callsign

def test_get():
    """
    test get()
    """
    call = 'JJ1AYZ/1'
    callsign = Callsign(call)
    assert callsign.get() == call

def test_get_transfer():
    """
    test get_transfer()
    """
    call = 'JJ1AYZ/1'
    callsign = Callsign(call)
    assert callsign.get_transfer() == 'JJ1AYZ'
