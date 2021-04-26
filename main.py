from pynput import mouse
from pynput import keyboard
import playsound
from threading import Thread

sound_path = "no.mp3"


def on_click(x, y, button, pressed):
    if pressed:
        Thread(target=playsound.playsound, kwargs={"sound": sound_path}).start()

def on_press(key):
    Thread(target=playsound.playsound, kwargs={"sound": sound_path}).start()

mlistener = mouse.Listener(on_click=on_click)
mlistener.start()

klistener = keyboard.Listener(on_press=on_press)
klistener.start()

while True:
    pass