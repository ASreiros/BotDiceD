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


def spells(processed):
    spell_level = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    spells_list = processed.split()
    if len(spells_list) == 1 and spells_list[0] == "spells":
        spells_text = generate_spells_list('', '', 1, '')
        return spells_text
    elif len(spells_list) == 2 and spells_list[0] == "spells" and spells_list[1] in spell_level:
        spells_text = generate_spells_list('', spells_list[1], 1, '')
        return spells_text


def spell(processed):
    spell_list = processed.split()
    if len(spell_list) == 1 and spell_list[0] == "spell":
        return "Please name a spell you need. For example /spell Fireball"
    elif len(spell_list) > 1 and spell_list[0] == "spell":
        spell_name = processed[6:].capitalize()
        slug_list = spell_name.split()
        slug = ""
        for word in slug_list:
            slug += f'{word.lower()}-'
        slug = slug[:-1]
        print("slug:", slug)
        return get_spell(slug, top=True)
    else:
        return "Check def spell"

def generate_spells_list(text, lvl, page, letter):
    URL = f"https://api.open5e.com/v1/spells/?document__slug=wotc-srd&page={page}&spell_level={lvl}"
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
        return None
    else:
        try:
            spells_text = text
            for spell in data['results']:
                if spell['name'][0] is not letter:
                    letter = spell['name'][0]
                    spells_text += f'\n \n {letter} \n'
                spells_text += f" {spell['name']}  |"
        except Exception as e:
            print("error:", e)
            return None
        else:
            if data['next']:
                page += 1
                spells_text = generate_spells_list(spells_text, lvl, page, letter)
                return spells_text
            else:
                return spells_text

def get_spell(name, top):
    SPELL_URL = f"https://api.open5e.com/v1/spells/?document__slug=wotc-srd&slug={name}"
    try:
        response = requests.get(url=SPELL_URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
        return "Something wrong with spell"
    else:
        text = ""
        if int(data.get('count', 0)) == 0:
            if top:
                return get_similar_spells(name=name, page=1, text='', counter=0)
            else:
                return ""
        else:
            text = ""
            result = data.get("results", [])
            print(data)
            for spell_name in result:
                text += f'**{spell_name.get("name", "Noname")}** '
                text += f'({spell_name.get("spell_level", "10")} lvl) \n'
                text += f'Components: {spell_name.get("components", "")}'
                if spell_name.get('requires_verbal_components', False):
                    text += f' ({spell_name.get("material", "")})'
                text += f'\n Casting time: {spell_name.get("casting_time", "noinfo")}, '
                text += f'Ritual: {spell_name.get("ritual", "noinfo")}, '
                text += f'Duration: {spell_name.get("duration", "0")}, '
                text += f'Range: {spell_name.get("range", "0")} \n \n'
                text += f'Description: {spell_name.get("desc", "")} \n'
                text += f'Higher lvl: {spell_name.get("higher_level", "no info")} Page:{spell_name.get("page", "")} \n'
            return text



def get_similar_spells(name, page, text, counter):
    URL = f"https://api.open5e.com/v1/spells/?document__slug=wotc-srd&page={page}"
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
        return "Something went wrong"
    else:
        try:
            spells_text = text
            for spell in data['results']:
                slug = spell.get('slug', "")
                if name in slug:
                    counter += 1
                    spells_text += f"\n {get_spell(name=slug, top=False)} \n"
                    spells_text += "-------------------------------------------------------------------------- \n"
        except Exception as e:
            print("error:", e)
            return None
        else:
            if counter > 4:
                spells_text += f" \n More then 5 spells found. Only first 5 shown. Please enter more precise input if your spell is not in the list. \n"
                return spells_text
            if data['next']:
                page += 1
                spells_text = get_similar_spells(name=name, page=page, text=spells_text, counter=counter)
                return spells_text
            else:
                return spells_text



