import common

# Battle TODO List
# 1 - Calculate enemy power dependant on floor
#       General bonus for every 10 levels on common monsters
#       Bigger bonus if on a 10-floor for boss monsters
# 2 - Take player's highest level and allow choices for every 10 floors as start point
# 3 - On player actions, add exp to appropriate skill
# 4 - Check for skill level up on battle end
#       Check for class level up on battle end
#       Check for player level up on battle end
# 5 - Set checks for player skills to verify what skills can be used
#       Ex; Wands, staffs, and cards allow magic. Swords and axe allow brute skills. Daggers allow steal and stealth
# 6 - Thief skills need to activate when certain criteria happen
#       Pickup; Chance of items when items picked up. Exp on item acquired.
#       Accuracy; Super small boost to critical on regular hit. Exp on successful hit on enemy.
#       Critical; Boost crit damage and gains on landing critical. Exp upon critical hit.
#       Recovery; Chance to recover from miss. Exp upon miss, no recovery success required.

def prepBattleMenu(player):
    choice_menu_options = (" Enter The Tower At Floor 1", "Return")
    choice_menu = True
    choice_number = 1
    lines = []
    for x in choice_menu_options:
        line = f" {choice_number} - {choice_menu_options}"
        lines.append(line)
        choice_number += 1

    common.drawUI(player, lines)

def towerBattle(player):
    pass