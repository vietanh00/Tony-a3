#Launch the GUI and necessary codes
from prog import proj_parsevoice as pv
import subprocess

#functions for the gui buttons
def in_voice_mode():
    tony()
def in_text_mode():
    pass
def in_recording_macro():
    pass
def get_all_description():
    result = ""
    for cmd, macros in cmd_exec:
        result += cmd + '\t \t' + cmd_desc[cmd]
    return result
