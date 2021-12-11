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

def screen_w(root):
    width = root.winfo_screenwidth()
    return width

def screen_h(root):
    height = root.winfo_screenheight()
    return height

def switch_mode(my_frame, all_frames):
    for f in all_frames:
        f.grid_remove()
    my_frame.grid()

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
    frame_voice = Frame(root, bg="#3c3c3c")
    frame_voice.grid()
    voice_desc = Label(frame_voice, text="The application will try and recognize your voice command.", 
        fg="#ffffff")
    voice_recognized = Label(frame_voice, text="", fg="#ffffff")
    #2.2. Text:   Allow user-submitted command into a query box
    frame_text = Frame(root, bg="#3c3c3c")
    frame_text.grid()
    text_desc  = Label(frame_text, text="Type your command(s) in the box below.", fg="#ffffff")
    text_desc.pack(fill='x', expand=True)
    text_entry = StringVar()
    text_box   = Entry(frame_text, textvariable=text_entry)
    text_box.pack(fill='x', expand=True)
    #2.3. Record: Display recorded user-submitted commands
    frame_record    = Frame(root, bg="#3c3c3c")
    frame_record.grid()
    new_macro_name  = StringVar()
    macro_des       = Label(frame_record, text="Click below to start recording a new macro.")

    new_macro_label = Label(frame_record, text="Your macro name:")
    new_macro_label.pack(fill='x', expand=True)
    new_macro_box   = Entry(frame_record, textvariable=new_macro_name)
    new_macro_box.pack(fill='x', expand=True)
    macro_record_btn = Button(frame_record, text="Start recording", **top_button_style)

    #2.4. Macros recorded: Display all user-recorded macros (name + date + description)
    frame_allrecorded = Frame(root, bg="#3c3c3c")
    frame_allrecorded.grid()
    #2.5. About:  Display project + team info
    frame_about    = Frame(root, bg="#3c3c3c")
    frame_about.grid()
    #1)Top bar: Selection between Voice mode, Text mode, and Macro (Record)
    #Start with voice mode by default
    frame1 = Frame(root, bg="#3c3c3c")
    frame1.place(x=0, y=0, width=400)
    voice_button = Button(frame1, text="Voice",**top_button_style)
    text_button = Button(frame1, text="Text",**top_button_style)
    text_button.configure(command=lambda: switch_mode(frame_text))

    record_button = Button(frame1, text="Record macro",**top_button_style)
    all_recorded_button  = Button(frame1, text="Macros recorded",**top_button_style)
    about_button = Button(frame1, text="About",**top_button_style)
    top_buttons = [voice_button, text_button, record_button, all_recorded_button, about_button]
    frame_mode = [frame_voice, frame_text, frame_record, frame_allrecorded, frame_about]
    switch_mode(frame_voice, frame_mode)
    for i in range(0, len(top_buttons)):
        top_buttons[i].grid(column=i, row=0)
        button_hovered(top_buttons[i])
        top_buttons[i].configure(command=lambda: switch_mode(frame_mode[i], frame_mode))
    print(screen_h(root))
    print(screen_w(root))
    root.mainloop()
    return 0

gui_main()