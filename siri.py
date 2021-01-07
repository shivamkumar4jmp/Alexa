import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listner = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri', '')
                print(command)
    except:
        pass
    return command

def run_siri():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        # print(time)
        talk('Right now time is ' + time)
    elif 'who is' in command:
        person =  command.replace('who is' , '')
        info = wikipedia.summary(person , 2)
        print(info)
        talk(info)
    elif 'date' or 'girlfriend' in command:
        talk('sorry , I have a Boyfriend')
    elif 'are you single' in command:
        talk('no, I am in a relationship with Internet')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        else:
        talk('I can not understand please repeat again')




while True:
    run_siri()