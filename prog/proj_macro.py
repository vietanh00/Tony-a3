#Allows the user to record a macro and name it
#Sequence of mouse movements, clicks, keys pressed
#Name: invoked next time via voice commands
import keyboard, mouse
import dill     #dill over pickle since it is preserved after shutdowns and stuff
import threading, time
#Dictionaries to store command-key (to be executed) and command-description pairs
#Only user-recorded macros are in here. Default commands not included.

#Macro names will be verbally called! Make them as clear as possible!
#Sample entry: { 'youtube next': [[mouse events], [keyboard events]] }
filename = 'macros_exec.pkl'
def record_some_macro(name):
    global filename, cmd_exec
    time.sleep(0.5)
    print("You can record your macro now!")
    mouse_events = []
    mouse.hook(mouse_events.append)
    keyboard.start_recording()       #Starting the recording
    keyboard.wait("`")
    mouse.unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()  #Stopping the recording. Returns list of events
    #Save (name, mouse, keyboard) to a file
    macro_tuple = (name, mouse_events, keyboard_events)
    f = open(filename, 'wb')
    dill.dump(macro_tuple, f)
    f.close()
    return macro_tuple

def replay_macro(macro_name): #use threading to play BOTH mouse and keyboard events
    global filename
    print("Trying to do what you did...")
    current_name = ""
    k_events = []
    m_events = []
    while True:
        try:
            f = open(filename, 'rb')
            macro_obj = dill.load(f)
            if macro_obj[0] == macro_name:
                current_name = macro_name
                m_events = macro_obj[1]
                k_events = macro_obj[2]
                break
        except EOFError:
            break
    if len(k_events) == 0:
        return("macro not registered, or poorly pronounced")

    #Keyboard threadings:
    k_thread = threading.Thread(target = lambda :keyboard.play(k_events))
    k_thread.start()

    #Mouse threadings:
    m_thread = threading.Thread(target = lambda :mouse.play(m_events))
    m_thread.start()

    #waiting for both threadings to be completed
    k_thread.join() 
    m_thread.join()
    return 0
        

def testmac():
    name = 'haha'
    print("Send ` to stop recording!")
    my_macro = record_some_macro(name)
    replay_macro(name)
    
testmac()