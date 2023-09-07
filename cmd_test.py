from tello import Tello
import threading

tello = Tello()

def cmd(str):
    tello.send_command(str)

def loop():
    while True:
        s = input()
        cmd(s.replace('\n', ''))

t = threading.Thread(target=loop)
t.start()