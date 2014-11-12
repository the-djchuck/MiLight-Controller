import logging
import socket
import time
import values

DEFAULT_IP = '127.0.0.1'
DEFAULT_PORT = 8899
DEFAULT_SLEEP = 10


class WifiController:
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
        except Exception as e:
            logging.error(e)

    def send_multiple_messages(self, messages, sleep_time=None):
        if sleep_time is None:
            sleep_time = DEFAULT_SLEEP
        for message in messages:
            self.send_message(message)
            time.sleep(sleep_time)

    def zone_on(self, zone='All'):
        try:
            self.send_message(values.ZONE_ON[zone])
        except KeyError:
            logging.error('Not a valid Zone')

    def zone_off(self, zone='All'):
        try:
            self.send_message(values.ZONE_OFF[zone])
        except KeyError:
            logging.error('Not a valid Zone')

    def dim_over_time(self, seconds=75):
        sleep_time = seconds/25
        brightness = 0x1B
        for x in range(0, 25):
            self.send_message(bytearray([0x4E, brightness-x, 0x55]))
            time.sleep(sleep_time)

    def bright_over_time(self, seconds=75):
        sleep_time = seconds/25
        brightness = 0x02
        for x in range(0, 25):
            self.send_message(bytearray([0x4E, brightness+x, 0x55]))
            time.sleep(sleep_time)

    def full_spectrum(self, seconds=255):
        sleep_time = seconds/255
        color = 0x00
        for x in range(0, 255):
            self.send_message(bytearray([0x40, color+x, 0x55]))
            time.sleep(sleep_time)
