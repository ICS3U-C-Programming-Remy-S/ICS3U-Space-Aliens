#!/usr/bin/env python3
# Created by: Remy Skelton
# Date: Dec. 19,2023
# This program is a "Space Alien" game on pybadge


import stage
import ugame
import random
import time
import constants
import supervisor


def menu_scene():
    # this function is the code create the menu scene


    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text object
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(30,10)
    text1.text("Messi studios")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS START")
    text.append(text2)
    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)

    text3.move(20,60)
    text3.text("Select for info")
    text.append(text3)
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

        # go to game scene
        if keys & ugame.K_START != 0:
            game_scene()

        # go to info scene
        if keys & ugame.K_SELECT != 0:
            info_scene()

        # redraw the sprites
        game.tick()


def info_scene():
    # this function is the code create the information scene
    # play sound when scene is opened
    info_sound = open("gunshot_echo.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(info_sound)

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # add text object
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(10,10)
    text1.text("Use A to Shoot\nAlien= 1 point\nMove with dpad\nHit = -1 life\n10 to lvl up\n25 to win\nB to boost\nSelect to mute\nlvl + 1 life\nAliens deal double damage")
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(40,110)
    text2.text("PRESS DOWN")
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

        # when down is clicked it goes back to menu
        if keys & ugame.K_DOWN != 0:
            menu_scene()

        # redraw the sprites
        game.tick()


def splash_scene():
    # this function is the code create thesplash scene of game
    # play the splash sound at start of scene
    splash_sound = open("neon_light.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(splash_sound)

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the image into tile: 
    #   https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank
    background.tile(2, 3, 0)  # blank
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank
    background.tile(2, 4, 0)  # blank
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank
    background.tile(2, 5, 0)  # blank
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank

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
    # get the global mute variable created at bottom
    global is_muted

    # create ship speed variable for boost 
    ship_speed = constants.SHIP_SPEED
    # Initialize lives to 3 for lvl 1
    lives = 3

    # Create text to display lives at top right
    lives_text = stage.Text(width=29, height=14)
    lives_text.clear()
    lives_text.cursor(0, 0)
    lives_text.move(89, 1)
    lives_text.text(f"Lives: {lives}")

    # set score to 0 and display in top left
    score = 0
    score_text = stage.Text(width = 29, height = 14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text(f"Score: {score}")

    # set high score to score and display bottom left
    high_score = 0

    high_score_text = stage.Text(width = 29, height = 14)
    high_score_text.clear()
    high_score_text.cursor(0,0)
    high_score_text.move(1,120)
    high_score_text.text(f"High Score: {high_score}")

    # function to display aliens
    def show_alien():
        # take the alien that are off screen and puts them back on
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                         constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                Break

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that keep state information on, set all button to up
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get all sound for the game
    gun_sound = open("rdr_shot.wav", 'rb')
    alien_death_sound = open("rdr_death.wav", 'rb')
    lives_lost_sound = open("t1_be_back.wav", 'rb')
    music_sound = open("good_bad_ugly.wav", 'rb')
    intro_sound = open("dyin_livin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # play sound at start of scene and then start the game
    sound.play(intro_sound)
    time.sleep(2.0)


    # play the western music sound
    sound.play(music_sound)

    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background,
                            constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(3, 14)
            background.tile(x_location, y_location, tile_picked)

    # a sprite that will update every frame with te background
    ship = stage.Sprite(image_bank_sprites, 4,  75, 66)

    # list of aliens to have more than 1
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS):
        a_single_alien = stage.Sprite(image_bank_sprites, 8, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    # call show_alien function to display alien
    show_alien()

    # create a list for the laser to shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS):
        a_single_laser = stage.Sprite(image_bank_sprites, 12, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = [score_text, lives_text, high_score_text] + lasers + [ship] + aliens + [background]

    # render the sprites
    # render the game scene once per scene
    game.render_block()

    # a forever loop
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()

        # take player to lvl 2 scene when score is 10
        if score == 10:
            # sleep for 1 second and call lvl 2 function
            time.sleep(1.0)
            game_lvl_2(score, high_score)

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

         # button B for boost
        if keys & ugame.K_X != 0:
            if b_button == constants.button_state["button_up"]:
                # change to just pressed
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
                # speed boost
                ship_speed += 1
        else:
            # check if state is still pressed
            if b_button == constants.button_state["button_still_pressed"]:
                # set speed back to normal
                b_button = constants.button_state["button_released"]
                # no more boost
                ship_speed -= 1
            else:
                # else change state to button back up again
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_START != 0:
            Pass

        # mute when SELECT button is pressed
        if keys & ugame.K_SELECT != 0:
            if is_muted == True:
                ugame.audio.mute(False)
                is_muted = False
            else:
                ugame.audio.mute(True)
                is_muted = True

        # Movement for ship, with borders and ability to wrap around
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + ship_speed, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - ship_speed, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_UP:
            if ship.y >= 0:
                ship.move(ship.x, ship.y - ship_speed)
            else:
                ship.move(ship.x, 0)
        if keys & ugame.K_DOWN:
            if ship.y <= 120:
                ship.move(ship.x, ship.y + ship_speed)
            else:
                ship.move(ship.x, 120)

        # update the logic of the game
        # play gun sound when button pressed
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(gun_sound)
                    Break

        # each frame to move lasers that has shot
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # when alien goes under the screen
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text(f"Score: {score}")
        
        # within the same function, in the collision detection block
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                                        lasers[laser_number].x + 16, lasers[laser_number].y +16,
                                        aliens[alien_number].x, aliens[alien_number].y,
                                        aliens[alien_number].x +16, aliens[alien_number].y +16):
                            # alien was hit
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(alien_death_sound)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text(f"Score: {score}")
                            if score > high_score:
                                high_score = score
                                high_score_text.clear()
                                high_score_text.cursor(0,0)
                                high_score_text.move(1,120)
                                high_score_text.text(f"High Score: {high_score}")
                            show_alien()
                            show_alien()

        # collision detection between ship and alien
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # When alien hits ship
                    sound.stop()
                    sound.play(lives_lost_sound)
                    # Deduct a life
                    lives -= 1
                    lives_text.clear()
                    lives_text.cursor(0, 0)
                    lives_text.move(89, 1)
                    lives_text.text(f"Lives: {lives}")
                    if lives == 0:
                        time.sleep(3.0)
                        game_over_scene(score, high_score)
                    else:
                        time.sleep(3.0)
                        # Continue playing by resetting the ship position
                        ship.move(constants.SCREEN_X // 2, constants.SCREEN_Y - constants.SPRITE_SIZE)

        # only refresh the sprite
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()

def game_lvl_2(score, high_score):
    # this function is the code create the 2nd game scene
    # create the ship speed variable
    ship_speed = constants.SHIP_SPEED

    # mute variable
    global is_muted
    # Initialize lives to 4 for lvl 2
    lives = 4

    # Create text for lives display
    lives_text = stage.Text(width=29, height=14)
    lives_text.clear()
    lives_text.cursor(0, 0)
    lives_text.move(89, 1)
    lives_text.text(f"Lives: {lives}")

    # keep score the same as lvl 1 and display
    score_text = stage.Text(width = 29, height = 14)
    score_text.clear()
    score_text.cursor(0,0)
    score_text.move(1,1)
    score_text.text(f"Score: {score}")

    # highscore from lvl 1 and display
    high_score_text = stage.Text(width = 29, height = 14)
    high_score_text.clear()
    high_score_text.cursor(0,0)
    high_score_text.move(1,120)
    high_score_text.text(f"High Score: {high_score}")

    # display the alien
    def show_alien():
        # take the alien that are off screen and puts them back on
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x < 0:
                aliens[alien_number].move(random.randint(0 + constants.SPRITE_SIZE,
                                                         constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)
                Break

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("mt_game_studio.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    # buttons that keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get all the sounds to play in this scene
    gun_sound = open("rdr_shot.wav", 'rb')
    alien_death_sound = open("rdr_death.wav", 'rb')
    lives_lost_sound = open("gunshot_echo.wav", 'rb')
    music_sound = open("good_bad_ugly.wav", 'rb')
    intro_sound = open("dyin_livin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # play both sounds for start of scene
    sound.play(intro_sound)
    time.sleep(2.0)
    sound.play(music_sound)

    # set the background to the 0 image from image bank
    # the size will be (10x8 tiles of sixe 16x16)
    background = stage.Grid(image_bank_background,
                            constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            tile_picked = random.randint(3, 14)
            background.tile(x_location, y_location, tile_picked)

    # a sprite that will update every frame with te background
    ship = stage.Sprite(image_bank_sprites, 4,  75, 66)

    # list of aliens to have more than 1
    aliens = []
    for alien_number in range(constants.TOTAL_NUMBER_OF_ALIENS_lvl_2):
        a_single_alien = stage.Sprite(image_bank_sprites, 9, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        aliens.append(a_single_alien)

    # call alien function to display
    show_alien()
    # create a list for the laser to shoot
    lasers = []
    for laser_number in range(constants.TOTAL_NUMBER_OF_LASERS_lvl_2):
        a_single_laser = stage.Sprite(image_bank_sprites, 12, constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        lasers.append(a_single_laser)

    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = [score_text, lives_text, high_score_text] + lasers + [ship] + aliens + [background]

    # render the sprites
    # render the game scene once per scene
    game.render_block()

    # a forever loop
    while True:
        # get the user input
        keys = ugame.buttons.get_pressed()

        # take player to win scene when score is 25
        if score == 25:
            time.sleep(3.0)
            win_scene(score)


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

       # check if B button is being pressed
        if keys & ugame.K_X != 0:
            if b_button == constants.button_state["button_up"]:
                # change to just pressed
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
                # speed boost
                ship_speed += 1
        else:
            # check if state is still pressed
            if b_button == constants.button_state["button_still_pressed"]:
                # set speed back to normal
                b_button = constants.button_state["button_released"]
                # ship speed normal
                ship_speed -= 1
            else:
                # else change state to button back up again
                b_button = constants.button_state["button_up"]

        if keys & ugame.K_START != 0:
            Pass

        # mute when SELECT button is pressed
        if keys & ugame.K_SELECT != 0:
            if is_muted == True:
                ugame.audio.mute(False)
                is_muted = False
            else:
                ugame.audio.mute(True)
                is_muted = True

   
        # move ship across y and x with wrap and borders
        if keys & ugame.K_RIGHT:
            if ship.x <= constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(ship.x + ship_speed, ship.y)
            else:
                ship.move(0, ship.y)
        if keys & ugame.K_LEFT:
            if ship.x >= 0:
                ship.move(ship.x - ship_speed, ship.y)
            else:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
        if keys & ugame.K_UP:
            if ship.y >= 0:
                ship.move(ship.x, ship.y - ship_speed)
            else:
                ship.move(ship.x, 0)
        if keys & ugame.K_DOWN:
            if ship.y <= 120:
                ship.move(ship.x, ship.y + ship_speed)
            else:
                ship.move(ship.x, 120)

        # update the logic of the game
        # play gun sound when button pressed
        if a_button == constants.button_state["button_just_pressed"]:
            for laser_number in range(len(lasers)):
                if lasers[laser_number].x < 0:
                    lasers[laser_number].move(ship.x, ship.y)
                    sound.play(gun_sound)
                    Break

        # each frame to move lasers that has shot
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                lasers[laser_number].move(lasers[laser_number].x, lasers[laser_number].y - constants.LASER_SPEED)
                if lasers[laser_number].y < constants.OFF_TOP_SCREEN:
                    lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # when alien goes under the screen 
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                aliens[alien_number].move(aliens[alien_number].x, aliens[alien_number].y + constants.ALIEN_SPEED)
                if aliens[alien_number].y > constants.SCREEN_Y:
                    aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_alien()
                    score -= 1
                    if score < 0:
                        score = 0
                    score_text.clear()
                    score_text.cursor(0,0)
                    score_text.move(1,1)
                    score_text.text(f"Score: {score}")
        
        # within the same function, in the collision detection block
        for laser_number in range(len(lasers)):
            if lasers[laser_number].x > 0:
                for alien_number in range(len(aliens)):
                    if aliens[alien_number].x > 0:
                        if stage.collide(lasers[laser_number].x, lasers[laser_number].y,
                                        lasers[laser_number].x + 16, lasers[laser_number].y +16,
                                        aliens[alien_number].x, aliens[alien_number].y,
                                        aliens[alien_number].x +16, aliens[alien_number].y +16):
                            # alien was hit
                            aliens[alien_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            lasers[laser_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(alien_death_sound)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0,0)
                            score_text.move(1,1)
                            score_text.text(f"Score: {score}")
                            if score > high_score:
                                high_score = score
                                high_score_text.clear()
                                high_score_text.cursor(0,0)
                                high_score_text.move(1,120)
                                high_score_text.text(f"High Score: {high_score}")
                            show_alien()
                            show_alien()

         # collision between ship and alien
        for alien_number in range(len(aliens)):
            if aliens[alien_number].x > 0:
                if stage.collide(aliens[alien_number].x + 1, aliens[alien_number].y,
                                 aliens[alien_number].x + 15, aliens[alien_number].y + 15,
                                 ship.x, ship.y,
                                 ship.x + 15, ship.y + 15):
                    # When alien hits ship
                    sound.stop()
                    sound.play(lives_lost_sound)
                    # Deduct 2 lives
                    lives -= 2
                    lives_text.clear()
                    lives_text.cursor(0, 0)
                    lives_text.move(89, 1)
                    lives_text.text(f"Lives: {lives}")
                    if lives == 0:
                        time.sleep(3.0)
                        game_over_scene(score, high_score)
                    else:
                        time.sleep(3.0)
                        # reset postion of the ship position to a proper place
                        ship.move(constants.SCREEN_X // 2, constants.SCREEN_Y - constants.SPRITE_SIZE)

        # only refresh the sprite
        game.render_sprites(lasers + [ship] + aliens)
        game.tick()

def game_over_scene(final_score, high_score):
    # the game over function
    # image bank
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # image 0 is background
    background = stage.Grid(image_bank_2,
                            constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    
    # text to display
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(22,20)
    text1.text("Final score: {:0>2d} \nHigh Score: {:0>2d}".format(final_score, high_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(43,60)
    text2.text("GAME OVER")
    text.append(text2)

    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)
    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = text + [background]

    # render the sprites and background
    # render the game scene once per scene
    game.render_block()

    # forever loop
    while True:
        # user input
        keys = ugame.buttons.get_pressed()

        # Check if the SELECT button is pressed
        if keys & ugame.K_SELECT != 0:
            # reload the program (restart the game)
            supervisor.reload()
        # Update logic of the game and wait for refresh
        game.tick()

def win_scene(final_score):
    # the win scene function
    # play win music sound for win
    music_sound = open("good_bad_ugly.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(music_sound)

    # image bank
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")
    # image 0 is background
    background = stage.Grid(image_bank_2,
                            constants.SCREEN_GRID_X,
                            constants.SCREEN_GRID_Y)
    
    # text to display
    text = []
    text1 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text1.move(22,20)
    text1.text("Final score: {:0>2d}".format(final_score))
    text.append(text1)

    text2 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text2.move(45,60)
    text2.text("You Win")
    text.append(text2)

    text3 = stage.Text(width=29, height=12, font=None, palette=constants.RED_PALETTE, buffer=None)
    text3.move(32,110)
    text3.text("PRESS SELECT")
    text.append(text3)

    # create the stage for the background to show
    # frames at 60 fps
    game = stage.Stage(ugame.display, constants.FPS)

    # set the layers, so the item show up in order
    game.layers = text + [background]

    # render the sprites and background
    # render the game scene once per scene
    game.render_block()
    # forever loop
    while True:
        # user input
        keys = ugame.buttons.get_pressed() 
        # Check if the SELECT button is pressed
        if keys & ugame.K_SELECT != 0:
            # Reload the program (restart the game)
            supervisor.reload()
        # Update logic of the game and wait for refresh
        game.tick()

# global variable mute to pass between functions
is_muted = False

# call splash scene first
if __name__ == "__main__":
    splash_scene()