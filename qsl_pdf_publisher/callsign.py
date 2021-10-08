"""
callsign operation class
"""


class Callsign:
    """
    Callsign class
    Set callsign as constructer's parameter
    You can get callsign as is or without '/SOMETHING'
    """


    callsign: str = ''


    def __init__(self, callsign:str) -> None:
        """
        Set callsign string
        """
        self.callsign = callsign


    def get(self) -> str:
        """
        Get callsign as you set
        """
        return self.callsign


    def get_transfer(self) -> str:
        """
        Get callsign for transfer QSL
        """
        return self.callsign.split('/')[0]
