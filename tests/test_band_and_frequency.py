"""
test band_and_frequency module
"""
from qsl_pdf_publisher.band_and_frequency import get_band_by_frequency


def test_get_band_by_frequency():
    """
    test get_band_by_frequency()
    """
    assert get_band_by_frequency('135kHz') == '2200m'
    assert get_band_by_frequency('475kHz') == '600m'
    assert get_band_by_frequency('1.9MHz') == '160m'
    assert get_band_by_frequency('3.5MHz') == '80m'
    assert get_band_by_frequency('7MHz') == '40m'
    assert get_band_by_frequency('10MHz') == '30m'
    assert get_band_by_frequency('14MHz') == '20m'
    assert get_band_by_frequency('18MHz') == '17m'
    assert get_band_by_frequency('21MHz') == '15m'
    assert get_band_by_frequency('24MHz') == '12m'
    assert get_band_by_frequency('28MHz') == '10m'
    assert get_band_by_frequency('50MHz') == '6m'
    assert get_band_by_frequency('144MHz') == '2m'
    assert get_band_by_frequency('430MHz') == '70cm'
    assert get_band_by_frequency('1200MHz') == '23cm'
    assert get_band_by_frequency('2400MHz') == '12cm'
    assert get_band_by_frequency('5.6GHz') == '5cm'
    assert get_band_by_frequency('10GHz') == '3cm'
