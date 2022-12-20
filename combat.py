import keyboard
import time
import random
from players import *
from trivia import generate_trivia
import functions


class Combat:
    def __init__ (self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2
        self.player1_in_combat = player1.Clone()
        self.player2_in_combat = player2.Clone()
        self.turn = 0
        self.player1_states = []
        self.player2_states = []
        self.end = False
        self.winner = None

    def get_answer(self, player, start_time, solution):
        actual_time = time.time()
        while time.time() - actual_time < 30:
            if solution == input():
                return player
            else:
                wrong = True
                print(f"Wrong answer, now {self.player2_in_combat.name if player == self.player1_in_combat else self.player1_in_combat.name} can answer it in {300 - (time.time() - start_time) if 300 - (time.time() - start_time) > 0 else 30} seconds")   
                break
        if not wrong:
            print(f"Time over. Now {self.player2_in_combat.name if player == self.player1_in_combat else self.player1_in_combat.name} can answer it in {300 - (time.time() - start_time) if 300 - (time.time() - start_time) > 0 else 30} seconds")
        left_time = 300 - (time.time() - start_time) if 300 - (time.time() - start_time) > 0 else 30
        actual_time = time.time()
        while time.time() - actual_time < left_time:
            if solution == input():
                return self.player1_in_combat if player == self.player2_in_combat else self.player2_in_combat
            else:
                print("Wrong answer too. Now a random player will attack first")
                return random.choice([self.player1_in_combat,self.player2_in_combat])
        print("Time over. Now a random player will attack first")
        return random.choice([self.player1_in_combat,self.player2_in_combat])

    def play(self): #TODO: Needs to return winner and loser
        while not self.end:
            print(f"{self.player1_in_combat.name}, what armor do you like to use?")

            for i in range(len(self.player1_in_combat.armors)): #TODO: Only show armors in your current level
                if self.player1_in_combat.armors[i][2]>self.player1_in_combat.level:
                    break
                print(f"{i} : {self.player1_in_combat.armors[i][1]}")
                max_selection=i
            while True:
                armor_selection = int(input())
                if armor_selection > max_selection:
                    print("Invalid Input")
                else:
                    break
            self.player1_armor = self.player1_in_combat.armors[armor_selection][0]

            print(f"{self.player2_in_combat.name}, what armor do you like to use?")

            for i in range(len(self.player2_in_combat.armors)):
                if self.player2_in_combat.armors[i][2]>self.player2_in_combat.level:
                    break
                print(f"{i} : {self.player2_in_combat.armors[i][1]}")
                max_selection = i
            while True:
                armor_selection = int(input())
                if armor_selection > max_selection:
                    print("Invalid Input")
                else:
                    break
            self.player2_armor = self.player2_in_combat.armors[armor_selection][0]

            first_one_to_attack = None
            trivia = generate_trivia()
            print(trivia[0])
            start_time = time.time()
            print(f"Players have 5 minutes to solve the trivia problem. To answer the question {self.player1_in_combat.name} must have to press the key 'A' and {self.player2_in_combat.name} the key 'L',\n the first one to get the correct answer will attack first")

            while True:
                if keyboard.is_pressed('a'): 
                    print(f"{self.player1_in_combat.name} has 30 seconds to write the answer")
                    first_one_to_attack = self.get_answer(self.player1_in_combat,start_time,trivia[1])
                    break
                if keyboard.is_pressed('l'):
                    print(f"{self.player2_in_combat.name} has 30 seconds to write the answer")
                    first_one_to_attack = self.get_answer(self.player2_in_combat,start_time,trivia[1])
                    break
                if time.time() - start_time > 300:
                    print("Now a random player will atack first")
                    first_one_to_attack = random.choice([self.player1_in_combat, self.player2_in_combat])
                    break
            self.playTurn(first_one_to_attack)
            if not self.end:
                if self.player1_in_combat == first_one_to_attack:
                    self.playTurn(self.player2_in_combat)
                else:
                    self.playTurn(self.player1_in_combat)
        return self.winner


    def calculateDamage(self, player : Player, attack_selected):
        if player == self.player1_in_combat:
            toprint, armor_value = player.attacks[attack_selected][0](self.player2_armor,player.epsilon,player.damage)
            print(f"The zero founded was {toprint}. \nIt was founded in {armor_value} steps.")
            damage = player.damage- armor_value
            print(f"The attack caused a damage of {damage}")
        else:
            toprint, armor_value = player.attacks[attack_selected][0](self.player1_armor,player.epsilon,player.damage)
            print(f"The zero founded was {toprint}. \nIt was founded in {armor_value} steps.")
            damage = player.damage- armor_value
            print(f"The attack caused a damage of {damage}")
        return damage

    def playTurn(self, player : Player):
        print(f"{player.name}'s states:\n Life: {player.life}\n Damage: {player.damage}\n Epsilon: {player.epsilon}")
        if player == self.player1_in_combat:
            print(self.player1_states)
            print(f"{self.player2_in_combat.name}'s states:\n Life: {self.player2_in_combat.life}\n Damage: {self.player2_in_combat.damage}\n Epsilon: {self.player2_in_combat.epsilon}")
            print(self.player2_states)
        else:
            print(self.player2_states)
            print(f"{self.player1_in_combat.name}'s states:\n Life: {self.player1_in_combat.life}\n Damage: {self.player1_in_combat.damage}\n Epsilon: {self.player1_in_combat.epsilon}")
            print(self.player2_states)
        action = input(f"Is the turn of {player.name}\nWhat do you like to do? \nAttack(1) \nUse Skill(2)")


        if action == '1':
            print('Select your attack. Select 0 to return')
            for i in range(len(player.attacks)):
                if player.attacks[i][2] > player.level:
                    break
                print(f"{i+1}) {player.attacks[i][1]}")
                max_selection=i+1
            while True:
                attack_selection = int(input())
                if attack_selection > max_selection:
                    print("Invalid Input")
                else:
                    break
            if attack_selection == 0:
                return self.playTurn(player)
            else:
                damage = self.calculateDamage(player, attack_selection-1)
                if self.player1_in_combat == player:
                    self.player2_in_combat.life = self.player2_in_combat.life - damage
                    if self.player2_in_combat.life<=0:
                        self.end = True
                        self.winner = self.player1
                        print(f"That was an epic combat! {player.name} has emerged victorious")
                else:
                    self.player1_in_combat.life = self.player1_in_combat.life - damage
                    if self.player1_in_combat.life <= 0:
                        self.end = True
                        self.winner = self.player2
                        print(f"That was an epic combat! {player.name} has emerged victorious")                      

        elif action == '2':
            print('Select your skill. Select 0 to return')
            for i in range(len(player.skills)):
                if player.skill[i][2] > player.level:
                    break
                print(f"{i+1}) {player.skills[i][1]}")
                max_selection=i+1
            while True:
                skill_selection = input()
                if skill_selection > max_selection:
                    print("Invalid Input")
                else:
                    break
            if skill_selection == 0:
                return self.playTurn(self, player)
            else:
                player.skills[skill_selection-1][0](self,player)
            
            print("Now you most attack")

            print('Select your attack.')
            for i in range(len(player.attacks)):
                if player.attacks[i][2] > player.level:
                    break
                print(f"{i+1}) {player.attacks[i][1]}")
                max_selection=i+1
            while True:
                attack_selection = input()
                if attack_selection > max_selection:
                    print("Invalid Input")
                else:
                    break

            damage = self.calculateDamage(self, player, attack_selection-1)
            if self.player1 == player:
                self.player2_in_combat.life = self.player2_in_combat.life - damage
                if self.player2_in_combat.life<0:
                    self.end = True
                    self.winner = self.player1
                    print(f"That was an epic combat! {player.name} has emerged victorious")
            else:
                self.player1_in_combat.life = self.player1_in_combat.life - damage
                if self.player1_in_combat.life < 0:
                    self.end = True
                    self.winner = self.player2
                    print(f"That was an epic combat! {player.name} has emerged victorious")



        else:
            print('Invalid input')
            return self.playTurn(self, player)