import random
import requested_info


def roll_dice(values):
    result = ""
    number_of_dices = int(values[0])
    rolls = []
    text = f"You rolled {values[0]}d{values[1]}. "

    if int(values[0]) == 0 or int(values[1]) == 0:
        text += "I'm polite, so I wont tell you how you should use that 0. But try to figure it out yourself."
        return text
    if int(values[0]) > 100:
        text += "I wont roll more then 100 dices. You do it."
        return text

    for n in range(number_of_dices):
        roll = random.randint(1, int(values[1]))
        rolls.append(roll)
    for number in rolls:
        result += f"{number},  "
    text += f" Your rolls are:  {result} \n"
    if int(values[1]) == 20 and int(values[0]) > 1:
        text += f"Best: {max(rolls)}, worst: {min(rolls)}"
    elif int(values[0]) == 4 and int(values[1]) == 6:
        text += f"Total is: {sum(rolls)}. Best 3 rolls sum is {sum(rolls)-min(rolls)}"
    elif int(values[0]) > 1:
        text += f"Total is: {sum(rolls)}, Best: {max(rolls)}, worst: {min(rolls)}"
    return text


def commands(processed):
    if processed == "armors" or processed == "armor":
        return requested_info.armor()
    if processed == "condition" or processed == "conditions":
        return requested_info.conditions()
    if processed == "weapon" or processed == "weapons":
        return requested_info.weapon()
    if "spells" in processed:
        return requested_info.spells(processed)
    elif "spell" in processed:
        return requested_info.spell(processed)
    if 'scrap' in processed:
        return requested_info.scrap()


def get_response(message: str):
    processed: str = message.lower()
    if processed[0] == "/":
        return commands(processed[1:])
    if processed == "d":
        return roll_dice([1, 20])
    if processed == "dd":
        return roll_dice([2, 20])
    if processed == "help":
        return generate_help()

    if 'd' in processed:
        parts = processed.split("d")
        if not len(parts) == 2:
            return None
        if parts[0] == "":
            parts[0] = "1"
        if parts[1].isdigit() and parts[0].isdigit():
            return roll_dice(parts)
        else:
            return None
    else:
        return None


def generate_help():
    list_commands = "Below is the list of my commands: \n \n"
    list_commands += "x and y means any positive integer number in this examples \n"
    command_data = {
        "xdy": "Rolls x dices with y sided",
        "dy": "Rolls 1 dice with y sides",
        "d": "Rolls 1d20",
        "dd": "Rolls 2d20",
        "/armors": "Gives list of armors",
        "/armor": "Same as above(/armors)",
        "/conditions": "Gives a list of conditions",
        "/condition": "Same as above(/condition)",
        "/weapons": "Gives list of weapons",
        "weapon": "Same as above(/weapons)",
        "other": "You also can just type number of valid dices to roll and I will roll if i will understand you. For example 3d12"
    }
    for key, value in command_data.items():
        list_commands += f"{key}: {value} \n"



