"""
relations between band and frequency
"""


def get_band_by_frequency(frequency: str) -> str:
    """
    Get antenna name by frequency
    """
    frequency_band_map: dict = {
        '135kHz' : '2200m',
        '475kHz' : '600m',
        '1.9MHz' : '160m',
        '3.5MHz' : '80m',
        '7MHz' : '40m',
        '10MHz' : '30m',
        '14MHz' : '20m',
        '18MHz' : '17m',
        '21MHz' : '15m',
        '24MHz' : '12m',
        '28MHz' : '10m',
        '50MHz' : '6m',
        '144MHz' : '2m',
        '430MHz' : '70cm',
        '1200MHz' : '23cm',
        '2400MHz' : '12cm',
        '5.6GHz' : '5cm',
        '10GHz' : '3cm',
    }

    return frequency_band_map[frequency]
