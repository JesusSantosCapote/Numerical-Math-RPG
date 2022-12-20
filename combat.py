import keyboard
import time
import random
from players import Player
from trivia import generate_trivia
import functions

def to_dict(player):
    player_dict = {}
    player_dict['life'] = player.life
    player_dict['']
    

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

    def get_answer(self, player, start_time, solution):
        actual_time = time.time()
        while time.time() - actual_time < 30:
            if solution == input():
                return player
            else:
                print(f"Wrong answer, now {self.player2.name if player == self.player1 else self.player1.name} can answer it in {300 - time.time() - start_time if 300 - time.time() - start_time > 0 else 30} seconds")   
                break
        print(f"Time over. Now {self.player2.name if player == self.player1 else self.player1.name} can answer it in {300 - time.time() - start_time if 300 - time.time() - start_time > 0 else 30} seconds")
        left_time = 300 - time.time() - start_time if 300 - time.time() - start_time > 0 else 30
        actual_time = time.time()
        while time.time() - actual_time < left_time:
            if solution == input():
                return self.player1 if player == self.player2 else self.player2
            else:
                print("Wrong answer too. Now a random player will attack first")
                return random.choice([self.player1,self.player2])
        print("Time over. Now a random player will attack first")
        return random.choice([self.player1,self.player2])

    def play(self):
        while not self.end:
            print(f"{self.player1_in_combat.name}, what armor do you like to use?")

            for i in range(len(self.player1_in_combat.armors)):
                print(f"{i} : {self.player1_in_combat.armors[i][1]}")

            self.player1_armor = self.player1_in_combat.armors[int(input())]

            print(f"{self.player2_in_combat.name}, what armor do you like to use?")

            for i in range(len(self.player2_in_combat.armors)):
                print(f"{i} : {self.player2_in_combat.armors[i][1]}")

            self.player2_armor = self.player2_in_combat.armors[int(input())]
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
            self.playTurn(self, first_one_to_attack)
            if not self.end:
                if self.player1_in_combat == first_one_to_attack:
                    self.playTurn(self, self.player2_in_combat)
                else:
                    self.playTurn(self, self.player1_in_combat)


    def calculateDamage(self, player : Player, attack_selected): #NOT IMPLEMENTED YET
        if player == self.player1:
            damage = player.attacks[attack_selected](self.player2_armor,player.epsilon)
        else:
            damage = player.attacks[attack_selected](self.player1_armor,player.epsilon)
        return damage

    def playTurn(self, player : Player):
        action = input(f"Is the turn of {player.name}\nWhat do you like to do? \nAttack(1) \nUse Skill(2)")
        print(f"Your stats are:\n Life: {player.life}")


        if action == '1':
            print('Select your attack. Select 0 to return')
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
            if attack_selection == 0:
                return self.playTurn(self, player)
            else:
                damage = self.calculateDamage(self, player, attack_selection-1)
                if self.player1 == player:
                    self.player2_in_combat.life = self.player2_in_combat.life - damage
                    if self.player2_in_combat.life<=0:
                        self.end = True
                else:
                    self.player1_in_combat.life = self.player1_in_combat.life - damage
                    if self.player1_in_combat.life <= 0:
                        self.end = True

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
                player.skills[skill_selection-1](self,player)
            
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
            else:
                self.player1_in_combat.life = self.player1_in_combat.life - damage
                if self.player1_in_combat.life < 0:
                    self.end = True



        else:
            print('Invalid input')
            return self.playTurn(self, player)