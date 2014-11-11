import controller

ZONES_ON = ['0x42',  # All Zones
            '0x45',  # Zone 1
            '0x47',  # Zone 2
            '0x49',  # Zone 3
            '0x4B']  # Zone 4

ZONES_OFF = ['0x41',  # All Zones
             '0x46',  # Zone 1
             '0x48',  # Zone 2
             '0x4A',  # Zone 3
             '0x4C']  # Zone 4


def sunrise(zone=0):
    """
    This will simulate a sunrise for selected zone
    zone 0 is for all
    :return:
    """
    ctl = controller.MiLightWifiController()
    message_time = 30
    messages = []
    on_message = '%s 0x00 0x55' % ZONES_ON[zone]
    messages.append(on_message)
    ctl.send_multiple_messages(messages,sleep_time=message_time)


def sunset(zone=0):
    """
    This will simulate a sunset for selected zone
    zone 0 is for all
    :return:
    """
    ctl = controller.MiLightWifiController()
    message_time = 30
    messages = []
    on_message = '%s 0x00 0x55' % ZONES_OFF[zone]
    messages.append(on_message)
    ctl.send_multiple_messages(messages,sleep_time=message_time)