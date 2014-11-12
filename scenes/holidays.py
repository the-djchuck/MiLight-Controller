import values

def july_fourth(zone='All'):
    messages = [[0x40, values.COLORS['Red'], 0x55],
                ['sleep', 15],
                [0x40, values.COLORS['Royal_Blue'], 0x55],
                ['sleep', 15],
                [values.WHITE[zone], 0x00, 0x55],
                ['sleep', 15],
                ]
    return messages


def halloween():
    messages = [[0x40, values.COLORS['Orange'], 0x55],
                ['sleep', 15],
                [0x40, values.COLORS['Green'], 0x55],
                ['sleep', 15],
                ]
    return messages


def christmas():
    messages = [[0x40, values.COLORS['Red'], 0x55],
                ['sleep', 15],
                [0x40, values.COLORS['Green'], 0x55],
                ['sleep', 15],
                ]
    return messages