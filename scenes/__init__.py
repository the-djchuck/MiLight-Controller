from controller import WifiController


def custom_cycle(controller=WifiController(), zone='All', color_list=[], pause_time=None):
    controller.zone_on(zone=zone)
    controller.bright()
    for color in color_list:
        if color is 'White':
            controller.white(zone=zone)
        else:
            controller.color(color=color)
        if pause_time is None:
            controller.long_pause()
        else:
            controller.pause(pause_time)