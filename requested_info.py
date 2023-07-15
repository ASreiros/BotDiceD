import requests

def armor():
    info = "Armor	                    Armor Class (AC)                 Cost	Strength	Stealth	 \n"
    categories = ['Light Armor', 'Medium Armor', 'Heavy Armor', 'Shield']
    category = ""
    URL = 'https://api.open5e.com/v1/armor/?format=json'
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(e)
        return None
    else:
        try:
            for armor_piece in data['results']:
                if armor_piece['document__slug'] == 'wotc-srd':
                    if armor_piece['category'] in categories:
                        if not armor_piece['category'] == category:
                            category = armor_piece['category']
                            info += f'--- {category} --- \n'
                        info += f"{armor_piece['name'] if len(armor_piece['name']) > 12 else armor_piece['name'].ljust(22, ' ')}| AC:{armor_piece['ac_string'] if len(armor_piece['ac_string'])> 15 else armor_piece['ac_string'].ljust(45)}|Cost:{armor_piece['cost'].ljust(10, ' ')}| STR: {'-' if not armor_piece['strength_requirement'] else armor_piece['strength_requirement']}|  {'-' if armor_piece['stealth_disadvantage'] else 'Disadvantage'} \n \n"

        except Exception as e:
            print("error:", e)
            return None
        else:
            return info

