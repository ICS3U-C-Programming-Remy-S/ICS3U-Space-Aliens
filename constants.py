#!/usr/bin/env python3
# Created by: Remy Skelton
# Date: Dec. 19,2023
# This constants file for the space Alien game

# screen size is 160x128 and sprite size is 16x16
SCREEN_X = 160
SCREEN_Y = 128
SCREEN_GRID_X = 10
SCREEN_GRID_Y = 8
SPRITE_SIZE = 16
TOTAL_NUMBER_OF_ALIENS = 5
FPS = 60
SPRITE_MOVEMENT_SPEED = 1

# used for buttons
button_state = {
    "button_up": "up",
    "button_just_pressed": "just pressed",
    "button_still_pressed": "still pressed",
    "button_released": "released"
}
# pallet for red filled text
NEW_PALETTE = (b'\xff\xff\x00\x22\xcey\x22\xff\xff\xff\xff\xff\xff\xff\xff\xff'

b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff')