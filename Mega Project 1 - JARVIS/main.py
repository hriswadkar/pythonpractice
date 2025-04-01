import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary


recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def processCommand(command):
    print("Command: " + command)
    if "open youtube" in command.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif command.lower() == "play":
        song = command.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

def speak(text):
    ttsx.say(text)
    ttsx.runAndWait()

if __name__ == "__main__":
    # Entry point for the program    
    print("JARVIS is starting...")
    speak("JARVIS is starting...")
    while True:
        # listen for the wake word "JARVIS"
        r = sr.Recognizer()        
        
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening!")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
        
            command = r.recognize_google(audio)
            if(command.lower() == "jarvis"):
                speak("Yes sir, how can I help you?")
                
                with sr.Microphone() as source:
                    print("Listening!")
                    print("Yes sir, how can I help you?")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
