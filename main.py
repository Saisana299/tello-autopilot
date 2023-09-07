from tello import Tello

t = Tello()

t.send_command("speed?")
t.send_command("battely?")
t.send_command("time?")
t.send_command("wifi?")
t.send_command("sdk?")
t.send_command("sn?")

t.send_command("takeoff")
t.send_command("up 20")
t.send_command("left 20")
t.send_command("right 20")
t.send_command("down 20")
t.send_command("flip f")
t.send_command("land")
t.send_command("streamoff")

for l in t.get_log():
    print(l)