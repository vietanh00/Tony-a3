#Small GUI with widgets
#This is to allow user to manually close program or type commands
#It is also reassuring to see the program on screen
from tkinter import *
from tkinter import ttk
from style import *
#Create a small window for GUI
#Widgets: Minimize, Close
#Entries: Query box, enter button
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
def voice_mode(master):
    global elementz
    destroy_all()
    voice_desc = Label(master, text="The application will try and recognize your voice command.", 
        **main_app_text)
    voice_recognized = Label(master, text="haha", **main_app_text)
    track_btn(voice_desc)
    track_btn(voice_recognized)
    voice_desc.place(x=20, y = 50)
    voice_recognized.place(x=20, y = 100)
def text_mode(master):
    global elementz
    destroy_all()
    text_desc  = Label(master, text="Type your command(s) in the box below, separated by commas", 
        **main_app_text)
    text_desc.place(x=20, y=50)
    text_entry = StringVar()
    text_box   = Entry(master, textvariable=text_entry)
    text_box.place(x=20, y=70, width=300)
    track_btn(text_desc)
    track_btn(text_box)
def record_mode(master):
    global elementz
    destroy_all()
    new_macro_name  = StringVar()
    macro_des       = Label(master, text="Click below to start recording a new macro.")
    new_macro_label = Label(master, text="Your macro name:", **main_app_text)
    new_macro_label.place(x=20, y=40)
    new_macro_box   = Entry(master, textvariable=new_macro_name)
    new_macro_box.place(x=20, y=60)
    macro_record_btn = Button(master, text="Start recording", bg="#ffffff")
    macro_record_btn.place(x=20, y=80)
    track_btn(macro_des)
    track_btn(new_macro_label)
    track_btn(new_macro_box)
    track_btn(macro_record_btn)
def allrecorded_mode(master):
    global elementz
    destroy_all()
    desc_allrecorded = Label(master, text="Below are your submitted macros.", 
        **main_app_text)
    desc_allrecorded.place(x=20, y=40)
    track_btn(desc_allrecorded)
def about_mode(master):
    global elementz
    destroy_all()
    big_about = Label(master, text="About", **main_app_text, font=('Arial', 20))
    big_about.place(x=20, y=30)
    track_btn(big_about)
def on_enter(e):
    e.widget['background'] = '#505050'
def on_leave(e):
    e.widget['background'] = '#3c3c3c'
def button_hovered(my_butt):
    my_butt.bind("<Enter>", on_enter)
    my_butt.bind("<Leave>", on_leave)

def gui_main():
    root = Tk()
    root.geometry('400x150+%d+%d' % (screen_w(root) - 400, screen_h(root) - 250))
    root.title("Friendly Neighborhood Voice Assistant")
    root.configure(bg="#1e1e1e")    
    #2) Main
    #2.1. Voice:  Recognize user speech and print it onto the application box
    #2.2. Text:   Allow user-submitted command into a query box    
    #2.4. Macros recorded: Display all user-recorded macros (name + date + description)
    #2.5. About:  Display project + team info

    #1)Top bar: Selection between Voice mode, Text mode, and Macro (Record)
    #Start with voice mode by default
    voice_button = Button(root, text="Voice",**top_button_style, command=lambda: voice_mode(root))
    text_button = Button(root, text="Text",**top_button_style, command=lambda:text_mode(root))
    record_button = Button(root, text="Record macro",**top_button_style,
        command=lambda:record_mode(root))
    all_recorded_button  = Button(root, text="Macros recorded",**top_button_style, 
        command=lambda:allrecorded_mode(root))
    about_button = Button(root, text="About",**top_button_style, command=lambda:about_mode(root))
    top_buttons = [voice_button, text_button, record_button, all_recorded_button, about_button]
    for i in range(0, len(top_buttons)):
        top_buttons[i].grid(column=i, row=0)
        button_hovered(top_buttons[i])
    print("Tracking screen dimension")
    print(screen_h(root))
    print(screen_w(root))
    root.mainloop()
    return 0

gui_main()