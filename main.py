from players import *
from combat import *
from player_serializer import save_profile, load_profile
import os

end = False
print("Hello welcome to RPG Numerical Math")
while not end:
    print("What do you like to do?\n1)Versus Combat\n2)Create Player")
    action=input()
    saved_profiles = os.listdir("Player_profiles")        

    if action == "1" and len(saved_profiles) >= 2:  

        print("Select first player:")
        for i in range (len(saved_profiles)):
            print(f"{i+1}){saved_profiles[i].split('.')[0]}")
        while True:
            selected_player=int(input())
            if selected_player>0 and selected_player< len(saved_profiles)+1:
                break
            else:
                print("Invalid Input")

        player1=load_profile(saved_profiles[selected_player - 1].split(".")[0])

        print(f"First player selected was {player1.name}, a {player1.__str__()}, with {player1.experience} experience")

        print("Select second player:")

        for i in range (len(saved_profiles)):
            if i == selected_player - 1:
                continue
            print(f"{i+1}){saved_profiles[i].split('.')[0]}")
        
        while True:
            selected_player2=int(input())
            if selected_player2>0 and selected_player2< len(saved_profiles)+1 and selected_player2 != selected_player:
                break
            else:
                print("Invalid Input")
        player2=load_profile(saved_profiles[selected_player2 - 1].split(".")[0])

        print(f"Second player selected was {player2.name}, a {player2.__str__()}, with {player2.experience} experience")

        print("Now lets see an epic numerical math combat")
        combat = Combat(player1, player2)
        winner = combat.play()

        if winner == player1:
            if player1.level < player2.level:
                exp = 1 + ( player2.level - player1.level)*0.5
            else:
                exp = 1/ (1 + (player1.level - player2.level))
            player1.get_exp(exp)
            print(f"{player1.name} has won {exp} points of experience, his current level is {player1.level}")
            save_profile(player1)
        else:
            if player2.level < player1.level:
                exp = 1 + ( player1.level - player2.level)*0.5
            else:
                exp = 1/ (1 + (player1.level - player2.level))
            player2.get_exp(exp)
            print(f"{player2.name} has won {exp} points of experience, his current level is {player2.level}")
            save_profile(player2)
        

    elif action == "1":
        print("There is not even two players saved")

    elif action == "2":
        name = input("Write your Player's name \n")
        while True:
            player_rol=int(input("Select your player's rol:\n1)Warrior\n2)Rogue\n3)Wizard\n"))
            if player_rol>0 and player_rol<4:
                break
            else:
                print("Invalid input.")
        if player_rol == 1:
            new_player= Warrior(name)
            save_profile(new_player)
        elif player_rol ==2:
            new_player= Rogue(name)
            save_profile(new_player)
        elif player_rol ==3:
            new_player= Wizard(name)
            save_profile(new_player)
        

