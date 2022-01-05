#Default actions:   left click, drag, double click
import proj_macro as pm
import win32com.client
import subprocess, time, webbrowser, json
#try:
import requests
import keyboard, mouse
import win32gui, win32con
"""except:
    subprocess.run(["pip", "install", "requests"])
    subprocess.run(["pip", "install", "keyboard"])
    subprocess.run(["pip", "install", "mouse"])
    subprocess.run(["pip", "install", "pywin32"])
    time.sleep(10)
    import requests
    import keyboard, mouse
    import win32gui, win32con"""



has_stopped = False     #return if user has called 'stop'
win_maxed = False       #return if current window is maximized

def execute_commands(cmd):
    global has_stopped
    if 'stop' in cmd:
        stop()
    #try:
        #'find' is better than 'index' since it doesnt raise exceptions
    if cmd.find('drag') == 0: #sample: drag north 300
        cmd = cmd.split(" ") #cmd is now a list
        direction = cmd[1]
        distance = cmd[2]
        mouse_drag(direction, distance)
    elif cmd.find('mouse') == 0: #sample: mouse east 200
        cmd = cmd.split(" ") #cmd is now a list
        direction = cmd[1]
        distance = cmd[2]
        mouse_dir(direction, distance)
    elif cmd.find('left-click') == 0: #'left click' or 'left click 4' (4 times)
        cmd= cmd.split(" ")
        if len(cmd) > 2:
            repeat = cmd[2]
        else:
            repeat = 1
        left_click(repeat)
    elif cmd.find('right-click') == 0: #niche case of repeated right click
        cmd= cmd.split(" ")
        if len(cmd) > 2:
            repeat = cmd[2]
        else:
            repeat = 1
        left_click(repeat)
    elif cmd.find('scroll') == 0: #'scroll up/down 4' (4 times)
        cmd = cmd.split(" ")
        repeat = cmd[2]
        if cmd[1] == 'up':
            scroll('up', repeat)
        else:
            scroll('down', repeat)
    elif 'maximize' in cmd: #maximize a window, or 'normalize' it
        maximize()
    elif 'minimize' in cmd: #minimize a window
        minimize()
    elif 'search' in cmd:
        cmd = cmd.split(' ')
        query = cmd[1]
        search(query)
    elif cmd.find('press') == 0:
        cmd = cmd.split(' ')
        some_key = cmd[1]
        press(some_key)
    elif cmd.find('combine') == 0:
        cmd = cmd.split(' ')
        length = len(cmd) 
        key1 = cmd[1]
        if key1 == 'alt-tab': #only alt-tab has this issue
            key1 = 'alt'
            key2 = 'tab'
        else:
            key2 = cmd[2]
            if length > 3:
                key3 = cmd[3]
                combine(key1, key2, key3)
            else:
                key2 = cmd[2]
                combine(key1, key2)
    elif cmd.find('type') == 0:
        speech1 = cmd[5:]
        type_keys(speech1)
    elif cmd.find('web') == 0: #'web youtube.com' -> launch browser, no www please
        cmd = cmd.split(" ")
        site = cmd[1]
        web(site)
    elif cmd.find('volume') == 0: #change SYSTEM volume. 'volume up/down/mute'
        cmd = cmd.split(' ')
        direction=cmd[1]
        volume(direction)
    else: #no more basic commands. Search for stuff in the macros Pickle file
        err_code = pm.replay_macro(cmd)
        if err_code == 1:
            print("macro not registered, or poorly pronounced")
    #except:
    #    pass

    return 0

#the bot will recognize twenty-two as 22, but not three as 3
#even worse, two/2/to is all jumbled up
def voice_int(num_voice):
    voices  = ['one', 'two', 'to', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero']
    ints    = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in range (0, len(voices)):
        if num_voice == voices[i]:
            return ints[i]

def is_maxed():
    global win_maxed
    return win_maxed
def stop():
    global has_stopped
    has_stopped = True
def stop_called(): #help other functions to decide if program is stopped
    global has_stopped
    return (has_stopped == True)

def mouse_drag(direction, distance):
    global has_stopped
    has_stopped = False
    dist = int(distance)
    mouse.press()
    mouse_dir(direction, distance)
    mouse.release()
    return 0

def mouse_dir(direction, distance):
    dist = int(distance)
    if direction == 'north': #move mouse 'up' some distance
        mouse.move(0, -dist, absolute=False)
    if direction == 'south': #move mouse 'down' some distance
        mouse.move(0, dist, absolute=False)
    if direction == 'east': #move mouse 'right' some distance
        mouse.move(dist, 0, absolute=False)
    if direction == 'west': #move mouse 'left' some distance
        mouse.move(-dist, 0, absolute=False)

def left_click(repeat=1):
    for i in range(0, repeat):
        mouse.click()
def right_click(repeat=1):
    for i in range(0, repeat):
        mouse.right_click()

def scroll(direction, repeat):
    global has_stopped
    has_stopped = False
    if direction == 'down':
        for i in range(0, repeat):
            mouse.wheel(delta=-1)
            time.sleep(0.8) #sleep some time for the user to check
    else:
        for i in range(0, repeat):
            mouse.wheel(delta=1)
            time.sleep(0.8)

def maximize():
    global win_maxed
    #maximize the CURRENT active window (e.g. in the foreground)
    #if it's already maxed, show the normal size instead
    if not is_maxed():
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
        win_maxed = True
    else:
        hwnd = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        win_maxed = False
    return 0

def minimize():
    #maximize the CURRENT active window (e.g. in the foreground)
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    return 0

def press(some_key):
    keyboard.press_and_release(some_key)

def combine(key1, key2, key3=''):
    if key3 == '':
        keyboard.press_and_release(key1 +'+'+ key2)
    else: 
        keyboard.press_and_release(key1 +'+'+ key2+'+'+key3)

#def combine3()

def type_keys(speech):
    keyboard.write(speech)

#web stuff
def web(site):
    webbrowser.get().open('http://' + site)
    return 0

def search(query): #Opens the default browser and search for query on google
    webbrowser.get().open('http://www.google.com')
    time.sleep(3) #sleep time may depend on computer/connection
    keyboard.write(query)
    keyboard.press_and_release('enter')
    return 0

def volume(direction): #up, down, mute
    shell = win32com.client.Dispatch("WScript.Shell")
    if direction == 'up':
        shell.SendKeys(chr(175), 0)
    elif direction == 'down':
        shell.SendKeys(chr(174), 0)
    elif direction =='mute': #mute
        shell.SendKeys(chr(173), 0)
    return 0

def test():
    execute_commands('volume down')

#test()