import struct

def cmd_form(string):
    return chr(string).encode()

RESET       =cmd_form(7)
START       =cmd_form(128)
BAUD        =cmd_form(129)
CONTROL     =cmd_form(130)
SAFE        =cmd_form(131)
FULL        =cmd_form(132)
POWER       =cmd_form(133)
SPOT        =cmd_form(134)
CLEAN       =cmd_form(135)
MAX         =cmd_form(136)
DRIVE       =cmd_form(137)
DOCK        =cmd_form(143)
STOP        =cmd_form(173)

#Special drive cases
VEL_MAX     =500
RAD_MAX     =2000
STRAIGHT    =32767  #0x8000
ZERORAD_C   =-1     #0xFFFF
ZERORAD_CC  =1      #0x0001

def hex_split(integer):
    high, low = struct.unpack('>BB', struct.pack('>h', integer))
    return high, low
