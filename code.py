#!/usr/bin/env python3
# Created by: Remy Skelton
# Date: Dec. 19,2023
# This program is a "Space Alien" game on pybadge




import stage
import ugame
import random
import time
import constants


def menu_scene():
    # this function is the code create the main game scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text object
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(30,10)
    text1.text("Messi studio")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS START")
    text.append(text2)

    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = text + [background]
    # render the sprites
    # render the game scene once per scene
    game.render_block()


    # a forever loop
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:
            game_scene()

        # redraw the sprites
        game.tick()


def splash_scene():
    # this function is the code create the main game scene


    # sound to play
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

   # used this program to split the image into tile: 

    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png

    background.tile(2, 2, 0)  # blank white

    background.tile(3, 2, 1)

    background.tile(4, 2, 2)

    background.tile(5, 2, 3)

    background.tile(6, 2, 4)

    background.tile(7, 2, 0)  # blank white



    background.tile(2, 3, 0)  # blank white

    background.tile(3, 3, 5)

    background.tile(4, 3, 6)

    background.tile(5, 3, 7)

    background.tile(6, 3, 8)

    background.tile(7, 3, 0)  # blank white



    background.tile(2, 4, 0)  # blank white

    background.tile(3, 4, 9)

    background.tile(4, 4, 10)

    background.tile(5, 4, 11)

    background.tile(6, 4, 12)

    background.tile(7, 4, 0)  # blank white



    background.tile(2, 5, 0)  # blank white

    background.tile(3, 5, 0)

    background.tile(4, 5, 13)

    background.tile(5, 5, 14)

    background.tile(6, 5, 0)

    background.tile(7, 5, 0)  # blank white

    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = [background]
    # render the sprites
    # render the game scene once per scene
    game.render_block()


    # a forever loop
    while True:
        # wait for 2 seconds to go to menu
        time.sleep(2.0)
        menu_scene()



def game_scene():
    # this function is the code create the main game scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # sound to play
    pew_sound = open("pew.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)


    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)


    # a sprite that will update every frame with te background
    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    alien = stage.Sprite(image_bank_sprites, 9, int(constants.SCREEN_X / 2 - constants.SPRITE_SIZE / 2), 16)


    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = [ship] + [alien] + [background]
    # render the sprites
    # render the game scene once per scene
    game.render_block()


    # a forever loop
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()


        # A button to shoot
        if keys & ugame.K_O != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_released"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        # B button
        if keys & ugame.K_O != 0:
            pass
        if keys & ugame.K_START != 0:
            pass
        if keys & ugame.K_SELECT != 0:
            pass
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + 1, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - 1, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_UP:
            if ship.y >= 0:
                ship.move(ship.x, ship.y - 1)
            else:
                ship.move(ship.x, 0)
        if keys & ugame.K_DOWN:
            if ship.y <= 120:
                ship.move(ship.x, ship.y + 1)
            else:
                ship.move(ship.x, 120)
        # update the logic of the game
        if a_button == constants.button_state["button_just_pressed"]:
            sound.play(pew_sound)

        # only refresh the sprite
        game.render_sprites([ship] + [alien])
        game.tick()




if __name__ == "__main__":
    splash_scene()