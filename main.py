from tello import Tello
import threading

t = Tello()

def loop():
    while True:
        s = input()
        t.send_cmd(s.replace('\n', ''))

cmd_loop = threading.Thread(target=loop)
cmd_loop.start()

t.send_cmd("speed?")
t.send_cmd("battely?")
t.send_cmd("time?")
t.send_cmd("wifi?")
t.send_cmd("sdk?")
t.send_cmd("sn?")

t.send_cmd("takeoff")
t.send_cmd("up 20")
t.send_cmd("left 20")
t.send_cmd("right 20")
t.send_cmd("down 20")
t.send_cmd("flip f")
t.send_cmd("land")
t.send_cmd("streamoff")