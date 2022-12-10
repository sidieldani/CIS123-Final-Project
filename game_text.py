import time
import requests

# Naming conventions:
# The game will progress in layers, and functions in this file will be named after the layer where they'll be called.
# The player will need to pass through layer A to get to B, B to get to C, etc. Functions in the A layer will be
# encountered as soon as the game starts.The B layer functions refer to character creation. C layer functions take place
# in the game's 'hub', which is where the meat of the game takes place. The D layer represents the end, and it's where
# the game checks if the player has all the requirements to finish the game.

def save_game(player_info):
    f = open('savefile.txt', 'w')
    f.write(player_info.save_info)

def a0_init_location():     #Player class starts in this false location
    return

def a1_title_screen():
    # Display game logo
    # "wow that logo is ridiculously big", yeah, nothing I can do about that. if it was any smaller it would be hard(er)
    # to read the ASCII art.

    big_ass_title = '''                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                        ~!7!7777!~^      .:~!77??7!~.        .^!!7???7~:     :!!!77.  :!!777..~!77?^   .^~!!7!77:                                                       
                                                       .!!?JJJJJJY5J^  .^!7?JJJJJJJYY7.    :!7??JJJJJJYYJ^   :!7J55. ^!7Y5Y: .!!?5P~  :!7?JJJJ5P^                                                       
                                                       .!!?557~!!7J5Y..!77JYY?!!!77?Y5Y^  ^!7?YY?!!!!77J557  :!!J5Y.^!7Y5?.  .!!?55^  ~!7J5J7!!7:                                                       
                                                       .!!?5P!:!!7J5Y.~!7J5Y^    .~!7Y5J :!!?55!     ^!!J55^ :!!J5Y!!7Y57    .!!?55^  ~!7J5Y!!!!                                                        
                                                       .!!?557!7?YY?: ~!7Y5?      ^!!J55.:!!J55:     .!!?5P! :!!J5Y!!7Y57    .!!?55^  ~!7JYJJJYY                                                        
                                                       .!!?557!!J55~  ^!!J557:...^!!?Y5? .!!?Y5J^...:!!7J5Y: :!!J5Y:~!7Y57   .!!?55^  ~!755?^^^^                                                        
                                                       .!!?5P!^!!J55^  ^!7?JYY?????JY5?.  :!77JYYJ?????Y5Y^  :!!J5Y..!!?Y57  .!!?55^  ^!7JYJ??JY:                                                       
                                                       .!7?Y5! ^!?J5Y:  .~!7??JJJJYJ7^      ^!7??JJJJJJ?~.   :7?J5Y. .!7JY57 .!7?Y5~   ^!7??JJY5:                                                       
                                                        :^^^^:  :^^^^:     .^^~~~^:.          .:^~~~~^.      .^^^^^   .^^^^^. :^^^^.     .:^^^^^.                                                       
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                  ..                   ..         ..            ...              ...                                 ..                                    ..                                           
              :~!7????7:            :~7??J~   .~!7????!.    :~!7????7^      .^!77????7~:      :~!7777?!          :~!7????~.   ~777?^  ^77777777!~:     :~!7????7^ .~7777777777??. .^~!7777?^            
            .~77JJJ??J55~         .~77?JYP7  ~77JJJ??J5Y~  ~77?JJ??J55!   .~77?JJJJ?JJYY?:   ~7??JJJYPJ        .~77JJJ??Y5Y^ .!!?5P~  ~!7JJJJJ?J5Y!  .~77JJJ??J55~ !7JJJ?JJJJJ55..!7?JJJJYP~            
            ^!!J5Y~!!7Y5J         ^!7?Y5?~^ ^!!J5Y~~!!J55.:!!J5Y!~!!J55. :!7?YYJ!~~~77?Y5Y: :!!?Y5?!!!~        ~!7Y5J^!!7Y5Y .!!?55~  ~!7Y5?^~!!?5P^ ^!!J5Y~!!7Y5J.~!!!7!?5Y7!!! ^!!J5Y7!!7^            
            ^!7YPJ ^!!J5Y.        ^!!?557   ^!7Y5J^!77Y5Y.:!!J5Y :!!J55: ~!7Y5J.    :!7!!7~ :!!?Y5?!7?^        ~!75P7~!7?YPJ .!!?55~  ~!7YP?^~!!J55^ ^!7YPJ ^!!J5Y.   .!!?55:    ^!7JYY777?.            
            ^!7YYJJ!!!J5Y.         ^!7?Y57  ^!7Y5J~7JYY?: ^!!J5YJ!!!J55: !!?5P7      ~7777! :!!?YJJ?J5~        ~!7Y5?!7JYY7. .!!?55~  ~!7Y5J!!?Y5?^  ^!7YYJJ!!!J5Y.   .!!?55:    ^!7JYJJ?Y5.            
            ^!7YJY5!!!J5Y.       ..:!!7J55: ^!7Y5J^~~^.   ^!!JJJ57!!J55: ^!7J5Y!:..:~!7J55~ :!!J5Y~^^~:        ~!7Y57^~~^.   .!!?55~  ~!7Y5?~!7557   ^!7YJY5!!!J5Y.   .!!?55:    ^!7Y5J~^^~.            
            ^!7Y5J^^!!J5Y.       ^7777?Y5J  ^!7YPJ        ^!!Y5Y^^!!J55:  ^!7?JYJ?????J5Y~  .!!?YJJ?JY?        ~!75P7        .!!?5P~  ~!7YP?.!!?557  ^!7Y5J^^!!J5Y.   .!!?55:    :!!?YJ??J5~            
            ~7?J5J ^7?JYY.       ^7?JJYJ!.  ^7?J5J        ^7?JYY .7?JY5:   .~!7??JJJJJJ!:    .~7????J5?        ~7?J57        .!7?Y5~  ~7?J5? :!7JY5~ ~7?J5? ^7?JYY.   .!7JY5:     :!7????Y5~            
            .::::: .:::::        .:^^^:     .:::::        .:::::  :::::       .:^^^^^.         ..::::::        .::::.         :::::.  .:::::  .::::: .::::: .:::::     :::::.       ..:::::.            
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                           ...              ....    ....                                  ....                         .....                                                            
                                        :~7?JY? .!7??J^   ^!7?JJ?^:~7?JJJ!.  .!7??J^ !7??J^ :!7??J.   .^!7??JJJ7^  ~77?????????J:   :~!7??JJ?7~.     !7???????7~.                                       
                                       ~77?JY5J .!!?5P~  ~!7JJJ?YY7?J???YP?  .!!?5P^ !!?5P~ :!!J55.  .!7?JJJ??J55~ ~7?JJ??JJJJ5P^ ^!7?JJJJ???J5Y7.  .!!?YJJJ??J5Y~                                      
                                      :!!?Y5J~^ .!!?5P~ .!!?557~!?J5J~!!J55. .!!?55^ !!?5P~ :!!J55.  ^!7J5J^~!7YPJ ^~~~7!?557~~!.^!7JYY?~^^~77?Y5J. .!!?557^~!!J55.                                     
                                      .!!?Y5J.  .!!?5P~ .!!?5P^^!7YP?:!!J55. .!!?55^ !!?5P~ :!!J55.  ~!7YP? ^!!Y5Y     ~!?5P~   .!!?55!     :!!?5P! .!!?557^!!7Y5J.                                     
                                       :!!?Y5Y. .!!?5P~ .!!?5P~^!7YP?:!!J55. .!!?55^ !!?5P~ :!!J55.  ~!7YYJJ~!!Y5Y    .!!?5P~   :!!?55^     .!!?YP7 .!!?557!!JYY7.                                      
                                     .::~!7J5P~ .!!?5P~ .!!?5P~^!7YP?:!!J55. .!!?55!:!!?5P~ :!!J55!^.~!7YJY5!!!Y5Y    .!!?5P~    ~!7J5Y!:::^!!7J5Y: .!!?557!!?55!                                       
                                     :77???Y5Y. .!!?5P~ .!!?5P~^!7YP?:!!J55.  ~!7JYJ?7?Y5J.  ~!7JJ55:^!7YP?:^!!YPY    .!!?5P~    .~!7?JYJJ???JY5J:  .!!?5P!:!!?55~                                      
                                     :!7JJJJ!.  .!7?J5~ .!7?J5~^7?JY?:7??YY.   ^!7??JJJJ!.    ^!7?J5:~7?JY? ^7?JYJ     !7?J5~      .~!7??JJJJJ7^     !7?J5~ :!?JYY^                                     
                                      ::^^:      .:..:.  .:..:..:.... .:...      .:^^:.         ...: .:.... .::...     .:..:.         .::^^:..       .:....  .:..:.                                     
                                                                                                                                                                                                                                                                                                                                                                                                                
                                                                                                                                                                                                        '''
    print(big_ass_title)
    return


def a2_main_menu():
    # Ask for new game, load game, or quit

    player_choice = ''
    player_options = '''Input the letter in parenthesis to pick a path. You can always press (q) to quit. 
    (a)New Game
    (b)Load Game
    (q)Quit
    '''
    print(player_options)
    player_choice = str(input('Please input your choice: '))
    while player_choice != 'a' and player_choice != 'b' and player_choice != 'q':  # confirm correct input
        print('Invalid input. Please input your choice as a lowercase character:', end=' ')
        player_choice = str(input())

    return player_choice


def b1_new_game():
    # get player name, origin story
    # output opening text, then return first, last, and origin
    # The options are: (A) A free ship (B) Your brother as a crew member (C) increased base stats.

    first_name = ''
    last_name = ''
    player_origin = ''
    intro_joke = requests.get("https://official-joke-api.appspot.com/random_joke")
    text1 = f'''\t\tWelcome, landlubber, to Rookie! A Space Pirate Simulator. You are about to embark on a journey to become 
    a space pirate captain - if you can make it out of the spaceport, that is. Be warned, it is not every freebooter 
    that gets to wear the captain's hat, and you are much more likely to perish than to succeed on your first journey. 
    But failure is nothing but an opportunity to learn, and while you may fail on your mission, others might succeed by 
    remembering your mistakes.
    Before beginning the game, here's a random joke to fill my API requirement for this project: 
    {intro_joke.json()}
    \tWith that out of the way, you must now create your character. What is your name, landlubber?'''
    print(text1)

    first_name = input('First name: ')
    while first_name.isalpha() == False:  # ensures string only has letters
        first_name = input('Sorry, only letters allowed! Try again: ')

    if first_name == 'q':
        quit()
    last_name = input('Last name: ')
    while last_name.isalpha() == False:  # ensures string only has letters
        last_name = input('Sorry, only letters allowed! Try again: ')
    if last_name == 'q':
        quit()

    text2 = f'''\t\tYour name is {first_name}. You were born 18 years ago to this very day, to the {last_name} family of space 
    pirates. When you were but a wee child, a terrible tragedy befell your parents. You were accompanying them as they 
    ran errands to prepare for an expedition, when suddenly, space barracudas attacked! Your parents never stood a 
    chance, but you managed to escape unscathed.'''
    print(text2)

    while player_origin != 'a' and player_origin != 'b' and player_origin != 'c' and player_origin != 'q':
        player_origin = str(input('What saved you? (a) A rival pirate (b) My sneaky brother (c) My robotic legs: '))
        if player_origin == 'q':
            quit()
        if player_origin != 'a' and player_origin != 'b' and player_origin != 'c':
            print('Invalid input. Please input the character a, b, or c to show your choice.')

    print('From this point, you can enter the letter "s" to save your character information at any time.')

    return first_name, last_name, player_origin


def b2_ship(first_name):
    # output ship origin story, ask player if they wish to change their last name to Butterbean or not.

    change_lname = False
    text1 = f'''\t\tDeath by space barracuda is a tale all too common in the ports of the Void Sea. Luckily, it was not your tale (yet).
    Just before certain doom, a rival space pirate swooped in with his crew! Captain Fewhairs Butterbean drove the 
    barracudas away with a barrage of laser cannonballs, and although he was too late to save your family, he did manage
    to rescue you. 
    \tCaptain Fewhairs raised you, and taught you everything you know about space piracy. Piloting, history, flag 
    etiquette, the best torrent websites, he taught you all of it. Somewhere along the line, he made you an offer: 
    Abandon your family's name, and become {first_name} Butterbean, heir to the Butterbean Pirates'''
    print(text1)

    player_choice = str(input("Did you take his offer? (a) Yes (b) No: "))
    while player_choice != 'a' and player_choice != 'b' and player_choice != 'q':  # confirm correct input
        if player_choice == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice = str(input("Did you take his offer? (a) Yes (b) No: "))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice = str(input("Did you take his offer? (a) Yes (b) No: "))

    if player_choice == 'q':
        quit()
    elif player_choice == 'a':
        change_lname = True

    text2 = '''\t\tAlas, like all good things, the life of the Butterbean Pirates eventually came to an end. Just as a space elephant
    never forgets, a space barracuda never forgives. The school of giant space fish ambushed Captain Fewhairs on his 
    last expedition before retirement, and took their revenge upon him and his entire crew! There were no survivors. 
    \tRegardless of your earlier choice, Captain Fewhairs saw you as his progeny. Although most of his belongings became
    barracuda food, he did leave you with his old reserve ship, the Barracuda's Folly. It was old, rusty, depressurized,
    and lacking a crew, but it was your last reminder of a once great pirate. To you, that made it perfect. To everyone
    else, it looked like it would blow into a million pieces the second it heard the word "takeoff".
    
    SHIP GAINED!'''
    print(text2)

    return change_lname


def b3_brother(last_name):
    # print brother origin story
    # Player gains a first mate crew member.

    text1 = f'''\t\tDeath by space barracuda is a tale all too common in the ports of the Void Sea. Luckily, fate had other plans for
    you and your brother. While your parents were running errands, your brother, Peet {last_name}, sneaked you off to 
    watch a fight in the local neighborhood thunderdome. When news came of another space barracuda attack, the two of 
    you thought nothing of it. That is, until the wreckage of the family ship showed up in the holo-news.
    \tThis was years ago. The two of you have spent the time since living in the streets, first scavenging and begging, 
    then picking pockets and robbing sailors, all in preparation to one day follow in the steps of your parents, and
    become truly great space pirates. People in this spaceport might know and fear the {last_name} brothers, but that's
    not enough for the two of you. You want the whole galaxy to know your names!
    \tAnd all you need to make all those dreams come true, is a ship. And a crew. Maybe an eye-patch or a peg-leg wouldn't hurt.
    
    CREW MEMBER GAINED! - FIRST MATE'''

    return


def b4_stats():
    # print stats origin story, no input/output required.
    # Player gains +1 to mental and physical stats.

    text1 = '''\t\tIn the olden days, when pirates would hop on pieces of wood and float on water like primitives, being born without 
    legs was a death sentence. Lucky for you, you live in a far-out sci-fi future. And here, not having legs means 
    having robot legs, and robot legs are awesome. 
    \tWhen space barracudas attacked, you ran, and you ran fast. While the space barracudas could not hope to possibly catch 
    up to you, your family did not have such a great exit strategy. They were chased down and turned to fish food, while
    you looked on hopelessly, unable to share the power of your robot legs.
    \tSince that day, you swore never to run from danger again. You spent your life tinkering with your robot legs, making
    them faster, stronger, more durable, smarter. That's right, smarter, you installed an auxiliary brain right in your 
    thighs, to help you think. You did all of this so that one day you could become a space pirate like your parents, 
    and get revenge upon barracuda-kind. 
    \tToday is that day. You feel like your legs are as great as they'll ever be. You feel readier than ever to become a space 
    pirate, and all that you need is a ship. And a crew. Maybe an eyepatch?
    
    STATS GAINED!'''
    print(text1)

    return


def c1_world_hub():
    text1 = f'''\t\tThere are many places that you will need to visit before you are ready for takeoff. In order to successfully take
    flight and become a prestigious space pirate, you will need the following:
    A ship
    A pilot, first mate, quartermaster, and mechanic
    At least 1 body health (BH) and 1 mind health (MH) point left
    
    When you feel that you are ready, simply (t)ake off, and see how you did. Now, pick a location to visit:
    (a) Cantina
    (b) Shipyard
    (c) Recruitment Office
    (t) Take Off'''
    print(text1)
    player_choice = str(input())
    while player_choice != 'a' and player_choice != 'b' and player_choice != 'c' and player_choice != 't' and player_choice != 'q':  # confirm correct input
        if player_choice == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice = str(input('''(a) Cantina
            (b) Shipyard
            (c) Recruitment Office
            (t) Take Off'''))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice = str(input('''(a) Cantina
            (b) Shipyard
            (c) Recruitment Office
            (t) Take Off'''))
    if player_choice == 'q':
        quit()

    return player_choice


def c2_cantina():
    # Opportunities:
    # Stare-down with old pirate captain. LOSE 2 MH, GAIN 1 MH, GAIN SHIP

    text1 = 'Placeholder text: Lose 1 MH point and gain ship? (a) Yes (b) No'
    print(text1)
    player_choice = str(input())
    while player_choice != 'a' and player_choice != 'b' and player_choice != 'q':  # confirm correct input
        if player_choice == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice = str(input("Placeholder text: Lose 1 MH point and gain ship? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice = str(input("Placeholder text: Lose 1 MH point and gain ship? (a) Yes (b) No"))
    if player_choice == 'q':
        quit()
    elif player_choice == 'a':
        print('1 MH LOST! SHIP GAINED!')
        return True
    return False


def c3_shipyard():
    # Opportunities:
    # Steal a ship, lose 2 BH.
    # Hire mechanic

    text1 = 'Placeholder text: Lose 2 BH and gain ship? (a) Yes (b) No'
    print(text1)
    player_choice1 = str(input())
    while player_choice1 != 'a' and player_choice1 != 'b' and player_choice1 != 'q':  # confirm correct input
        if player_choice1 == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice1 = str(input("Placeholder text: Lose 2 BH and gain ship? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice1 = str(input("Placeholder text: Lose 2 BH and gain ship? (a) Yes (b) No"))
    if player_choice1 == 'q':
        quit()

    text2 = 'Placeholder text: Hire Mechanic? (a) Yes (b) No'
    print(text2)
    player_choice2 = str(input())
    while player_choice2 != 'a' and player_choice2 != 'b' and player_choice2 != 'q':  # confirm correct input
        if player_choice2 == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice2 = str(input("Placeholder text: Hire Mechanic? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice2 = str(input("Placeholder text: Hire Mechanic? (a) Yes (b) No"))
    if player_choice2 == 'q':
        quit()

    return player_choice1, player_choice2


def c4_recruitment_office():
    # Opportunities:
    # Hire pilot, first mate, quartermaster, and mechanic
    # This location was meant to be several locations, with interesting events attached to them, but due to
    # time constraints on my part I'm lumping them all together. This way I can deliver a working project on time.

    text1 = 'Placeholder text: Hire Pilot? (a) Yes (b) No'
    text2 = 'Placeholder text: Hire First Mate? (a) Yes (b) No'
    text3 = 'Placeholder text: Hire Quartermaster? (a) Yes (b) No'
    text4 = 'Placeholder text: Hire Mechanic? (a) Yes (b) No'

    print(text1)
    player_choice1 = str(input())
    while player_choice1 != 'a' and player_choice1 != 'b' and player_choice1 != 'q':  # confirm correct input
        if player_choice1 == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice1 = str(input("Placeholder text: Hire Pilot? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice1 = str(input("Placeholder text: Hire Pilot? (a) Yes (b) No"))
    if player_choice1 == 'q':
        quit()

    print(text2)
    player_choice2 = str(input())
    while player_choice2 != 'a' and player_choice2 != 'b' and player_choice2 != 'q':  # confirm correct input
        if player_choice2 == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice2 = str(input("Placeholder text: Hire First Mate? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice2 = str(input("Placeholder text: Hire First Mate? (a) Yes (b) No"))
    if player_choice2 == 'q':
        quit()

    print(text3)
    player_choice3 = str(input())
    while player_choice3 != 'a' and player_choice3 != 'b' and player_choice3 != 'q':  # confirm correct input
        if player_choice3 == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice3 = str(input("Placeholder text: Hire Quartermaster? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice3 = str(input("Placeholder text: Hire Quartermaster? (a) Yes (b) No"))
    if player_choice3 == 'q':
        quit()

    print(text4)
    player_choice4 = str(input())
    while player_choice4 != 'a' and player_choice4 != 'b' and player_choice4 != 'q':  # confirm correct input
        if player_choice4 == 's':
            save_game(main.player_info)
            print('Game Saved')
            player_choice4 = str(input("Placeholder text: Hire Mechanic? (a) Yes (b) No"))
        else:
            print('Invalid input. Please input an appropriate character to show your choice.')
            player_choice4 = str(input("Placeholder text: Hire Mechanic? (a) Yes (b) No"))
    if player_choice4 == 'q':
        quit()

    return player_choice1, player_choice2, player_choice3, player_choice4


def d1_takeoff(player_class):
    # checks if the player class has all contents necessary to take off.
    # If the player meets all the requirements, they win the game. Otherwise, it's game over.
    print('You are about to take off towards outer space to become a space pirate! Calculating results...')
    print('3...', end=' ')
    time.sleep(1)
    print('2...', end=' ')
    time.sleep(1)
    print('1...', end=' ')
    time.sleep(1)
    if player_class.ship and player_class.crew_fmate and player_class.crew_quartermaster and player_class.crew_mechanic:
        if player_class.body_health >= 1 and player_class.mind_health >= 1:
            print('Congratulations: Due to your wise choices, you have proven yourself a capable space pirate!')
            print('You take off into space with your crew. Who knows what sorts of adventures await?')
            print('Thanks for playing!')
            x = input('Press any key to end game.')
            quit()
        else:
            print('Though you managed to gather a ship and crew, you are too injured to continue! Game Over')
            x = input('Press any key to end game.')
            quit()
    elif player_class.ship:
        print('Although you have a ship, you do not have enough manpower to operate it! Your ship explodes on takeoff.')
        print('Game Over')
        x = input('Press any key to end game.')
        quit()
    else:
        print('It seems like you do not yet have a ship to take off with. Maybe the shipyard or cantina will have one?')
        return

