import os


# Writes to file
def write_file(name, load_tuple, file_name):
    file = './saves/' + name + "/" + name + "_" + file_name
    with open(file, 'w') as save:
        for spot in load_tuple:
            save.write(str(spot) + '\n')


# Create player save based on player name input
def createPlayer(name):
    # Create player's general stats
    # Name, HP, MP, TP, Strength, Magic, Luck, Muns, General Experience, Highest Floor
    player_create_order = ["", 10, 10, 10, 5, 5, 5, 0, 0, 0]
    file_location = './saves/' + name
    os.makedirs(file_location)
    player_create_order[0] = name
    write_file(name, player_create_order, "playerSave.txt")

    # Create Warrior skill save
    # Fists, Short Swords, Longswords, Axes, Brute Skill
    warrior_create_order = [0, 0, 0, 0, 0]
    write_file(name, warrior_create_order, "warriorSave.txt")

    # Create Mage skill save
    # Wands, Staffs, Cards, Arcane, Buffs, Debuffs, Healing
    mage_create_order = [0, 0, 0, 0, 0, 0, 0]
    write_file(name, mage_create_order, "mageSave.txt")

    # Create Thief skill save
    # Daggers, Pickup, Steal, Stealth, Accuracy, Critical, Recovery
    thief_create_order = [0, 0, 0, 0, 0, 0, 0]
    write_file(name, thief_create_order, "thiefSave.txt")

    # Create Skills skill save
    # Smithing, Runic, Grab Bag
    crafting_create_order = [0, 0, 0]
    write_file(name, crafting_create_order, "craftingSave.txt")

    # Create starter equipment save
    beginners_shortsword = {
        "NAME": "Beginner's Short Sword",
        "TYPE": "S.Swords",
        "SKILL": "S.Swords",
        "LEVEL": 1,
        "ATTACK_PHYSICAL": 2,
        "ATTACK_MAGICAL": 0,
        "ATTACK_LUCK": 0,
        "DEFENSE_PHYSICAL": 0,
        "DEFENSE_MAGICAL": 0
    }
    beginners_wand = {
        "NAME": "Beginner's Wand",
        "TYPE": "Wands",
        "SKILL": "Wands",
        "LEVEL": 1,
        "ATTACK_PHYSICAL": 0,
        "ATTACK_MAGICAL": 2,
        "ATTACK_LUCK": 0,
        "DEFENSE_PHYSICAL": 0,
        "DEFENSE_MAGICAL": 0
    }
    beginners_dagger = {
        "NAME": "Beginner's Dagger",
        "TYPE": "Daggers",
        "SKILL": "Daggers",
        "LEVEL": 1,
        "ATTACK_PHYSICAL": 0,
        "ATTACK_MAGICAL": 0,
        "ATTACK_LUCK": 2,
        "DEFENSE_PHYSICAL": 0,
        "DEFENSE_MAGICAL": 0
    }

    equipment_create_order = [beginners_shortsword, beginners_wand, beginners_dagger]
    write_file(name, equipment_create_order, "inventorySave.txt")
    write_file(name, "", "equipmentSave.txt")

    return player_create_order, warrior_create_order, mage_create_order, thief_create_order, crafting_create_order, ""


def loadPlayer(name):
    player_load_order = []
    warrior_load_order = []
    mage_load_order = []
    thief_load_order = []
    crafting_load_order = []
    stat_load_order = [player_load_order, warrior_load_order, mage_load_order, thief_load_order, crafting_load_order]
    file_order = ["playerSave.txt", "warriorSave.txt", "mageSave.txt", "thiefSave.txt", "craftingSave.txt"]
    # Iterate through both stat lists and file names to read files and add to lists
    for job, file in zip(stat_load_order, file_order):

        # File name based on player input
        file_location = "./saves/" + name + "/" + name + "_" + file
        with open(file_location, 'r') as save:
            for line in save:

                # Attempts to load line turning it into an int (stats)
                try:
                    line = line.replace("\n", "")
                    line = int(line)
                    job.append(line)

                # Loads line as string should int attempt fail (name)
                except:
                    line = line.replace("\n", "")
                    job.append(line)

    return player_load_order, warrior_load_order, mage_load_order, thief_load_order, crafting_load_order, ""  # Equip


def savePlayer(name, save_lists):
    file_names = ["playerSave.txt", "warriorSave.txt", "mageSave.txt", "thiefSave.txt", "craftingSave.txt"]
    for save, file in zip(save_lists, file_names):
        write_file(name, save, file)
