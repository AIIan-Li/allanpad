import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP0, board.GP1, board.GP2)
keyboard.row_pins = (board.GP3, board.GP4, board.GP5)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = ((board.GP6, board.GP7, board.GP8, False),)

VOLUME_UP = KC.AUDIO_VOL_UP
VOLUME_DOWN = KC.AUDIO_VOL_DOWN

keyboard.keymap = [
    [
        KC.N1,  KC.N2,  KC.N3,
        KC.N4,  KC.N5,  KC.N6,
        KC.N7,  KC.N8,  KC.N9,
    ]
]

encoder_handler.map = [
    ((VOLUME_UP, VOLUME_DOWN),)
]

if __name__ == '__main__':
    keyboard.go()