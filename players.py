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

    def get_exp(self, experience_gained): #TODO: Check max level index, gain stats per level
        self.experience = self.experience + experience_gained
        for i in range (len(self.experience_threshold)):
            if self.experience>self.experience_threshold[i]:
                self.level = i+1

class Warrior(Player):
    
    def __init__(self, name):
        self.name=name
        self.armors = [(f1,"y=x^2",1), (f2, "y=x^3",1), (f5,"x^3 + 4",2), (f8,"x^2 - 5",3), (f9,"x^2 + x - 1",5), (f10,"x^2 + x - 4",8), (f14,"x^3 - 8",11), (f19,"x^3 + x^2 + x + 1",15)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-5
        self.life = 25
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 1, 2, 4, 6, 8, 11, 14, 17, 20, 24, 28, 32, 36, 40 ]

    def __str__(self) -> str:
        return f"Warrior of level {self.level}"

class Rogue(Player):

    def __init__(self, name):
        self.name=name
        self.armors = [(f1,"y=x^2",1), (f2, "y=x^3",1), (f8,"x^2 - 5",2), (f12,"x^2 + 3x - 2",4), (f13,"2x^2 + 4x - 8",5), (f14,"x^3 - 8",8), (f16, "x^3 + x^2 + 1",11), (f18,"x^3 + x^2 + x - 8",15)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-2
        self.life = 18
        self.damage = 6
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 1, 2, 4, 6, 8, 11, 14, 17, 20, 24, 28, 32, 36, 40 ]

    def __str__(self) -> str:
        return f"Rogue of level {self.level}"

class Wizard(Player):
    def __init__(self, name):
        self.name=name
        self.armors = [(f1,"y=x^2",1), (f2, "y=x^3",1), (f5,"x^3 + 4",2), (f9,"x^2 + x - 1",4), (f11,"x^2 + x - 3",6), (f16, "x^3 + x^2 + 1",8), (f17,"x^3 + x^2 - 4",12), (f20,"3x^3 + 2x^2 + 4x + 1",15)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-4
        self.life = 10
        self.damage = 8
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1), (secant, "Secant", 5), (regulaFalsiHamming, "Hamming Regula Falsi", 11)]
        self.experience = 0
        self.experience_threshold = [0, 1, 2, 4, 6, 8, 11, 14, 17, 20, 24, 28, 32, 36, 40 ]

    def __str__(self) -> str:
        return f"Wizard of level {self.level}"

        

    
