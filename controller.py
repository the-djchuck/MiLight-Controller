import socket
import time

DEFAULT_IP = '127.0.0.1'
DEFAULT_PORT = 8899
DEFAULT_SLEEP = 10


class MiLightWifiController:

    def __init__(self, ip_address=None, port=None):
        if ip_address is None:
            self.ip_address = DEFAULT_IP
        else:
	    self.ip_address = ip_address
	if port is None:
            self.port = DEFAULT_PORT
	else:
	    self.port = port
	
    def send_message(self, message):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(message, (self.ip_address, self.port))
            sock.close()
        except socket.error:
            print 'Message %s could not be sent' % message

    def send_multiple_messages(self, messages, sleep_time=None):
        if sleep_time is None:
            sleep_time = DEFAULT_SLEEP
        for message in messages:
            self.send_message(message)
            time.sleep(sleep_time)

    def all_on(self):
        self.send_message(bytearray([0x42, 0x00, 0x55]))

    def all_off(self):
        self.send_message(bytearray([0x41, 0x00, 0x55]))
