from functions import *

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
        for i in range (self.experience_threshold):
            if self.experience<self.experience_threshold[i]:
                self.level = i


class Warrior(Player):
    
    def __init__(self, name):
        self.name=name
        self.armors = [(lambda x : x**2,"y=x^2",1), (lambda x : x**3, "y=x^3",1)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-3
        self.life = 25
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 10, 25, 45, 70]





class Rogue(Player):

    def __init__(self, name):
        self.name=name
        self.armors = [(lambda x : x**2,"y=x^2",1), (lambda x : x**3, "y=x^3",1)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-3
        self.life = 25
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 10, 25, 45, 70]


class Wizard(Player):
    def __init__(self, name):
        self.name=name
        self.armors = [(lambda x : x**2,"y=x^2",1), (lambda x : x**3, "y=x^3",1)]
        self.skills = []
        self.level = 1
        self.epsilon = 1e-3
        self.life = 25
        self.damage = 10
        self.attacks = [(bisection, "Bisection", 1), (newton, "Newton", 1)]
        self.experience = 0
        self.experience_threshold = [0, 10, 25, 45, 70]
        

    
