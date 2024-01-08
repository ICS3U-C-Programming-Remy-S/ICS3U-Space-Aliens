#!/usr/bin/env python3
# Created by: Remy Skelton
# Date: Dec. 19,2023
# This program is a "Space Alien" game on pybadge




import stage
import ugame


def game_scene():
    # this function is the code create the main game scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")


    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background, 10, 8)


    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all the sprites, items to show in order
    game.layers = [background]
    # render the sprites
    # render the game scene once per scene
    game.render_block()
   
    # a forever loop
    while True:
        pass # place holder


if __name__ == "__main__":
    game_scene()