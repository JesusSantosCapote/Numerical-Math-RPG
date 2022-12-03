import keyboard
import time
import random
from players import Player

class Combat:
    def __init__ (self, player1:Player, player2:Player):
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
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
            print(f"{self.player1.name}, what armor do you like to use?")

            for i in range(len(self.player1.armors)):
                print(f"{i} : {self.player1.armors[i][1]}")

            player1_armor = self.player1.armors[int(input())]

            print(f"{self.player2.name}, what armor do you like to use?")

            for i in range(len(self.player2.armors)):
                print(f"{i} : {self.player2.armors[i][1]}")

            player2_armor = self.player2.armors[int(input())]
            first_one_to_attack = None
            trivia = generate_trivia()
            print(trivia[0])
            start_time = time.time()
            print(f"Players have 5 minutes to solve the trivia problem. To answer the question {self.player1.name} must have to press the key 'A' and {self.player2.name} the key 'L',\n the first one to get the correct answer will attack first")

            while True:
                if keyboard.is_pressed('a'): 
                    print(f"{self.player1.name} has 30 seconds to write the answer")
                    first_one_to_attack = self.get_answer(self.player1,start_time,trivia[1])
                    break
                if keyboard.is_pressed('l'):
                    print(f"{self.player2.name} has 30 seconds to write the answer")
                    first_one_to_attack = self.get_answer(self.player2,start_time,trivia[1])
                    break
                if time.time() - start_time > 300:
                    print("Now a random player will atack first")
                    first_one_to_attack = random.choice([self.player1, self.player2])
                    break
 

                
                    
                
        

                    



            

    def playTurn(self):
        playerturn = "Player 1" if self.turn % 2 == 0 else "Player2"
        action = input(f"Is the turn of {playerturn}\nWhat do you like to do? \nAttack(1) \nUse Skill(2)" )



# myCombat = Combat(players.Player(), players.Player())
# myCombat.playTurn()
    


a = lambda x: x**2
print(a.__format__())