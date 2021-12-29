#Launch the GUI and necessary codes
import proj_parsevoice as tony
import proj_commands as pc
import proj_macro as pm
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
