import pyttsx3
import speech_recognition as sr
import tkinter as tk

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)
engine.setProperty('rate', 140)

#mowi glos w glosniku
def speak(text):
    engine.say(text)
    engine.runAndWait()

#aktualizuje textbox na ekranie i wywoluje funkcje speak
def printAndSpeak(text):
    text_box.insert(tk.END, text+"\n")
    text_box.update()
    speak(text)

change =[False, False, False, False]

#zmienia kolor swiateł na podany
def changeLight(target, value) :
    global change
    global color
    #print(target)
    #print(value)
    #frames[3].configure(bg=value)
    i=0
    while i <4:
        #print(i)
        if(target[i]==True):
            frames[i].configure(bg=value)
        i+=1
    change=[False, False, False, False]
    color='yellow';

#odbiera komende od usera
def getCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        printAndSpeak("Podaj komendę.....")
        #print("Podaj komendę.....")
        audio=r.listen(source)
        try:
            printAndSpeak("Trwa rozpoznawanie.....")
            query=r.recognize_google(audio, language='pl')
        except Exception as e:
            printAndSpeak("Spróbuj ponownie...")
            #print("Spróbuj ponownie...")
            return "None"
        return query

#przetwarza komendę podaną przez usera
def makeCommand():
    global change
    while True:
        text_box.delete('1.0', tk.END)
        query = getCommand().lower()
        #query = 'włącz trzecie i czwarte światło na niebiesko'
        print(query)
        #xor 3 variables
        if ('włącz' in query and not 'wyłącz' in query and not 'zmień' in query) or (not 'włącz' in query and 'wyłącz' in query and not 'zmień' in query) or (not 'włącz' in query and not 'wyłącz' in query and 'zmień' in query):
            color='yellow'
            if'pierwsze' in query:
                change[0]=True
            if'drugie' in query:
                change[1]=True
            if'trzecie' in query:
                change[2]=True
            if'czwarte' in query:
                change[3]=True
            if(not 'pierwsze' in query and not 'drugie' in query and not 'trzecie' in query and not 'czwarte' in query):
                change=[True, True, True, True]
            if('niebieski' in query or 'niebieskie' in query or 'niebiesko' in query and not 'czerwony' in query and not 'czerwone' in query and not 'czerwono' in query and not 'zielony' in query and not 'zielone' in query and not 'zielono' in query):
                color='blue'
            if(not 'niebieski' in query and not 'niebieskie' in query and not 'niebiesko' in query and 'czerwony' in query or 'czerwone' in query or 'czerwono' in query and not 'zielony' in query and not 'zielone' in query and not 'zielono' in query):
                color='red'
            if(not 'niebieski' in query and not 'niebieskie' in query and not 'niebiesko' in query and not 'czerwony' in query and not 'czerwone' in query and not 'czerwono' in query and 'zielony' in query or 'zielone' in query or 'zielono' in query):
                color='green'
            if(color is None):
                color='black'
            if('wyłącz' in query and color != 'black'):
                printAndSpeak("Spróbuj ponownie")
            if 'włącz' in query:
                changeLight(change, color)
                printAndSpeak("Włączono światła")
            if 'wyłącz' in query:
                changeLight(change, 'black')
                printAndSpeak('Wyłączono światła')
            if 'zmień' in query:
                print(change)
                changeLight(change, color)
                printAndSpeak('Zmieniono kolor świateł')
        else:
            printAndSpeak("Spróbuj ponownie")
        return

#struktura elementów na ekranie
root = tk.Tk()
canvas  = tk.Canvas(root, height=550, width=400, bg="lightblue")
canvas.grid(columnspan=3)

frame1 = tk.Frame(root, bg='black')
frame1.place(width=120, height=120, x=60, y=60)


frame2 = tk.Frame(root, bg='black')
frame2.place(width=120, height=120, x=240, y=60)

frame3 = tk.Frame(root, bg='black')
frame3.place(width=120, height=120, x=60, y=240)

frame4 = tk.Frame(root, bg='black')
frame4.place(width=120, height=120, x=240, y=240)

frames = [frame1, frame2, frame3, frame4]


text_box=tk.Text(root, height=100, width=100)
text_box.insert(1.0, "Witaj!\nKliknij przycisk aby rozpocząć nasłuchiwanie")
text_box.place(x=0, y=400)

recognize_txt=tk.StringVar()
recognize_btn=tk.Button(root, textvariable=recognize_txt, bg="purple", command=lambda:makeCommand())
recognize_txt.set("Nasłuchuj")
recognize_btn.place(x=180, y=370)

root.mainloop()

