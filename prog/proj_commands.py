#Default actions:   left click, drag, double click
import proj_macro as pm
import keyboard, mouse
import time, webbrowser
import win32gui, win32con

has_stopped = False     #return if user has called 'stop'
win_maxed = False       #return if current window is maximized

def execute_commands(cmd):
    global cmd_exec, has_stopped
    if 'stop' in cmd:
        has_stopped = True
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
    elif cmd.find('scroll') == 0: #scroll up/down until 'stop'
        cmd = cmd.split(" ")
        if cmd[1] == 'up':
            scroll('up')
        else:
            scroll('down')
    elif 'maximize' in cmd: #maximize a window, or 'normalize' it
        maximize()
    elif 'minimize' in cmd: #minimize a window
        minimize()
    elif 'search' in cmd:
        cmd = cmd.split(' ')
        query = cmd[1]
        search(query)
    elif cmd.find('hold') == 0:
        cmd = cmd.split(' ')
        some_key = cmd[1]
        hold(some_key)
    elif cmd.find('combine') == 0:
        cmd = cmd.split(' ')
        key1 = cmd[1]
        key2 = cmd[2]
        combine(key1, key2)
    elif cmd.find('type') == 0:
        speech1 = cmd[5:]
        type_keys(speech1)
    elif cmd.find('wiki') == 0:
        query = cmd[5:]
        ask_wiki(query)
    elif cmd.find('weather') == 0:
        city = cmd[8:]
        weather(city)
    elif cmd.find('say') == 0: #make Tony say stuff
        speech2 = cmd[4:]
        pronounce(speech2)
    else: #no more basic commands
        if cmd in pm.cmd_exec:
            pm.replay_macro(cmd)
        else: #Tony doesnt know this command
            return 1
            
    return 0

def mouse_drag(direction, distance):
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
        mouse.move(0, dist, absolute=False)
    if direction == 'west': #move mouse 'left' some distance
        mouse.move(0, -dist, absolute=False)

def is_maxed():
    return win_maxed

def stop_called(): #help other functions to decide if program is stopped
    return has_stopped

def left_click(repeat=1):
    for i in range(0, repeat):
        mouse.click()
def right_click(repeat=1):
    for i in range(0, repeat):
        mouse.right_click()

def scroll(direction):
    global has_stopped
    has_stopped = True
    if direction == 'down':
        while not stop_called():
            mouse.wheel(delta=-1)
    else:
        while not stop_called():
            mouse.wheel(delta=1)

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

def search(query): #Opens the default browser and search for query on google
    webbrowser.get().open('http://www.google.com')
    time.sleep(2) #sleep time may depend on computer/connection
    keyboard.write(query)
    keyboard.press_and_release('enter')
    return 0

def hold(held_key):
    global has_stopped
    keyboard.press(held_key)
    if stop_called():
        keyboard.release(held_key)

def combine(key1, key2):
    keyboard.press_and_release(key1 +'+'+ key2)

def type_keys(speech):
    keyboard.write(speech)

#Below are actions that would trigger a voiced response
#Get weather condition, temperature, and air pollution level of some city
def weather(city):
    mkey = "b574c25bd6eb7f7802f69cd724e5308a"
    lat = ""
    lon = ""
    with open ("./city.list.json", encoding="utf-8") as f:
        data = json.load(f) #data will be a dict
    for item in data:
        if item["name"].lower() == city.lower():
            #convert those floats to string to append them quicker
            lon = str(item["coord"]["lon"])
            lat = str(item["coord"]["lat"])
            break
    airpol_url = "http://api.openweathermap.org/data/2.5/air_pollution?lat="+lat+"&lon="+lon+"&appid="+mkey
    weather_url = "http://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+mkey+"&units=metric"
    a_response = requests.get(airpol_url)
    w_response = requests.get(weather_url)
    #parse responses
    condition = w_response.json()["weather"][0]["main"].lower()
    temperature = int (w_response.json()["main"]["temp"]) #wrap just in case
    aircode = int (a_response.json()["list"][0]["main"]["aqi"]) #wrap just in case
    airqual = ['very good', 'good', 'alright', 'bad', 'very bad']
    result = ""
    result += "Weather condition of " + city + ": " + condition
    result += ", temperature is " + temperature +" degrees"
    result += ", air quality is " + airqual[aircode]
    pronounce(result)

def ask_wiki(query):
    return 0

def pronounce(speech):
    return 0

def test():
    execute_commands('mouse south 30')
test()