import requests



def weapon():
    info = ""
    categories = ['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shield']
    category = ""
    URL = 'https://api.open5e.com/v1/weapons/?format=json'
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
        return None
    else:
        try:
            info = ""
            category = ""
            print(data)
            for weapon_piece in data['results']:
                if weapon_piece['document__slug'] == 'wotc-srd':
                    if not weapon_piece['category'] == category:
                        category = weapon_piece['category']
                        info += f'\n\n------------ {category} ----------------------\n\n'
                    info += f"{weapon_piece['name']} | Dmg:{weapon_piece['damage_dice']} {weapon_piece['damage_type']} | Cost:{weapon_piece['cost']}"
                    if weapon_piece['properties']:
                        if len(weapon_piece['properties']) > 0:
                            info += "  |Properties: "
                            for prop in weapon_piece['properties']:
                                info += f"{prop}, "
                    info += "\n"
                    info += "----------------------------------------------\n"
            #         if armor_piece['category'] in categories:
            #             if not armor_piece['category'] == category:
            #                 category = armor_piece['category']
            #                 info += f'--- {category} --- \n'
            #             info += f"{armor_piece['name'] if len(armor_piece['name']) > 12 else armor_piece['name'].ljust(22, ' ')}| AC:{armor_piece['ac_string'] if len(armor_piece['ac_string'])> 15 else armor_piece['ac_string'].ljust(45)}|Cost:{armor_piece['cost'].ljust(10, ' ')}| STR: {'-' if not armor_piece['strength_requirement'] else armor_piece['strength_requirement']}|  {'-' if armor_piece['stealth_disadvantage'] else 'Disadvantage'} \n \n"
        except Exception as e:
            print("error:", e)
            return None
        else:
            return info


def armor():
    # info = "Armor	                    Armor Class (AC)                 Cost	Strength	Stealth	 \n"
    # categories = ['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shield']
    # category = ""
    # URL = 'https://api.open5e.com/v1/armor/?format=json'
    # try:
    #     response = requests.get(url=URL)
    #     response.raise_for_status()
    #     data = response.json()
    # except Exception as e:
    #     print(e)
    #     return None
    # else:
    #     try:
    #         for armor_piece in data['results']:
    #             if armor_piece['document__slug'] == 'wotc-srd':
    #                 if armor_piece['category'] in categories:
    #                     if not armor_piece['category'] == category:
    #                         category = armor_piece['category']
    #                         info += f'--- {category} --- \n'
    #                     info += f"{armor_piece['name'] if len(armor_piece['name']) > 12 else armor_piece['name'].ljust(22, ' ')}| AC:{armor_piece['ac_string'] if len(armor_piece['ac_string'])> 15 else armor_piece['ac_string'].ljust(45)}|Cost:{armor_piece['cost'].ljust(10, ' ')}| STR: {'-' if not armor_piece['strength_requirement'] else armor_piece['strength_requirement']}|  {'-' if armor_piece['stealth_disadvantage'] else 'Disadvantage'} \n \n"
    #
    #     except Exception as e:
    #         print("error:", e)
    #         return None
    #     else:
    #         print(info)

    info = """
|---------------------------------------------------------------------------|    
|    Armor	               |  Armor Class (AC)  |  Cost	               |Strength| Stealth|
|------------------------------- Light Armor ------------------------------|
|Padded                    | AC:11 + Dex                | Cost:5 gp           | STR: -     |  -         |
|Leather                    | AC:11 + Dex               | Cost:10 gp          | STR: -     |Dis       |
|Studded Leather  | AC:12 + Dex               | Cost:45 gp         | STR: -     | Dis      |
|------------------------------ Medium Armor ----------------------------|
|Hide                          | AC:12 + Dex(max 2) | Cost:10 gp         | STR: -     | Dis      |
|Chain Shirt             | AC:13 + Dex(max 2) | Cost:50 gp         | STR: -    | Dis      |
|Scale mail               | AC:14 + Dex(max 2) | Cost:50 gp         | STR: -    |  -         |
|Breastplate            | AC:14 + Dex(max 2) | Cost:400 gp      | STR: -     | Dis     |
|Half plate                | AC:15 + Dex(max 2) | Cost:750 gp       | STR: -    |  -         | 
|-------------------------------- Heavy Armor ----------------------------|
|Ring mail                 | AC:14                            | Cost:30 gp       | STR: -    | Dis      |
|Chain mail               | AC:16                            | Cost:75 gp       | STR: 13  | Dis      |
|Splint                       | AC:17                             | Cost:200 gp     | STR: 15 | Dis      |
|Plate                        | AC:18                             | Cost:1500 gp   | STR: 15 | Dis      |
|----------------------------------- Shield  -------------------------------|
|Shield                       | AC:  +2                          | Cost:10 gp       | STR: -    |  Dis     |
|--------------------------------------------------------------------------|
    """
    print(len(info))
    return info


def conditions():
    URL = "https://api.open5e.com/v1/conditions/?format=json"
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
        return None
    else:
        try:
            print(data)
            print("results: ", data['results'])
            condition_text = ""
            for condition in data['results']:
                condition_text += f"{condition['name']}: \n {condition['desc']}  \n\n"
        except Exception as e:
            print("error:", e)
            return None
        else:
            return condition_text
