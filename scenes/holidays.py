from controller import WifiController
import scenes

class Holidays:
    def __init__(self, ip_address=None, port=None):
        self.milight = WifiController(ip_address=ip_address, port=port)

    def july_fourth(self, zone='All'):
        color_list = ['Red', 'Royal_Blue', 'White']
        scenes.custom_cycle(controller=self.milight,
                            zone=zone,
                            color_list=color_list)

    def halloween(self, zone='All'):
        color_list = ['Orange', 'Green']
        scenes.custom_cycle(controller=self.milight,
                            zone=zone,
                            color_list=color_list)

    def christmas(self, zone='All'):
        color_list = ['Red', 'Green']
        scenes.custom_cycle(controller=self.milight,
                            zone=zone,
                            color_list=color_list)