import random
import time
import common

# Battle TODO List
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
# 7 - Set up battle requirements (check if player or enemy are out of HP and award extras)
#       Set up turn function (player then enemy)
#       Check player equipment and set up a quick dict for available player skills
#       How to incorporate skill selection into UI? (In block or under block?)
# 8 - On player action, queue exp for when battle is over
#       Level up during run or after run?
# 9 - Set up level up notification for skills, class, and player in character module
#       Relay those into battle to notify player of changes

class enemyStatsClass():

    def __init__(self, floor, base_1=10, base_2=3):

        # Add variation to stats
        def variantStat(self, stat):
            low = int((stat / 4) * -1)
            high = int(stat / 4)

            if low <= 0:
                low = -1
            if high <= 0:
                high = 1
            variant = random.randrange(low, high)
            return variant

        if floor % 10 == 0:
            # Create boss fight, stats
            calc_hp = ((floor * 1.5) * base_1)
            calc_mp = ((floor * 1.1) * base_1)
            calc_tp = ((floor * 1.1) * base_1)
            calc_attack = ((floor * 0.8) * base_2) + base_2
            calc_magic = ((floor * 0.8) * base_2) + base_2
            calc_luck = ((floor * 0.8) * base_2) + base_2
            self.stat_hp = int(variantStat(self, calc_hp) + calc_hp)
            self.stat_mp = int(variantStat(self, calc_mp) + calc_mp)
            self.stat_tp = int(variantStat(self, calc_tp) + calc_tp)
            self.stat_attack = int(variantStat(self, calc_attack) + calc_attack)
            self.stat_magic = int(variantStat(self, calc_magic) + calc_magic)
            self.stat_luck = int(variantStat(self, calc_luck) + calc_luck)

            # Create boss fight, armors
            calc_armor_physical = (floor * 0.2)
            calc_armor_magical = (floor * 0.2)
            self.armor_physical = int(variantStat(self, calc_armor_physical) + calc_armor_physical)
            self.armor_magical = int(variantStat(self, calc_armor_magical) + calc_armor_physical)

            # Ensure that armor is never less than 0
            if self.armor_physical <= 0:
                self.armor_physical = 0
            if self.armor_magical <= 0:
                self.armor_magical = 0

        else:
            # Create regular fight
            calc_hp = ((floor * 0.5) * base_1) + base_1
            calc_mp = ((floor * 0.25) * base_1) + base_1
            calc_tp = ((floor * 0.25) * base_1) + base_1
            calc_attack = ((floor * 0.33) * base_2) + base_2
            calc_magic = ((floor * 0.33) * base_2) + base_2
            calc_luck = ((floor * 0.33) * base_2) + base_2
            self.stat_hp = int(variantStat(self, calc_hp) + calc_hp)
            self.stat_mp = int(variantStat(self, calc_mp) + calc_mp)
            self.stat_tp = int(variantStat(self, calc_tp) + calc_tp)
            self.stat_attack = int(variantStat(self, calc_attack) + calc_attack)
            self.stat_magic = int(variantStat(self, calc_magic) + calc_magic)
            self.stat_luck = int(variantStat(self, calc_luck) + calc_luck)

            # Create boss fight, armors
            calc_armor_physical = (floor * 0.1)
            calc_armor_magical = (floor * 0.1)
            self.armor_physical = int(variantStat(self, calc_armor_physical) + calc_armor_physical)
            self.armor_magical = int(variantStat(self, calc_armor_magical) + calc_armor_physical)

            # Ensure that armor is never less than 0
            if self.armor_physical <= 0:
                self.armor_physical = 0
            if self.armor_magical <= 0:
                self.armor_magical = 0

def prepBattleMenu(player):
    prep_menu = True
    floor_options = []

    # Register floors to start on by finding the ones that evenly divide by 10 but first check if player has cleared
    # at least 10 floors

    if player.highest_floor >= 10:
        for floor_level in range(1, player.highest_floor + 1):
            if floor_level % 10 == 0:
                floor_options.append(str(str(floor_level)))
            else:
                pass
    else:
        pass

    # Add floor options to player options IF they have unlocked a floor with a factor of 10
    if len(floor_options) >= 1:
        choice_menu_options = (" Enter The Tower At Floor 1", " Select a Floor", " Return")

    else:
        choice_menu_options = (" Enter The Tower At Floor 1", " Return")
        choice_menu = True
        choice_number = 1
        lines = []
        for x in choice_menu_options:
            line = f" {choice_number} - {choice_menu_options}"
            lines.append(line)
            choice_number += 1

    to_make_lines = [player.name,
                      f"Level: {player.stat_level:2} ║ HP: {player.stat_hp} MP: {player.stat_mp} TP: {player.stat_tp}",
                      f"Str: {player.stat_strength:>3} ({player.bonus_strength:>3})",
                      f"Mag: {player.stat_magic:>3} ({player.bonus_magic:>3})",
                      f"Lck: {player.stat_luck:>3} ({player.bonus_luck:>3})",
                      "", f"Highest Floor: {player.highest_floor}", ""]

    # Add options to to_make_lines before pushing them to makeLines
    option_number = 1
    for option in choice_menu_options:
        to_make_lines.append(f" {str(option_number)} - {option}")
        option_number += 1

    # Draw the UI
    while prep_menu:
        common.clear()
        common.drawUI(player, to_make_lines, "prep")

        #try:
        player_options = input("\n   What would you like to do? ")
        player_options = int(player_options)

        # Check if player input is a valid number for the number of options
        if player_options - 1 <= len(choice_menu_options):
            if player_options == 1:
                player = towerBattle(player, 1)

            # Sets up for player to either pick floor if option is unlocked ot return to previous menu
            elif player_options == 2:
                if choice_menu_options[1] == " Select a Floor":
                    floor_option_number = 1
                    for nth_floor in floor_options:
                        print(f"        {floor_option_number} - Floor {nth_floor}")
                        floor_option_number += 1
                    player_floor_choice = input("\n     Please select a floor: ")

                    # Check if player input is a valid number for the number of options
                    player_floor_choice = int(player_floor_choice) - 1

                    # If it passes, begin battles at designated floor
                    if player_floor_choice <= len(floor_options):
                        floor = floor_options[player_floor_choice]
                        player = towerBattle(player, floor)

                    # If it fails, go through the loop again
                    else:
                        print(" That's not a valid choice. Please try again.")
                        time.sleep(2)
                else:
                    prep_menu = False
                    return player

            # Aleays send to previous menu
            elif player_options == 3:
                prep_menu = False
                return player

        #except:
        #   print(" That's not a valid choice. Please select again.")
        #   time.sleep(2)

def generateEnemy(floor):
    enemy = enemyStatsClass(floor)
    return enemy

def towerBattle(player, floor):
    # Generate enemy for the floor
    enemy = generateEnemy(floor)

    # Set player's current stats to max stats at beginning of floor
    player_current_hp = player.stat_hp
    player_current_mp = player.stat_mp
    player_current_tp = player.stat_tp

    # Set enemy's current stats to max stats at beginning of floor
    enemy_current_hp = enemy.stat_hp
    enemy_current_mp = enemy.stat_mp
    enemy_current_tp = enemy.stat_tp
    while player_current_hp > 0 and enemy_current_hp > 0:
        player_hp_bar = common.draw_hpmptp_bar(player.stat_hp, player_current_hp, "HP", True)
        player_mp_bar = common.draw_hpmptp_bar(player.stat_mp, player_current_mp, "MP", True)
        player_tp_bar = common.draw_hpmptp_bar(player.stat_tp, player_current_tp, "TP", True)
        enemy_hp_bar = common.draw_hpmptp_bar(enemy.stat_hp, enemy_current_hp, "HP", False)

        tower_battle_lines = ["", "", "", "Enemy Name", enemy_hp_bar, "", "", player.name, player_hp_bar, player_mp_bar,
                              player_tp_bar]
        common.drawUI(player, tower_battle_lines, "battle")
        input("To pause...")
