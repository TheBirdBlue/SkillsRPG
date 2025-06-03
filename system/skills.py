def loadSkills(lv_warrior, lv_mage, lv_thief, lv_crafting):
    file_order = ("./system/skills_warrior", "./system/skills_mage", "./system/skills_thief",
                  "./system/skills_crafting")
    level_order = (lv_warrior, lv_mage, lv_thief, lv_crafting)

    skill_dict = {}
    skill_index = 0

    # Go through skills info to pull for building character
    for class_level, file in zip(level_order, file_order):

        # Open class skill file
        with open(file, 'r') as skill_file:
            for line in skill_file:

                # Remove description line from checking
                if "##" in line:
                    pass

                else:

                    # Break up line by ","
                    split_line = line.split(",")

                    # Check if available to player
                    if int(split_line[0]) <= class_level:

                        # Add to player's skills if available to the player
                        # Index range is 0 to 5
                        skill_dict[skill_index] = {}
                        skill_dict[skill_index]["SKILL_NAME"] = split_line[1]
                        skill_dict[skill_index]["POWER"] = split_line[2]
                        skill_dict[skill_index]["ELEMENT"] = split_line[3]
                        skill_dict[skill_index]["SKILL"] = split_line[4]
                        # Remove /n from end of line
                        split_line[5] = split_line[5].replace("\n", "")
                        skill_dict[skill_index]["KEYS"] = split_line[5]
                        skill_index += 1

                    else:
                        pass

    return skill_dict
