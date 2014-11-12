ZONE_ON = {'All': bytearray([0x42, 0x00, 0x55]),  # All Zones
           '1': bytearray([0x45, 0x00, 0x55]),  # Zone 1
           '2': bytearray([0x47, 0x00, 0x55]),  # Zone 2
           '3': bytearray([0x49, 0x00, 0x55]),  # Zone 3
           '4': bytearray([0x4B, 0x00, 0x55]),  # Zone 4
           }

ZONE_OFF = {'All': bytearray([0x41, 0x00, 0x55]),  # All Zones
            '1': bytearray([0x46, 0x00, 0x55]),  # Zone 1
            '2': bytearray([0x48, 0x00, 0x55]),  # Zone 2
            '3': bytearray([0x4A, 0x00, 0x55]),  # Zone 3
            '4': bytearray([0x4C, 0x00, 0x55]),  # Zone 4
            }

COLORS = {'Violet': 0x00,
          'Royal_Blue': 0x10,
          'Baby_Blue': 0x20,
          'Aqua': 0x30,
          'Mint': 0x40,
          'Seafoam_Green': 0x50,
          'Green': 0x60,
          'Lime_Green': 0x70,
          'Yellow': 0x80,
          'Yellow_Orange': 0x90,
          'Orange': 0xA0,
          'Red': 0xB0,
          'Pink': 0xC0,
          'Fuchsia': 0xD0,
          'Lilac': 0xE0,
          'Lavender': 0xF0,
          }
