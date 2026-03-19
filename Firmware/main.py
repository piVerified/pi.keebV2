print("Starting PI.KEEB")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType

keyboard = KMKKeyboard()

#Hardware
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#modules
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

#Macros
SPOTIFY = send_string(KC.LGUI(KC.S), "spotify", KC.ENTER)
EDGE = send_string(KC.LGUI(KC.S), "edge", KC.ENTER)
CALENDAR = KC.LGUI(KC.N)

#Keymap 
keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.CALC,
        CALENDAR,      SPOTIFY,       KC.NO,
        EDGE,          KC.NO,         KC.MUTE
    ]
]

#Encoder 
encoder_handler.pins = ((board.GP0, board.GP1, None, False),)
encoder_handler.map = [
    ((KC.VOLU, KC.VOLD),)
]

#OLED 
oled_ext = Oled(
    OledDisplayMode.STATIC,
    oob_config={
        'scl': board.GP7,
        'sda': board.GP6,
    },
)
keyboard.extensions.append(oled_ext)

if __name__ == '__main__':
    keyboard.go()
