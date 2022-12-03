class Player:
    experience_threshold = () #Rellenar en algun punto

    name = ''

    armors = []

    skills = []

    __level = 1

    epsilon = 1e-2

    @property
    def life(self):
        raise NotImplementedError()

    @property
    def damage(self):
        raise NotImplementedError()

    @property
    def level(self):
        return self.__level

    @property
    def attacks(self):
        raise NotImplementedError()

    @property
    def experience(self):
        raise NotImplementedError()

    def level_up(self):
        self.__level += 1

    


class Warrior(Player):
    pass

class Rogue(Player):
    pass

class Wizard(Player):
    pass
        

    
