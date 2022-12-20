from combat import *
from players import *

def precision_debuff(combat : Combat, player: Player):
    if combat.player1_in_combat == player:
        combat.player2_in_combat.epsilon /= 100
        combat.player2_states.append("Precision Debuff")
    else:
        combat.player1_in_combat.epsilon /= 100
        combat.player1_states.append("Lower Precision")

def precision_buff(combat : Combat, player: Player):
    if combat.player1_in_combat == player:
        combat.player1_in_combat.epsilon *= 100
        combat.player1_states.append("Precision Buff")
    else:
        combat.player2_in_combat.epsilon *= 100
        combat.player2_states.append("Precision Buff")

def heal(combat: Combat, player:Player):
    if combat.player1_in_combat == player:
        combat.player1_in_combat.life += 18
        combat.player1_states.append("Healed")
    else:
        combat.player2_in_combat.life += 18
        combat.player2_states.append("Healed")

def increase_damage(combat: Combat, player:Player):
    if combat.player1_in_combat == player:
        combat.player1_in_combat.damage += combat.player1_in_combat.damage/2
        combat.player1_states.append("Increased Damage")
    else:
        combat.player2_in_combat.damage += combat.player2_in_combat.damage/2
        combat.player2_states.append("Increased Damage")

def decrease_damage(combat: Combat, player: Player):
    if combat.player1_in_combat == player:
        combat.player2_in_combat.damage = combat.player2_in_combat.damage/2
        combat.player2_states.append("Decreased Damage")
    else:
        combat.player1_in_combat.damage = combat.player1_in_combat.damage/2
        combat.player1_states.append("Decreased Damage")

def culling_blade(combat: Combat, player: Player):
    if combat.player1_in_combat == player:
        combat.player1_states.append("Culling Blade")
    else:
        combat.player2_states.append("Culling Blade")



