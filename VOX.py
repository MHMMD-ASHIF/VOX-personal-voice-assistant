import subprocess
import webbrowser
#import ctypes
import requests
import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pygame
from tkinter import *
import wolframalpha
#from bs4 import BeautifulSoup

listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty("rate")
engine.setProperty("rate", 130)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def second_c():
    engine.say('bye ')
    engine.say('take care')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            my_label.config(text="Listening...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source, phrase_time_limit=5)
            command = listener.recognize_google(voice)
            command = command.lower()


    except Exception as e:
        talk('unable to detect your voice')
        pass
    return command


def wake():
    talk('hello sir im online how can i help you')


def run_vox():
    while True:
        command = take_command()

        if "play" in command:
            song = command.replace("play", "")
            talk("playing" + song)
            pywhatkit.playonyt(song)

        elif 'open stackoverflow' in command:
            talk("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")


        elif 'wish me' in command:
            hour = int(datetime.datetime.now().hour)
            if 0 <= hour < 12:
                talk("Good Morning Sir !")


            elif 12 <= hour < 18:
                talk("Good Afternoon Sir !")

            else:
                talk("Good Evening Sir !")



        elif 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you")
            


        elif 'fine' in command or "good" in command:
            talk("It's good to know that your fine")



        elif "what's your name" in command or "What is your name" in command:
            talk("My friends call me  vox")



        elif 'please exit' in command:
            talk("Thanks for giving me your time")
            top.destroy()


        elif 'open wikipedia' in command:
            talk('opening')
            webbrowser.open('https://www.wikipedia.org/')


        elif "why you came to the world" in command:
            talk("Thanks to Ashif. further It's a secret")


        elif 'is love' in command:
            command("It is 7th sense that destroy all other senses")


        elif 'reason for you' in command:
            talk("I was created as a Mini project ")



        elif 'change background' in command:
            ctypes.windll.user32.SystemParametersInfoW(20,
                                                       0,
                                                       "Location of wallpaper",
                                                       0)
            talk("Background changed successfully")



        elif 'lock window' in command:
            talk("locking the device")
            ctypes.windll.user32.LockWorkStation()


        elif "where is" in command:
            command = command.replace("where is", "")
            location = command
            talk("User asked to Locate")
            talk(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")



        elif "are you married" in command:
            talk("no are you interested")

            if 'yes' in command:
                talk('all right i need to ask my parents')
            if 'no' in command:
                talk('ok')


        elif 'where are you from' in command:
            talk('i am from clouds')


        elif 'where is your home' in command:
            talk("above the sky")


        elif 'your fathers name' in command:
            talk('python')


        elif 'your mothers name' in command:
            talk('jarvis')


        elif "weather " in command:

            talk(" City name ")
            city_name = take_command()
            search = "temperature in " + city_name
            url = f"http://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_="BNeawe").text
            talk(f"current {search} is {temp}")


        elif 'open c drive' in command:
            talk('opening')
            os.startfile('C:')


        elif 'open e drive' in command:
            talk('opening')
            os.startfile('E:')


        elif "time" in command:
            time = datetime.datetime.now().strftime("%I:%M %p")
            talk("current time is " + time)


        elif "who is " in command:
            person = command.replace("who is ", "")
            info = wikipedia.summary(person, 1)
            talk(info)


        elif "what is" in command:
            concepts = command.replace("what is", "")
            info = wikipedia.summary(concepts, 1)
            talk(info)

        elif "date" in command:
            talk("sorry,i have a headache")


        elif "are you single" in command:
            talk("im in a relationship with wifi")


        elif "joke" in command:
            talk(pyjokes.get_joke())


        elif "i love you" in command:
            talk("i love you too")


        elif "who made you" in command or "create you" in command:
            talk('i have been created by Muhammed Ashif.')


        elif 'open google' in command:
            talk('opening google')
            webbrowser.open('http://www.google.com')


        elif "shut down fast" in command:
            talk("do you want to shut down the pc ")
            command = take_command()
            choice = command
            if choice == 'yes':
                talk("shutting down the pc")
                os.system("shutdown/s/t 30")
            if choice == 'no':
                talk("Thank for the help")


        elif "hibernate" in command or "sleep" in command:
            talk("Hibernating")
            subprocess.call("shutdown / h")


        elif "restart fast" in command:
            talk("do you want to restart the pc")
            command = take_command()
            choice = command
            if choice == 'yes':
                talk("restarting the pc")
                os.system("shut down/r/t 30")
            if choice == 'no':
                talk("thanks for the Help")


        elif "open chrome" in command:
            talk("opening chrome")
            os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")

        
        elif "open brave" in command:
            talk("opening brave")
            os.startfile("C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe")

        elif "open edge" in command:
            talk("opening microsoft edge")
            os.startfile("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")



        elif "open illustrator" in command:
            talk("opening illustrator")
            os.startfile("C:\Program Files\Adobe\Adobe Illustrator 2020\Support Files\Contents\Windows\Illustrator.exe")


        elif "open photoshop" in command:
            talk("opening photoshop")
            os.startfile("C:\Program Files\Adobe\Adobe Photoshop CC 2019\Photoshop.exe")


        elif "open eclipse" in command:
            talk("opening eclipse")
            os.startfile("E:\ASHY\java ide\eclipse\eclipse.exe")


        elif "who are you" in command or "define yourself" in command:
            speak = '''Hello sir, I am vox. Your personal Assistant. 
            I am here to make your life easier. You can command me to perform 
            various tasks .'''
            talk(speak)


        elif "bye" in command:
            talk("Ok bye and take care")


        elif 'open stack overflow' in command:
            talk('opening')
            webbrowser.open('https://stackoverflow.com/')


        elif 'open youtube' in command:
            talk('opening')
            webbrowser.open('https://www.youtube.com/')


        elif 'open facebook' in command:
            talk('opening')
            webbrowser.open('https://www.facebook.com/')


        elif 'open instagram' in command:
            talk('opening')
            webbrowser.open('https://www.instagram.com/')


        elif 'open email' in command or 'open gmail' in command:
            talk('opening')
            webbrowser.open(
                'https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue'
                '=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1'
                '&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


        elif 'open twitter' in command:
            talk('opening')
            webbrowser.open('https://twitter.com/LOGIN')


        elif 'search' in command:
            webbrowser.open(command)


        elif 'open excel' in command:
            talk('opening excel')
            power = r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"
            os.startfile(power)


        elif 'open powerpoint' in command:
            talk('opening powerpoint')
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE"
            os.startfile(power)


        elif 'open word' in command:
            talk('opening word')
            power = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE"
            os.startfile(power)


        elif 'open publisher' in command:
            talk('opening publisher')
            power = r"C:\Program Files\Microsoft Office\root\Office16\MSPUB.EXE"
            os.startfile(power)


        elif 'open access' in command:
            talk('opening access')
            power = r"C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE"
            os.startfile(power)


        elif 'open notepad' in command:
            talk('opening notepad')
            power = r'notepad.exe'
            os.startfile(power)


        elif "calculate" in command:
            talk('calculating')
            app_id = '6YU2XY-3UQAA293KY'
            client = wolframalpha.Client(app_id)
            indx = command.lower().split().index('calculate')
            query = command.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            talk("The answer is " + answer)




        else:
            talk("please say the command again sir")



def kill():
    top.destroy()




if __name__ == "__main__":
    top = Tk()
    top.geometry("700x900")
    top.resizable(False, False)
    top.title("VOX")
    top.iconbitmap('icon1.ico')

    bg = PhotoImage(file='bg1.png')

    label1 = Label(top, image=bg)
    label1.place(x=0, y=0, relwidth=1, relheight=1)

    pygame.mixer.init()



    def play():
        pygame.mixer.music.load("Mouseclick.mp3")
        pygame.mixer.music.play(loops=0)




    r_button = PhotoImage(file="MIC2.png")
    label11 = Label(image=r_button)

    mic_button = Button(top, image=r_button, command=lambda: [play(), run_vox()], borderwidth=0,
                        width=130,
                        height=130,
                        bg="#050424", activebackground="#050424", activeforeground='blue').place(x=270, y=520)

    stop_button = PhotoImage(file='stop2.png')
    label1 = Label(image=stop_button)

    stop_b = Button(top, image=stop_button, command=lambda: [play(), second_c(), kill()], borderwidth=0,
                    bg='#050424',
                    text='right', activebackground='#050424').place(x=295, y=700)

my_label = Label(top, text="")
my_label.pack(pady=50)
top.mainloop()


