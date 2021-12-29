#Allows the user to record a macro and name it
#Sequence of mouse movements, clicks, keys pressed
#Name: invoked next time via voice commands
import keyboard, mouse
import proj_commands
import threading
#Dictionaries to store command-key (to be executed) and command-description pairs
#Only user-recorded macros are in here. Default commands not included.

#Macro names will be verbally called! Make them as clear as possible!
cmd_exec = {}
#Sample entry: { 'youtube next': [[mouse events], [keyboard events]] }
cmd_desc = {}
#Sample entry: { 'youtube next': 'switch to the next video on Youtube'}

def record_some_macro():
    mouse_events = []
    mouse.hook(mouse_events.append)
    keyboard.start_recording()       #Starting the recording
    keyboard.wait("a")
    mouse.unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()  #Stopping the recording. Returns list of events

def replay_macro(macro_name): #use threading to play BOTH mouse and keyboard events
    try:
        #Keyboard threadings:
        k_thread = threading.Thread(target = lambda :keyboard.play(keyboard_events))
        k_thread.start()

        #Mouse threadings:
        m_thread = threading.Thread(target = lambda :mouse.play(mouse_events))
        m_thread.start()

        #waiting for both threadings to be completed
        k_thread.join() 
        m_thread.join()
        return 0
    except: #the bot will speak the line below
        return("macro not registered, or poorly pronounced")
