import game_text
import gamestate_class

def save_game(player_info):
    f = open('savefile.txt', 'w')
    f.write(player_info.save_info)

game_start = game_text.a1_title_screen()

player_info = gamestate_class.Game_state()  # initialize class that stores player info
a2_choice = game_text.a2_main_menu()

if a2_choice == 'a':  # if player selects 'new game'
    player_info.first_name, player_info.last_name, b1_choice = game_text.b1_new_game()
    if b1_choice == 'a':        #run backstory A
        b2_choice = game_text.b2_ship(player_info.first_name)
        if b2_choice:
            player_info.last_name = 'Butterbean'  # replaces player last name with their adoptive parent
            player_info.ship = True
    elif b1_choice == 'b':      #run backstory B
        b3_choice = game_text.b3_brother(player_info.last_name)
        player_info.crew_fmate = True
    elif b1_choice == 'c':      #run backstory C
        b4_choice = game_text.b4_stats()
        player_info.mind_health = 4
        player_info.body_health = 4

    c1_choice = game_text.c1_world_hub()
    while True: # infinite world hub loop. Can be ended with 'q', or by finishing the game.


        if c1_choice == 'a':  # run the cantina scenario
            c2_choice = game_text.c2_cantina()
            if c2_choice:
                player_info.mind_health -= 1
                player_info.ship = True

        elif c1_choice == 'b':  # run the shipyard scenario
            c3_choice1, c3_choice2 = game_text.c3_shipyard()
            if c3_choice1 == 'a':
                player_info.body_health -= 2
                player_info.ship = True
            if c3_choice2 == 'a':
                player_info.crew_mechanic = True

        elif c1_choice == 'c':  # run the recruitment office scenario
            c4_choice1, c4_choice2, c4_choice3, c4_choice4 = game_text.c4_recruitment_office()
            if c4_choice1 == 'a':
                player_info.crew_pilot = True
            if c4_choice2 == 'a':
                player_info.crew_fmate = True
            if c4_choice3 == 'a':
                player_info.crew_quartermaster = True
            if c4_choice4 == 'a':
                player_info.crew_mechanic = True

        elif c1_choice == 't':
            game_text.d1_takeoff(player_info)
        c1_choice = game_text.c1_world_hub()
elif a2_choice == 'b':
    save_game(player_info)