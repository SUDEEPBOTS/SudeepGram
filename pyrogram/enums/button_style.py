from enum import auto
from .auto_name import AutoName

class ButtonStyle(AutoName):
    """Button style/color options for inline keyboard buttons."""
    
    PRIMARY = auto()   # Blue
    DANGER = auto()    # Red  
    SUCCESS = auto()   # Green
