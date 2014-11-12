import controller


ZONES_ON = [0x42,  # All Zones
            0x45,  # Zone 1
            0x47,  # Zone 2
            0x49,  # Zone 3
            0x4B]  # Zone 4

ZONES_OFF = [0x41,  # All Zones
             0x46,  # Zone 1
             0x48,  # Zone 2
             0x4A,  # Zone 3
             0x4C]  # Zone 4


class SunObject:

    def __init__(self, ip_address=None, port=None):
        self.ctl = controller.MiLightWifiController(ip_address, port)
	self.sunrise = [[0x40, 0x95, 0x55],
                        [0x4E, 0x05, 0x55],
                        [0x40, 0x93, 0x55],
                        [0x4E, 0x08, 0x55],
                        [0x40, 0x90, 0x55],
                        [0x4E, 0x0B, 0x55],
                        [0x40, 0x87, 0x55],
                        [0x4E, 0x0E, 0x55],
                        [0x40, 0x84, 0x55],
                        [0x4E, 0x11, 0x55],
                        [0x40, 0x82, 0x55],
                        [0x4E, 0x14, 0x55],
                        [0x40, 0x81, 0x55],
                        [0x4E, 0x17, 0x55],
                        [0x40, 0x80, 0x55],
                        [0x4E, 0x1B, 0x55]]
        self.sunset = [[],
                       [],
                      ]
	
    def start_sunrise(self, zone=0, step_time=30):
        """
        This will simulate a sunrise for selected zone
        """
	self.ctl.send_message([ZONES_ON[zone], 0x00, 0x55])
	self.ctl.send_message([0x4E, 0x02, 0x55])
        self.ctl.send_multiple_messages(self.sunrise, step_time)

    def start_sunset(self, zone=0):
        """
        This will simulate a sunset for selected zone
        """
	ctl.send_multiple_messages(self.sunset,sleep_time=30)
        self.ctl.send_message([ZONES_OFF[zone], 0x00, 0x55])
