import socket
import time

DEFAULT_IP = '127.0.0.1'
DEFAULT_PORT = 8899
DEFAULT_SLEEP = 10


class MiLightWifiController:

    def __init__(self, ip_address=None, port=None):
        if ip_address is None:
            self.ip_address = DEFAULT_IP
        if port is None:
            self.port = DEFAULT_PORT

    def send_message(self, message):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(message, (self.ip_address, self.port))

    def send_multiple_messages(self, messages, sleep_time=None):
        if sleep_time is None:
            sleep_time = DEFAULT_SLEEP

        for message in messages:
            self.sendMessage(self, message)
            time.sleep(sleep_time)
