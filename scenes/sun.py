from controller import WifiController


class Sun:
    def __init__(self, ip_address=None, port=None):
        self.milight = WifiController(ip_address=ip_address, port=port)

    def sunrise(self, zone='All'):
        self.milight.zone_on(zone=zone)
        self.milight.quick_pause()
        self.milight.dim()
        self.milight.custom_color(color=0x95)
        self.milight.bright_over_time(seconds=60, brightness_level=5)
        self.milight.custom_color(color=0x94)
        self.milight.bright_over_time(seconds=60, brightness_level=10)
        self.milight.custom_color(color=0x93)
        self.milight.bright_over_time(seconds=60, brightness_level=15)
        self.milight.custom_color(color=0x92)
        self.milight.bright_over_time(seconds=60, brightness_level=20)
        self.milight.custom_color(color=0x91)
        self.milight.bright_over_time(seconds=60, brightness_level=25)

    def sunset(self, zone='All'):
        self.milight.zone_on(zone=zone)
        self.milight.quick_pause()
        self.milight.bright()
        self.milight.custom_color(color=0x91)
        self.milight.dim_over_time(seconds=60, dim_level=20)
        self.milight.custom_color(color=0x92)
        self.milight.dim_over_time(seconds=60, dim_level=15)
        self.milight.custom_color(color=0x93)
        self.milight.dim_over_time(seconds=60, dim_level=10)
        self.milight.custom_color(color=0x94)
        self.milight.dim_over_time(seconds=60, dim_level=5)
        self.milight.custom_color(color=0x95)
        self.milight.dim_over_time(seconds=60, dim_level=0)

