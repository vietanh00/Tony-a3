import subprocess, time

#try:
import speech_recognition as sr
"""except:
    subprocess.run(["pip", "install", "speech_recognition"])
    time.sleep(2)
    import speech_recognition as sr"""

voice_heard = ""
import proj_commands as pc
def tony():
    global voice_heard
    print("Please speak with clear pauses in place of spaces!")
    listener = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as source:
                print("Tony is listening...")
                listener.adjust_for_ambient_noise(source)   #wait for 1s before talking
                voice = listener.listen(source)
                voice_heard = listener.recognize_google(voice)
                print(">>VOICE: "+ voice_heard) #print everything that the bot could recognize
                voice_heard = voice_heard.lower()
                if 'off' in voice_heard:
                    print("Tony is shutting down")
                    return 1
                    break
                if 'tony' in voice_heard:
                    tony_index = voice_heard.index('tony')
                    instruction = voice_heard[(tony_index + 5):] #pass the rest of the cmd to be executed
                    pc.execute_commands(instruction)
        except sr.UnknownValueError:  #Unintelligible noises - coughing, sneezing, etc. or no noise at all
            print("Tony: No voice, or voice cannot be transcribed")
        except Exception as e: #generic errors
            print("Tony caught this " + str(e))
    return 0

tony()