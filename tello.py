import socket
import threading
import time
import cv2
from stats import Stats

class Tello:
    def __init__(self, cmd_timeout_sec: float = 15.0, tello_ip: str = '192.168.10.1', tello_port: int = 8889, local_port: int = 8889) -> None:
        self.local_port = local_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # socket for sending cmd
        self.socket.bind(('', self.local_port))

        # thread for receiving cmd ack
        self.receive_thread = threading.Thread(target=self._receive_thread)
        self.receive_thread.daemon = True
        self.receive_thread.start()

        self.tello_ip = tello_ip
        self.tello_port = tello_port
        self.tello_adderss = (self.tello_ip, self.tello_port)
        self.log = []

        self.cmd_timeout_sec = cmd_timeout_sec

        # video stream
        self.send_cmd("command")
        self.send_cmd("streamon")

        self.udp_video_address = 'udp://@0.0.0.0:11111'
        self.video_cap = cv2.VideoCapture(self.udp_video_address)
        self.frame = None

        self.receive_video_thread = threading.Thread(target=self._receive_video_thread())
        self.receive_video_thread.daemon = True
        self.receive_video_thread.start()

    def __del__(self) -> None:
        self.socket.close()

    def send_cmd(self, cmd: str) -> None:
        """
        Send a command to the ip address. Will be blocked until
        the last command receives an 'OK'.
        If the command fails (either b/c time out or error),
        will try to resend the command
        :param command: (str) the command to send
        :param ip: (str) the ip of Tello
        :return: The latest command response
        """
        self.log.append(Stats(cmd, len(self.log)))

        self.socket.sendto(cmd.encode('utf-8'), self.tello_adderss)
        print(f'sending command: {cmd} to {self.tello_ip}')

        start = time.time()
        while not self.log[-1].got_response():
            now = time.time()
            diff = now - start
            if diff > self.cmd_timeout_sec:
                print(f'max timeout exceeded... commad {cmd}')
                return

        print(f'done!!! sent command: {cmd} to {self.tello_ip}')

    def _receive_thread(self) -> None:
        """Listen to responses from the Tello.

        Runs as a thread, sets self.response to whatever the Tello last returned.

        """
        while True:
            try:
                self.response, ip = self.socket.recvfrom(1024)
                print(f'from {ip}: {self.response}')

                self.log[-1].add_response(self.response)
            except socket.error as exc:
                print(f'caught exception socket.error : {exc}')

    def _receive_video_thread(self) -> None:
        """
        Listens for video streaming (raw h264) from the Tello with opencv.
        Runs as a thread, sets self.frame to the most recent frame Tello captured.
        """
        while True:
            _, frame = self.video_cap.read()

            if frame is None or frame.size == 0:
                continue

            frame_height, frame_width = frame.shape[:2]
            self.frame = cv2.resize(frame, (int(frame_width/2), int(frame_height/2)))
            cv2.imshow('frame', self.frame)

            if cv2.waitKey(1) & 0xff == ord('q'):
                break

        self.video_cap.release()
        cv2.destroyAllWindows()

    def get_log(self) -> list:
        return self.log
