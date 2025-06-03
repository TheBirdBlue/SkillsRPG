import os

def clear():
    if os.name == "posix":
        _ = os.system("clear")
    else:
        _ = os.system("cls")

def numConversion(number):
    try:
        value = int(number)
        value = f"{value:,}"
        return value
    except(ValueError):
        return number

# Inputs options/info/other UI and ensures that 12 lines are available for drawUI()
def makeLines(made_lines):
    return_lines = []
    current_ui_lines = 16

    # If lines are less than 12 long
    if len(made_lines) < current_ui_lines:

        # Add already made options into the return list
        for line in made_lines:
            return_lines.append(line)

        # Add empty spaces for unused lines
        for line in range(len(made_lines), current_ui_lines + 1):
            return_lines.append("")

    # Return the 12 lines back and draw UI
    else:
        return made_lines

    return return_lines

# Draws Player UI
def drawUI(player, lines, mode):

    lines = makeLines(lines)

    def create_exp_bar(exp):

        # Calculate current level and exp required to level
        def calculate_remaining_exp(exp, level):
            exp_to_level = (level) * 10
            if exp >= exp_to_level:
                exp -= exp_to_level
                level += 1
                exp, level = calculate_remaining_exp(exp, level)

                return exp, level

            else:
                return exp, level

        # Calculate leftover and current level to find exp needed to level and set percentage.
        exp_leftover, current_lv = calculate_remaining_exp(exp, 1)
        exp_to_level = current_lv * 10
        exp_percentage = int((exp_leftover / exp_to_level) * 100)

        # Sets first half of exp bar to be full and calculates second half of exp bar accordingly
        if exp_percentage >= 60:
            first_half = "▓▓▓▓"
            second_half = exp_percentage - 60
            if second_half <= 0:
                second_half = ""
            else:
                second_half = int(second_half / 10) * "▓"

        # Sets second half of exp bar as empty and calculates first half accordingly
        elif exp_percentage <= 40:
            second_half = ""
            first_half = exp_percentage
            if first_half <= 0:
                first_half = ""
            else:
                first_half = int(first_half / 10) * "▓"

        else:
            first_half = "▓▓▓▓"
            second_half = ""

        exp_bar_format = f"[{first_half:<4}{exp_percentage:>2}{second_half:<4}]"

        return exp_bar_format


    # Create the exp bars for classes
    warrior_class_exp = int(player.warrior_shortsword_exp + player.warrior_longsword_exp + player.warrior_axe_exp +
                         player.warrior_brute_exp)
    player_warrior_class = create_exp_bar(warrior_class_exp)
    mage_class_exp = int(player.mage_wand_exp + player.mage_staff_exp + player.mage_card_exp + player.mage_arcane_exp +
                      player.mage_buff_exp + player.mage_debuff_exp + player.mage_healing_exp)
    player_mage_class = create_exp_bar(mage_class_exp)
    thief_class_exp = int(player.thief_dagger_exp + player.thief_pickup_exp + player.thief_steal_exp +
                       player.thief_stealth_exp + player.thief_accuracy_exp + player.thief_critical_exp +
                       player.thief_recovery_exp)
    player_thief_class = create_exp_bar(thief_class_exp)
    crafting_class_exp = int(player.crafting_smithing_exp + player.crafting_runic_exp + player.crafting_grabbag_exp)
    player_crafting_class = create_exp_bar(crafting_class_exp)

    # Create the exp bars for warrior skills
    fist = create_exp_bar(player.warrior_fist_exp)
    shortsword = create_exp_bar(player.warrior_shortsword_exp)
    longsword = create_exp_bar(player.warrior_longsword_exp)
    axe = create_exp_bar(player.warrior_axe_exp)
    brute = create_exp_bar(player.warrior_brute_exp)

    # Create the exp bard for mage skills
    wand = create_exp_bar(player.mage_wand_exp)
    staff = create_exp_bar(player.mage_staff_exp)
    card = create_exp_bar(player.mage_staff_exp)
    arcane = create_exp_bar(player.mage_arcane_exp)
    buff = create_exp_bar(player.mage_buff_exp)
    debuff = create_exp_bar(player.mage_debuff_exp)
    healing = create_exp_bar(player.mage_healing_exp)

    # Create the exp bars for thief skills
    dagger = create_exp_bar(player.thief_dagger_exp)
    pickup = create_exp_bar(player.thief_pickup_exp)
    steal = create_exp_bar(player.thief_steal_exp)
    stealth = create_exp_bar(player.thief_steal_exp)
    accuracy = create_exp_bar(player.thief_accuracy_exp)
    critical = create_exp_bar(player.thief_critical_exp)
    recovery = create_exp_bar(player.thief_recovery_exp)

    # Create the exp bars for crafting skills
    smithing = create_exp_bar(player.crafting_smithing_exp)
    runic = create_exp_bar(player.crafting_runic_exp)
    grabbag = create_exp_bar(player.crafting_grabbag_exp)

    # Print skills for the main lines
    warrior_skills_name_line_1 = (f"{"Fists":8} {player.warrior_fist_lv:>3} {"S.Sword":8} "
                                  f"{player.warrior_shortsword_lv:>3} {"L.Sword":8} {player.warrior_longsword_lv:>3} "
                                  f"{"Axe":8} {player.warrior_axe_lv:>3}")
    warrior_skills_expbar_line_1 = f"{fist} {shortsword} {longsword} {axe}"
    warrior_skills_name_line_2 = f"{"Brute":8} {player.warrior_brute_lv:>3} {"":12} {"":12} {"":12}"
    warrior_skills_expbar_line_2 = f"{brute} {"":12} {"":12} {"":12}"

    mage_skills_name_line_1 = (f"{"Wands":8} {player.mage_wand_lv:>3} {"Staffs":8} {player.mage_staff_lv:>3} "
                               f"{"Cards":8} {player.mage_card_lv:>3} {"":8} {"":3}")
    mage_skills_expbar_line_1 = f"{wand} {staff} {card} {"":12}"
    mage_skills_name_line_2 = (f"{"Arcane":8} {player.mage_arcane_lv:>3} {"Buffs":8} {player.mage_buff_lv:>3} "
                               f"{"Debuffs":8} {player.mage_debuff_lv:>3} {"Healing":8} {player.mage_healing_lv:>3}")
    mage_skills_expbar_line_2 = f"{arcane} {buff} {debuff} {healing}"

    thief_skills_name_line_1 =(f"{"Daggers":8} {player.thief_dagger_lv:>3} {"Pickup":8} {player.thief_pickup_lv:>3} "
                               f"{"Steal":8} {player.thief_steal_lv:>3} {"":8} {"":3}")
    thief_skills_expbar_line_1 = f"{dagger} {pickup} {steal} {"":12}"
    thief_skills_name_line_2 = (f"{"Stealth":8} {player.thief_stealth_lv:>3} {"Accuracy":8} "
                                f"{player.thief_accuracy_lv:>3} {"Critical":8} {player.thief_critical_lv:>3} "
                                f"{"Recovery":8} {player.thief_recovery_lv:>3}")
    thief_skills_expbar_line_2 = f"{stealth} {accuracy} {critical} {recovery}"

    crafting_skills_name = (f"{"Smithing":8} {player.crafting_smithing_lv:3} {"Runic":8} {player.crafting_runic_lv:3} "
                            f"{"Grab Bag":8} {player.crafting_grabbag_lv:3} {"":12}")
    crafting_skills_expbar = f"{smithing} {runic} {grabbag} {"":12}"

    # Begin UI lines
    # main_focus sets the "action area" for display to the player
    main_focus = 50

    # Format Line to break up classes in UI
    format_line = f" ║ {{:{main_focus}}} ║ {"═"*13:13} ║ {"═"*51:51} ║"

    line_start = f"\n ╔═{"═"*int(main_focus)}═╦═{"═"*13}═╦═{"═"*51}═╗"
    line_end = f" ╚═{"═"*int(main_focus)}═╩═{"═"*13}═╩═{"═"*51}═╝"

    # Warrior Lines
    line_1 = (f" ║ {lines[0]:{main_focus}} ║"
              f" {"Warrior":9} {player.warrior_level:3} ║ {warrior_skills_name_line_1} ║")
    line_2 = (f" ║ {lines[1]:{main_focus}} ║"
              f" {player_warrior_class:>13} ║ {warrior_skills_expbar_line_1} ║")
    line_3 = (f" ║ {lines[2]:{main_focus}} ║"
              f" {"":>13} ║ {warrior_skills_name_line_2} ║")
    line_4 = (f" ║ {lines[3]:{main_focus}} ║"
              f" {"":>13} ║ {warrior_skills_expbar_line_2} ║")

    # Mage Lines
    if mode == "battle":
        line_5 = (f" ║ {lines[5]:>{main_focus}} ║"
                  f" {"Mage":9} {player.mage_level:3} ║ {mage_skills_name_line_1} ║")
        line_6 = (f" ║ {lines[6]:>{main_focus}} ║"
                  f" {player_mage_class:>13} ║ {mage_skills_expbar_line_1} ║")
    else:
        line_5 = (f" ║ {lines[5]:{main_focus}} ║"
                  f" {"Mage":9} {player.mage_level:3} ║ {mage_skills_name_line_1} ║")
        line_6 = (f" ║ {lines[6]:{main_focus}} ║"
                  f" {player_mage_class:>13} ║ {mage_skills_expbar_line_1} ║")
    line_7 = (f" ║ {lines[7]:{main_focus}} ║"
              f" {"":>13} ║ {mage_skills_name_line_2} ║")
    line_8 = (f" ║ {lines[8]:{main_focus}} ║"
              f" {"":>13} ║ {mage_skills_expbar_line_2} ║")

    # Thief Lines
    line_9 = (f" ║ {lines[10]:{main_focus}} ║"
              f" {"Thief":9} {player.thief_level:3} ║ {thief_skills_name_line_1} ║")
    line_10 = (f" ║ {lines[11]:{main_focus}} ║"
              f" {player_thief_class:>13} ║ {thief_skills_expbar_line_1} ║")
    line_11 = (f" ║ {lines[12]:{main_focus}} ║"
              f" {"":>13} ║ {thief_skills_name_line_2} ║")
    line_12 = (f" ║ {lines[13]:{main_focus}} ║"
              f" {"":>13} ║ {thief_skills_expbar_line_2} ║")

    # Crafting Lines
    line_13 = (f" ║ {lines[15]:{main_focus}} ║"
              f" {"Crafting":>9} {player.crafting_level:3} ║ {crafting_skills_name} ║")
    line_14 = (f" ║ {lines[16]:{main_focus}} ║"
              f" {player_crafting_class:>13} ║ {crafting_skills_expbar} ║")

    # Print UI
    print_order = [line_start, line_1, line_2, line_3, line_4, format_line.format(lines[4]), line_5, line_6,
        line_7, line_8, format_line.format(lines[9]), line_9, line_10, line_11, line_12, format_line.format(lines[14]),
        line_13, line_14, line_end]
    for line in print_order:
        print(line)

def draw_hpmptp_bar(max, current, stat_type, isPlayer):
    # Calculate percent and number of bars needed to draw
    bars_to_draw = int(((current / max) * 200) / 10)
    if bars_to_draw <= 0:
        bars_to_draw = 1
    bars = "▓" * int(bars_to_draw)

    if isPlayer == True:
        bar = f"{stat_type}:   {current:3}/{max:3}   [{bars:<20}]  "
    else:
        bar = f"[{bars:>20}]"

    return bar
