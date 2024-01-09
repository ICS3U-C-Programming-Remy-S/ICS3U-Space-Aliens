#!/usr/bin/env python3
# Created by: Remy Skelton
# Date: Dec. 19,2023
# This program is a "Space Alien" game on pybadge




import stage
import ugame
import constants


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
    game_scene()