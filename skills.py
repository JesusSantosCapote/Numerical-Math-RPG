from Tools import graph_function

def precision_debuff(combat, player):
    if combat.player1_in_combat == player:
        combat.player2_in_combat.epsilon /= 100
        combat.player2_states.append("Precision Debuff")
        combat.player1_in_combat.skills.remove((precision_debuff, "Precision debuffer", 5 ))
    else:
        combat.player1_in_combat.epsilon /= 100
        combat.player1_states.append("Precision Debuff")
        combat.player2_in_combat.skills.remove((precision_debuff, "Precision debuffer", 5 ))


def precision_buff(combat, player):
    if combat.player1_in_combat == player:
        combat.player1_in_combat.epsilon *= 100
        combat.player1_states.append("Precision Buff")
        combat.player1_in_combat.skills.remove((precision_buff, "Precision buffer", 5 ))
        
    else:
        combat.player2_in_combat.epsilon *= 100
        combat.player2_states.append("Precision Buff")
        combat.player2_in_combat.skills.remove((precision_buff, "Precision buffer", 5 ))

def heal(combat, player):
    if combat.player1_in_combat == player:
        combat.player1_in_combat.life += 18
        combat.player1_states.append("Healed")
        combat.player1_in_combat.skills.remove((heal, "Heal", 10 ))
    else:
        combat.player2_in_combat.life += 18
        combat.player2_states.append("Healed")
        combat.player2_in_combat.skills.remove((heal, "Heal", 10 ))

def increase_damage(combat, player):
    if combat.player1_in_combat == player:
        combat.player1_in_combat.damage += combat.player1_in_combat.damage//2
        combat.player1_states.append("Increased Damage")
        combat.player1_in_combat.skills.remove((increase_damage, "Damage Increaser *1.5",5 ))

    else:
        combat.player2_in_combat.damage += combat.player2_in_combat.damage//2
        combat.player2_states.append("Increased Damage")
        combat.player2_in_combat.skills.remove((increase_damage, "Damage Increaser *1.5",5 ))

def decrease_damage(combat, player):
    if combat.player1_in_combat == player:
        combat.player2_in_combat.damage = combat.player2_in_combat.damage//2
        combat.player2_states.append("Decreased Damage")
        combat.player1_in_combat.skills.remove((decrease_damage, "Damage decreaser",10 ))
    else:
        combat.player1_in_combat.damage = combat.player1_in_combat.damage//2
        combat.player1_states.append("Decreased Damage")
        combat.player2_in_combat.skills.remove((decrease_damage, "Damage decreaser",10 ))

def culling_blade(combat, player):
    if combat.player1_in_combat == player:
        combat.player1_states.append("Culling Blade")
        combat.player1_in_combat.skills.remove((culling_blade, "Culling Blade",10 ))

    else:
        combat.player2_states.append("Culling Blade")
        combat.player2_in_combat.skills.remove((culling_blade, "Culling Blade",10 ))

def graphic_vision(combat, player):

    if combat.player1_in_combat == player:
        combat.player1_states.append("Graphic Vision")
        graph_function(combat.player2_armor,range(int(input("Give a range to graph. First extreme:")),int(input("Second extreme:"))),"black")
        combat.player1_in_combat.skills.remove((graphic_vision, "Graphic Vision",12 ))

    else:
        combat.player2_states.append("Graphic Vision")
        graph_function(combat.player1_armor,range(int(input("Give a range to graph. First extreme:")),int(input("Second extreme:"))),"black")
        combat.player2_in_combat.skills.remove((graphic_vision, "Graphic Vision", 12 ))




