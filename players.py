class Player:
    experience_threshold = [] # List of int, each position contains experiencie needed to reach index level

    name = '' #string

    armors = [] # List of Tuple: [function, string representation, level needed]

    skills = [] # List of Tuple: [function, string representation, level needed]

    __level = 1

    epsilon = 1e-2

    @property #float
    def life(self):
        raise NotImplementedError()

    @property #float
    def damage(self):
        raise NotImplementedError()

    @property
    def level(self): #int
        return self.__level

    @property
    def attacks(self):  # List of Tuple: [function, string representation, level needed]
        raise NotImplementedError()

    @property
    def experience(self): #int
        raise NotImplementedError()

    def level_up(self):
        self.__level += 1

    


class Warrior(Player):
    pass

class Rogue(Player):
    pass

class Wizard(Player):
    pass
        

    
