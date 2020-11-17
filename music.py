import pyttsx3
import threading
from playsound import playsound

engine = pyttsx3.init(driverName='sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+25)
voices = engine.getProperty('voices')
file1 = open("khaled.txt","r+")



class TestThreading(object):
    def __init__(self, interval=1):
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        while True:
            # More statements comes here
            playsound('beat.mp3')

tr = TestThreading()
engine.say(file1.read())
engine.runAndWait()