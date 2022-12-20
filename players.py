from functions import *
from armors import *

class Player:

    def __init__(self, name, armors, skills, level, epsilon, life, damage, attacks, experiencie, experience_threshold):
        self.name = name
        self.armors = armors
        self.skills = skills
        self.level = level
        self.epsilon = epsilon
        self.life = life
        self.damage = damage
        self.attacks = attacks
        self.experience = experiencie
        self.experience_threshold = experience_threshold
        
    def Clone (self):
        return Player(self.name, self.armors, self.skills, self.level, self.epsilon, self.life, self.damage, self.attacks, self.experience, self. experience_threshold)

    def get_exp(self, experience_gained): #TODO: Check max level index
        self.experience = self.experience + experience_gained
        for i in range (len(self.experience_threshold)):
            if self.experience>self.experience_threshold[i]:
                self.level = i+1
                break

class Warrior(Player):
    
    def __init__(self, name):
        self.name=name
        self.armors = [(f1,"y=x^2",1), (f2, "y=x^3",1)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-3
        self.life = 9
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 3, 8, 15, 25]

    def __str__(self) -> str:
        return f"Warrior of level {self.level}"

class Rogue(Player):

    def __init__(self, name):
        self.name=name
        self.armors = [(f1,"y=x^2",1), (f2, "y=x^3",1)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-3
        self.life = 25
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 3, 8, 15, 25]

    def __str__(self) -> str:
        return f"Rogue of level {self.level}"

class Wizard(Player):
    def __init__(self, name):
        self.name=name
        self.armors = [(f1,"y=x^2",1), (f2, "y=x^3",1)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-3
        self.life = 25
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 3, 8, 15, 25]

    def __str__(self) -> str:
        return f"Wizard of level {self.level}"

        

    
