game_running = True

while game_running == True:
    new_round = True
    player = {'name': "Pratikshya", "attack":10, "health":16, "health": 100}
    monster = {"name": "Aakash", "attack":12, "health":100}

    while new_round == True:

        player_won = False
        monster_won = False

        print("Please select action")
        print('1) Attack')
        print('2) Heal')
        print('3) Exit game')
        player_choice = input()

        if player_choice == '1'or 1:
            monster['health'] = monster['health']-player['attack']
            if monster['health'] <= 0:
                player_won = True
            
            else:
                player['health'] = player['health']-monster['attack']
                if player['health'] <= 0:
                    monster_won = True

                print(monster['health'])
                print(player['health'])

        elif player_choice == '2'or 2: 
            print("heal player")
            
        elif player_choice == '3'or 3:
            new_round = False
            game_running = False

        else:
            print("Invalid Input")

        if player_won == True or monster_won == True: 
            new_round = False


    

    