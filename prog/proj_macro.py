#Allows the user to record a macro and name it
#Sequence of mouse movements, clicks, keys pressed
#Name: invoked next time via voice commands
import keyboard, mouse, pathlib
import dill     #dill over pickle since it is preserved after shutdowns and stuff
import threading, time
#Dictionaries to store command-key (to be executed) and command-description pairs
#Only user-recorded macros are in here. Default commands not included.

#Macro names can be verbally called! Make them as clear as possible! No dashes and stuff.
#Sample entry: { 'youtube next': [[mouse events], [keyboard events]] }
filename = str(pathlib.Path().resolve()) +'\macros_exec.pickle'
all_macros = []
def record_some_macro(name):
    global filename
    time.sleep(0.5)
    #print("You can record your macro now! Press ` to stop recording!")
    mouse_events = []
    mouse.hook(mouse_events.append)
    keyboard.start_recording()       #Starting the recording
    keyboard.wait("`")
    mouse.unhook(mouse_events.append)
    keyboard_events = keyboard.stop_recording()  #Stopping the recording. Returns list of events
    #Save (name, mouse, keyboard) to a file
    macro_tuple = (name, mouse_events, keyboard_events)
    f= open(filename, 'ab+')
    dill.dump(macro_tuple, f)
    f.close()
    return macro_tuple

def replay_macro(macro_name): #use threading to play BOTH mouse and keyboard events
    global filename, all_macros
    current_name = ""
    k_events = []
    m_events = []
    f =  open(filename, 'rb')
    while True:
        try:
            macro_obj = dill.load(f)
            all_macros.append(macro_obj)
            if macro_obj[0] == macro_name:
                current_name = macro_name
                #print(macro_obj[0])
                m_events = macro_obj[1]
                k_events = macro_obj[2]
                break
        except EOFError:
            break
    f.close()
    if len(k_events) == 0:
        return 1

    #print("Trying to do what you did...")
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
    name = 'hehe'
    my_macro = record_some_macro(name)
    replay_macro(name)
#testmac()