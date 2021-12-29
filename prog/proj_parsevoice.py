import speech_recognition as sr

def tony():
    print("Please speak with clear pauses in place of spaces!")
    listener = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Tony is listening...")
                listener.adjust_for_ambient_noise(source)   #wait for 1s before talking
                voice = listener.listen(source)
                cmd = listener.recognize_google(voice)
                print(">>VOICE: "+ cmd)
                cmd = cmd.lower()
                if 'off' in cmd:
                    break
                if 'tony' in cmd:
                    tony_index = cmd.index('tony')
                    instruction = cmd[tony_index:] #pass the rest of the cmd to be executed
                
        except sr.UnknownValueError:  #Unintelligible noises - coughing, sneezing, etc. or no noise at all
            print("ERROR: No voice, or voice cannot be transcribed")
        except: #generic errors
            print("I dont know what to do")
    return 0

tony()