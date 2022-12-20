import functions

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

    


class Warrior(Player):
    pass

class Rogue(Player):
    pass

class Wizard(Player):
    pass
        

    
