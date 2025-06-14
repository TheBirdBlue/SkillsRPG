#!/usr/bin/python

import time
import os
import sys
import random

sys.path.insert(0, "./modules")
sys.path.insert(1, "./saves")
sys.path.insert(2, "./system")

import common
import saveload
import battle
import skills
from flavor import flavor_list

# Main TODO LIST
# 1 - Link to workshop module
# 2 - Link to training module
# 3 - Create and link to player save file for current inventory

class playerStatsClass():

    def calculate_level(self, exp, level):
        exp_to_level = level * 10
        if exp >= exp_to_level:
            exp -= exp_to_level
            level += 1
            self.calculate_level(exp, level)

            return level

        else:
            return level

    def equip_items(self, equipped_list, req_type):
        # Iterate through equipped and look for item type to be stored
        for item in equipped_list:
            if item["TYPE"] in req_type:
                return_item = {
                    "NAME": item["NAME"],
                    "TYPE": item["TYPE"],
                    "SKILL": item["SKILL"],
                    "LEVEL": int(item["LEVEL"]),
                    "ATTACK_PHYSICAL": int(item["ATTACK_PHYSICAL"]),
                    "ATTACK_MAGICAL": int(item["ATTACK_MAGICAL"]),
                    "ATTACK_LUCK": int(item["ATTACK_LUCK"]),
                    "DEFENSE_PHYSICAL": int(item["DEFENSE_PHYSICAL"]),
                    "DEFENSE_MAGICAL": int(item["DEFENSE_MAGICAL"])
                }
            else:
                pass

            if return_item == None:
                return_item = {
                    "NAME": "None",
                    "TYPE": "None",
                    "SKILL": "None",
                    "LEVEL": "None",
                    "ATTACK_PHYSICAL": 0,
                    "ATTACK_MAGICAL": 0,
                    "ATTACK_LUCK": 0,
                    "DEFENSE_PHYSICAL": 0,
                    "DEFENSE_MAGICAL": 0
                }

        return return_item

    def __init__(self, player_stats, warrior_stats, mage_stats, thief_stats, crafting_stats, equipped):
        self.name = player_stats[0]
        self.stat_hp = player_stats[1]
        self.stat_mp = player_stats[2]
        self.stat_tp = player_stats[3]
        self.stat_strength = player_stats[4]
        self.stat_magic = player_stats[5]
        self.stat_luck = player_stats[6]
        self.muns = player_stats[7]
        self.gen_exp = player_stats[8]
        self.highest_floor = player_stats[9]

        # Warrior Stats
        # Fists, Short Swords, Longswords, Axes, Brute Skill
        self.warrior_fist_exp = warrior_stats[0]
        self.warrior_shortsword_exp = warrior_stats[1]
        self.warrior_longsword_exp = warrior_stats[2]
        self.warrior_axe_exp = warrior_stats[3]
        self.warrior_brute_exp = warrior_stats[4]
        self.warrior_fist_lv = self.calculate_level(self.warrior_fist_exp, 0)
        self.warrior_shortsword_lv = self.calculate_level(self.warrior_shortsword_exp, 0)
        self.warrior_longsword_lv = self.calculate_level(self.warrior_longsword_exp, 0)
        self.warrior_axe_lv = self.calculate_level(self.warrior_axe_exp, 0)
        self.warrior_brute_lv = self.calculate_level(self.warrior_brute_exp, 1)
        warrior_level_total = (self.warrior_fist_lv + self.warrior_shortsword_lv + self.warrior_longsword_lv +
                               self.warrior_axe_lv + self.warrior_brute_lv - 5)
        self.warrior_level = self.calculate_level(warrior_level_total, 0)

        # Mage Stats
        # Wands, Staffs, Cards, Arcane, Buffs, Debuffs, Healing
        self.mage_wand_exp = mage_stats[0]
        self.mage_staff_exp = mage_stats[1]
        self.mage_card_exp = mage_stats[2]
        self.mage_arcane_exp = mage_stats[3]
        self.mage_buff_exp = mage_stats[4]
        self.mage_debuff_exp = mage_stats[5]
        self.mage_healing_exp = mage_stats[6]
        self.mage_wand_lv = self.calculate_level(self.mage_wand_exp, 1)
        self.mage_staff_lv = self.calculate_level(self.mage_staff_exp, 1)
        self.mage_card_lv = self.calculate_level(self.mage_card_exp, 1)
        self.mage_arcane_lv = self.calculate_level(self.mage_arcane_exp, 1)
        self.mage_buff_lv = self.calculate_level(self.mage_buff_exp, 1)
        self.mage_debuff_lv = self.calculate_level(self.mage_debuff_exp, 1)
        self.mage_healing_lv = self.calculate_level(self.mage_healing_exp, 1)
        mage_level_total = (self.mage_wand_lv + self.mage_staff_lv + self.mage_card_lv + self.mage_arcane_lv
                            + self.mage_buff_lv + self.mage_debuff_lv + self.mage_healing_lv - 7)
        self.mage_level = self.calculate_level(mage_level_total, 1)

        # Thief Stats
        # Daggers, Pickup, Steal, Stealth, Accuracy, Critical, Recovery
        self.thief_dagger_exp = thief_stats[0]
        self.thief_pickup_exp = thief_stats[1]
        self.thief_steal_exp = thief_stats[2]
        self.thief_stealth_exp = thief_stats[3]
        self.thief_accuracy_exp = thief_stats[4]
        self.thief_critical_exp = thief_stats[5]
        self.thief_recovery_exp = thief_stats[6]
        self.thief_dagger_lv = self.calculate_level(self.thief_dagger_exp, 1)
        self.thief_pickup_lv = self.calculate_level(self.thief_pickup_exp, 1)
        self.thief_steal_lv = self.calculate_level(self.thief_stealth_exp, 1)
        self.thief_stealth_lv = self.calculate_level(self.thief_stealth_exp, 1)
        self.thief_accuracy_lv = self.calculate_level(self.thief_accuracy_exp, 1)
        self.thief_critical_lv = self.calculate_level(self.thief_critical_exp, 1)
        self.thief_recovery_lv = self.calculate_level(self.thief_recovery_exp, 1)
        thief_level_total = (self.thief_dagger_exp + self.thief_pickup_lv + self.thief_steal_lv + self.thief_stealth_lv
                             + self.thief_critical_lv + self.thief_recovery_lv - 7)
        self.thief_level = self.calculate_level(thief_level_total, 1)

        # Crafting Stats
        # Smithing, Runic, Grab Bag
        self.crafting_smithing_exp = crafting_stats[0]
        self.crafting_runic_exp = crafting_stats[1]
        self.crafting_grabbag_exp = crafting_stats[2]
        self.crafting_smithing_lv = self.calculate_level(self.crafting_smithing_exp, 1)
        self.crafting_runic_lv = self.calculate_level(self.crafting_runic_exp, 1)
        self.crafting_grabbag_lv = self.calculate_level(self.crafting_grabbag_exp, 1)
        crafting_level_total = self.crafting_smithing_lv + self.crafting_runic_exp + self.crafting_grabbag_lv - 3
        self.crafting_level = self.calculate_level(crafting_level_total, 1)

        # Player bonus stats and overall level
        # Player level bonuses
        player_level_total = (warrior_level_total + mage_level_total + thief_level_total + self.warrior_level +
                              self.mage_level + self.thief_level)
        self.stat_level = self.calculate_level(player_level_total, 1)

        # Player class level bonuses
        self.bonus_strength = self.warrior_level - 1
        self.bonus_magic = self.mage_level - 1
        self.bonus_luck = self.thief_level - 1

        # Player equipment bonuses
        if equipped == "":
            self.equipped_weapon = {
                    "NAME": "Unarmed",
                    "TYPE": "Fists",
                    "SKILL": "Fists",
                    "LEVEL": "0",
                    "ATTACK_PHYSICAL": 1,
                    "ATTACK_MAGICAL": 0,
                    "ATTACK_LUCK": 0,
                    "DEFENSE_PHYSICAL": 0,
                    "DEFENSE_MAGICAL": 0
                }

            self.equipped_armor_helm = {}
            self.equipped_armor_body = {}
            self.equipped_accessory = {}
            self.bonus_strength_equipment = 1
            self.bonus_magic_equipment = 0
            self.bonus_luck_equipment = 0
            self.armor_physical = 0
            self.armor_magical = 0
            self.skill_bonus = ""

        else:
            weapon_req = ["S.Sword", "L.Sword", "Axe", "Wands", "Staffs", "Cards", "Daggers"]
            accessory_req = ["Necklace", "Ring", "Skill Gem"]
            self.equipped_weapon = self.equip_items(equipped, weapon_req)

            # Check if player has nothing equipped in weapon and sets them to unarmed if nothing equipped
            if self.equipped_weapon["Name"] == "None":
                self.equipped_weapon = {
                    "NAME": "Unarmed",
                    "TYPE": "Fists",
                    "SKILL": "Fists",
                    "LEVEL": "0",
                    "ATTACK_PHYSICAL": 1,
                    "ATTACK_MAGICAL": 0,
                    "ATTACK_LUCK": 0,
                    "DEFENSE_PHYSICAL": 0,
                    "DEFENSE_MAGICAL": 0
                }
            else:
                pass

            self.equipped_armor_helm = self.equip_items(equipped, "Helm")
            self.equipped_armor_body = self.equip_items(equipped, "Body")
            self.equipped_accessory = self.equip_items(equipped, accessory_req)
            self.bonus_strength_equipment = (self.equipped_weapon["ATTACK_PHYSICAL"] +
                                             self.equipped_armor_helm["ATTACK_PHYSICAL"] +
                                             self.equipped_armor_body["ATTACK_PHYSICAL"] +
                                             self.equipped_accessory["ATTACK_PHYSICAL"])
            self.bonus_magic_equipment = (self.equipped_weapon["ATTACK_MAGICAL"] +
                                             self.equipped_armor_helm["ATTACK_MAGICAL"] +
                                             self.equipped_armor_body["ATTACK_MAGICAL"] +
                                             self.equipped_accessory["ATTACK_MAGICAL"])
            self.bonus_luck_equipment = (self.equipped_weapon["ATTACK_LUCK"] +
                                             self.equipped_armor_helm["ATTACK_LUCK"] +
                                             self.equipped_armor_body["ATTACK_LUCK"] +
                                             self.equipped_accessory["ATTACK_LUCK"])
            self.armor_physical = (self.equipped_weapon["DEFENSE_PHYSICAL"] +
                                             self.equipped_armor_helm["DEFENSE_PHYSICAL"] +
                                             self.equipped_armor_body["DEFENSE_PHYSICAL"] +
                                             self.equipped_accessory["DEFENSE_PHYSICAL"])
            self.armor_magical = (self.equipped_weapon["DEFENSE_MAGICAL"] +
                                             self.equipped_armor_helm["DEFENSE_MAGICAL"] +
                                             self.equipped_armor_body["DEFENSE_MAGICAL"] +
                                             self.equipped_accessory["DEFENSE_MAGICAL"])
            self.skill_bonus = self.equipped_accessory["SKILL"]

        # Pull player skills
        self.skills = skills.loadSkills(self.warrior_level, self.mage_level, self.thief_level, self.crafting_level)

def main():
    # Set save file list
    load_names = []
    print(' Please select save name or enter a new name to create a new save;')
    for name in os.listdir("./saves"):
        if ".py" in name or "__pycache__" in name:
            pass
        else:
            load_names.append(name)

    position = 1
    for name in load_names:
        print(f"    {str(position)} - {name}")

    player_input = input(" Select save: ")

    # If save exists
    if player_input in load_names:
        (stats_player, stats_warrior, stats_mage, stats_thief, stats_crafting, equipment)\
            = saveload.loadPlayer(player_input)
        player = playerStatsClass(stats_player, stats_warrior, stats_mage, stats_thief, stats_crafting, equipment)

    # If save is new
    else:
        (stats_player, stats_warrior, stats_mage, stats_thief, stats_crafting, equipment)\
            = saveload.createPlayer(player_input)
        player = playerStatsClass(stats_player, stats_warrior, stats_mage, stats_thief, stats_crafting, "")

    run_game = True

    while run_game:
        common.clear()
        main_lines = [player.name,
                      f"Level: {player.stat_level:2} ║ HP: {player.stat_hp} MP: {player.stat_mp} TP: {player.stat_tp}",
                      f"Str: {player.stat_strength:>3} ({player.bonus_strength:>3})  "
                      f"Eq:({player.bonus_strength_equipment:>3})",
                      f"Mag: {player.stat_magic:>3} ({player.bonus_magic:>3})  Eq:({player.bonus_magic_equipment:>3})",
                      f"Lck: {player.stat_luck:>3} ({player.bonus_luck:>3})  Eq:({player.bonus_luck_equipment:>3})",
                      "", f"Highest Floor: {player.highest_floor}", ""]

        # Set up options and print them to the player
        options = ["To The Tower!", "To The Workshop", "To The Training Grounds", "Rest Yourself (Quit Game)"]
        option_number = 1
        for option in options:
            main_lines.append((f" {str(option_number)} - {option}"))
            option_number += 1

        common.drawUI(player, main_lines, "main")

        # Flavor text
        flavor_pick = random.randrange(0, len(flavor_list))
        print("\n     " + flavor_list[flavor_pick])

        # Pause for player input
        player_options_input = input("\n     What would you like to do? ")

        # Check if player input was a number
        #try:
        player_options = int(player_options_input)

        # Check if player input is a valid number for the number of options
        if player_options <= len(options):
            if player_options == 1:
                player = battle.prepBattleMenu(player)
            elif player_options == 2:
                pass
            elif player_options == 3:
                pass

            # Begin save and quit
            elif player_options == 4:
                player_confirm = input("\n Would you like to save and quit? (Y|N) : ")
                if player_confirm.lower() == "y":
                    # Makes lists to be saved
                    player_stats = [player.name, player.stat_hp, player.stat_mp, player.stat_tp,
                                    player.stat_strength, player.stat_magic, player.stat_luck, player.muns,
                                    player.gen_exp]
                    player_warrior_stats = [player.warrior_shortsword_exp, player.warrior_longsword_exp,
                                            player.warrior_axe_exp, player.warrior_brute_exp]
                    player_mage_stats = [player.mage_wand_exp, player.mage_staff_exp, player.mage_card_exp,
                                         player.mage_arcane_exp, player.mage_buff_exp, player.mage_debuff_exp,
                                         player.mage_healing_exp]
                    player_thief_stats = [player.thief_dagger_exp, player.thief_pickup_exp, player.thief_steal_exp,
                                          player.thief_stealth_exp, player.thief_accuracy_exp,
                                          player.thief_critical_exp, player.thief_recovery_exp]
                    player_crafting_stats = [player.crafting_smithing_exp, player.crafting_runic_exp,
                                             player.crafting_grabbag_exp]
                    all_stats = [player_stats, player_warrior_stats, player_mage_stats, player_thief_stats,
                                 player_crafting_stats]

                    # Saves the lists to the appropriate files
                    saveload.savePlayer(player.name, all_stats)
                    run_game = False
                else:
                    pass
        else:
            print(" That's not a choice. Please select again.")
            time.sleep(2)
        #except:
            #print(" That's not a choice. Please select again.")
            #time.sleep(2)

main()
