import players
class Combat:
    def __init__ (self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 0
        self.end = False
    def playTurn(self):
        playerturn = "Player 1" if self.turn % 2 == 0 else "Player2"
        action = input(f"Is the turn of {playerturn}\nWhat do you like to do? \nAttack(1) \nUse Skill(2)" )



myCombat = Combat(players.Player(), players.Player())
myCombat.playTurn()
    



