#Small GUI with widgets
#This is to allow user to manually close program or type commands
#It is also reassuring to see the program on screen
import subprocess, dill, pathlib
#try:
from tkinter import *
from tkinter import ttk
"""except:
    subprocess.run(["pip", "install", "tkinter"])
    time.sleep(3)
    from tkinter import *
    from tkinter import ttk"""
from style import *
import proj_macro as pm
import proj_commands as pc


root = Tk()
cmd_text_entries = StringVar()
new_macro_name = StringVar()
#Create a small window for GUI
#Calling Tk() also allows collecting screen resolution
elementz = []
def screen_w(master):
    return master.winfo_screenwidth()
def screen_h(master):
    return master.winfo_screenheight()
def destroy_all():
    global elementz
    if len(elementz) > 0:
        for b in elementz:
            b.destroy()
def track_btn(some_button):
    global elementz
    while some_button not in elementz:
        elementz.append(some_button)
def clear_macros():
    filename = pm.filename
    empty_list = [1]
    empty_list.clear()
    with open(filename, 'wb') as f:
        dill.dump(empty_list, f)
def gui_run(string_of_cmd): #execute a comma-separated string of cmd
    list_of_cmd = string_of_cmd.split(',')
    for i in range(0, len(list_of_cmd)):
        pc.execute_commands(list_of_cmd[i].strip())
    return 0
def text_mode(master):
    global elementz, cmd_text_entries #either a 'list' (a string, really) of commands, or a macro, or a mix
    destroy_all()
    text_desc  = Label(master, text="Type your command(s) in the box below, separated by commas.", 
        **main_app_text)
    text_desc.place(x=20, y=50)
    text_box   = Entry(master, textvariable=cmd_text_entries)
    text_box.place(x=20, y=70, width=300)
    x_text_cmd = Button(master, text="Run", bg="#ffffff", command=lambda:gui_run(str(cmd_text_entries.get())))
    x_text_cmd.place(x=20, y=100)
    track_btn(text_desc)
    track_btn(text_box)
    track_btn(x_text_cmd)
def record_mode(master):
    global elementz, new_macro_name
    destroy_all()
    macro_des       = Label(master, text="Click below to start recording a new macro, and press ` to stop.")
    new_macro_label = Label(master, text="Your macro name:", **main_app_text)
    new_macro_label.place(x=20, y=40)
    new_macro_box   = Entry(master, textvariable=new_macro_name)
    new_macro_box.place(x=20, y=60)
    macro_record_btn = Button(master, text="Start recording", bg="#ffffff", 
        command=lambda:pm.record_some_macro(str(new_macro_name.get()))) #wrap just in case
    macro_record_btn.place(x=20, y=80)
    track_btn(macro_des)
    track_btn(new_macro_label)
    track_btn(new_macro_box)
    track_btn(macro_record_btn)
def allrecorded_mode(master):
    global elementz, macro_list
    destroy_all()
    filename = pm.filename
    all_macs = "" #get all user-submitted macros' names
    f =  open(filename, 'rb')
    while True:
        try:
            macro_obj = dill.load(f)
            all_macs += macro_obj[0] + "\n"
        except EOFError:
            break
        except: #generic errors
            pass
    f.close()
    desc_allrecorded = Label(master, text="Below are your submitted macros.", 
        **main_app_text)
    desc_allrecorded.place(x=20, y=40)
    del_macros = Button(master, text="Delete all macros", command=lambda:clear_macros())
    del_macros.place(x = 20, y =60)
    mac_label = Label(master, text=all_macs, **main_app_text)
    mac_label.place(x=20, y = 100)
    track_btn(desc_allrecorded)
    track_btn(mac_label)
    track_btn(del_macros)
def about_mode(master):
    global elementz
    destroy_all()
    big_about = Label(master, text="About", **main_app_text, font=('Arial', 20))
    big_about.place(x=20, y=30)
    track_btn(big_about)
    basic_cmds = Label(master, text='off\nmouse/drag north/south/east/west\nscroll up/down\nleft/right click\n'
    + 'press <key>\ntype <text>\ncombine <keys>\nweb <site>\nminimize/maximize\nsearch <query>',
         **main_app_text)
    basic_cmds.place(x=20, y=60)
    track_btn(basic_cmds)
#Change widget color upon being hovered
def on_enter(e): 
    e.widget['background'] = '#505050'
def on_leave(e):
    e.widget['background'] = '#3c3c3c'
def button_hovered(my_butt):
    my_butt.bind("<Enter>", on_enter)
    my_butt.bind("<Leave>", on_leave)

#def gui_main():
img_path = str(pathlib.Path().resolve()) +"\\title_icon robot.png"
title_photo = PhotoImage(file = img_path)
root.iconphoto(False, title_photo)
s_w = screen_w(root) * 0.31
s_h = screen_h(root) * 0.25
#print(f"Tracking screen dimension: %d %d" % (screen_h(root),screen_w(root))) #just for debug
root.geometry('%dx%d+%d+%d' % (s_w, s_h, screen_w(root) - s_w, screen_h(root) - s_h * 2))
root.title("Tony: Silent Mode")
root.configure(bg="#1e1e1e")    
root.resizable(width=False, height=True)
welcome = Label(root, text="Click a button above to start commanding your bot!", **main_app_text)
welcome.place(x=25, y=70)
track_btn(welcome)

#Top bar: Selection between Voice mode, Text mode, and Macro (Record)
#   Text:   Allow user-submitted command into a query box
#   Record macro: Prompt user-submitted macro and its name
#   All recorded macros: display the name of all user-submitted macros
#   About:  Display project + team info
text_button = Button(root, text="Text",**top_button_style, command=lambda:text_mode(root))
record_button = Button(root, text="Record macro",**top_button_style,
    command=lambda:record_mode(root))
all_recorded_button  = Button(root, text="Macros recorded",**top_button_style, 
        command=lambda:allrecorded_mode(root))
about_button = Button(root, text="About",**top_button_style, command=lambda:about_mode(root))
top_buttons = [text_button, record_button, all_recorded_button, about_button]
for i in range(0, len(top_buttons)):
    top_buttons[i].grid(column=i, row=0)
    button_hovered(top_buttons[i])
root.mainloop()
#return 0
