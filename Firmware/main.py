
import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

from kmk.modules.layers import Layers






keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules.append(layers)
keyboard.modules.append(encoder_handler)
keyboard.extensions.append(MediaKeys())


# Define matrix pins based on the schematic, using GP pins
keyboard.col_pins = (board.GP0, board.GP1, board.GP2)  # COLUMN_1, COLUMN_2, COLUMN_3
keyboard.row_pins = (board.GP5, board.GP4, board.GP3)  # ROW_A, ROW_B, ROW_C
keyboard.diode_orientation = DiodeOrientation.COL2ROW



# Define keymap
keyboard.keymap = [
    [
        KC.A, KC.B, KC.C,
        KC.D, KC.E, KC.F,
        KC.G, KC.H, KC.I
    ]
]

# Configure encoder based on the schematic, using GP pins
encoder_handler.pins = ((board.GP10, board.GP9, board.GP8),)  # ENCA, ENCB, ENC_SWITCH
# Encoder map
encoder_handler.map = [(
    (KC.VOLU, KC.VOLD),
    KC.MUTE  # This will be triggered when the encoder is pressed
)]

if __name__ == '__main__':
    keyboard.go()