from tello import Tello

t = Tello()

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

for l in t.get_log():
    print(l)