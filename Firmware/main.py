print("Starting PI.KEEBV2")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.matrix import DiodeOrientation
from kmk.handlers.sequences import send_string
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()

#Hardware
keyboard.col_pins = (board.GP26, board.GP27, board.GP28)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW


#Macros TBD


#Keymap 
keyboard.keymap = [
    [
        KC.1, KC.2, KC.3,
        KC.4, KC.5, KC.6,
        KC.7, KC.8, KC.9,

    ]


if __name__ == '__main__':
    keyboard.go()
