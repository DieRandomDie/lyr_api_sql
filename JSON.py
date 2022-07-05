import requests
import json
from types import SimpleNamespace


def getApi(key):
    try:
        request = requests.get("https://lyrania.co.uk/api/accounts.php?search="+key)
        request.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise SystemExit(e)
    return request.text


def api_to_object(key):
    json_text = getApi(key).replace(' ', '_').replace('-', '_')
    data = json.loads(json_text, object_hook=lambda d: SimpleNamespace(**d))

    orbs = []
    levels = []
    for index, key in enumerate(vars(data.equipment)):
        orbs.append(key.split("_")[0])
        levels.append(vars(data.equipment)[key])

    data.equipment.shortsword = {'orb': orbs[0], 'level': int(levels[0])}
    data.equipment.dagger = {'orb': orbs[1], 'level': int(levels[1])}
    data.equipment.helmet = {'orb': orbs[2], 'level': int(levels[2])}
    data.equipment.shoulders = {'orb': orbs[3], 'level': int(levels[3])}
    data.equipment.wrist = {'orb': orbs[4], 'level': int(levels[4])}
    data.equipment.gloves = {'orb': orbs[5], 'level': int(levels[5])}
    data.equipment.chestpiece = {'orb': orbs[6], 'level': int(levels[6])}
    data.equipment.leggings = {'orb': orbs[7], 'level': int(levels[7])}
    data.equipment.boots = {'orb': orbs[8], 'level': int(levels[8])}
    # CURRENCY
    data.currency.tokens = int(data.currency.tokens)
    data.currency.bound_tokens = int(data.currency.bound_tokens)
    data.currency.money = data.currency.money.replace('_', ' ')
    data.currency.jade = int(data.currency.jade)
    data.currency.jewel_frags = int(data.currency.jewel_frags)
    data.currency.enchanting_dust = int(data.currency.enchanting_dust)
    data.currency.dungeon_points = int(data.currency.dungeon_points)
    data.currency.diamonds = int(data.currency.diamonds)
    data.currency.rubies = int(data.currency.rubies)
    data.currency.sapphires = int(data.currency.sapphires)
    data.currency.emeralds = int(data.currency.emeralds)
    data.currency.opals = int(data.currency.opals)
    '''
    # GUILD DATA
    data.guild.guild_name
    data.guild.guild_level
    data.guild.weekly_dungeon_points
    
    # JADE BOOSTS
    data.jade_boosts.crit_hit_chance
    data.jade_boosts.crit_hit_damage
    data.jade_boosts.heroism
    data.jade_boosts.leadership
    data.jade_boosts.archaeology
    data.jade_boosts.jewelcrafting
    data.jade_boosts.serendipity
    data.jade_boosts.e_peen
    data.jade_boosts.jade_god
    
    # SIMPLE DATA
    data.id
    data.name
    data.level
    data.current_area
    data.experience
    data.spouse
    data.surname
    data.total_autos
    data.total_kills
    data.total_quests
    data.tradeskills
    
    # STATS
    data.stats.health
    data.stats.attack
    data.stats.defence
    data.stats.accuracy
    data.stats.evasion
    
    # TOKEN BOOSTS
    data.token_boosts.exp_boost
    data.token_boosts.gold_boost
    data.token_boosts.stat_boost
    data.token_boosts.quest_boost
    data.token_boosts.global_boost
    data.token_boosts.health_boost
    data.token_boosts.attack_boost
    data.token_boosts.defence_boost
    data.token_boosts.accuracy_boost
    data.token_boosts.evasion_boost
    data.token_boosts.jack_of_all_jades
    data.token_boosts.dungeon_mastery
    data.token_boosts.areaboss_taxonomy
    data.token_boosts.tradeskill_slots
    data.token_boosts.jewellery_slots
    
    # EQUIPMENT
    data.equipment.shortsword['orb']
    data.equipment.shortsword['level']
    data.equipment.dagger['orb']
    data.equipment.dagger['level']
    data.equipment.helmet['orb']
    data.equipment.helmet['level']
    data.equipment.shoulders['orb']
    data.equipment.shoulders['level']
    data.equipment.wrist['orb']
    data.equipment.wrist['level']
    data.equipment.gloves['orb']
    data.equipment.gloves['level']
    data.equipment.chestpiece['orb']
    data.equipment.chestpiece['level']
    data.equipment.leggings['orb']
    data.equipment.leggings['level']
    data.equipment.boots['orb']
    data.equipment.boots['level']'''

    print(f'data.currency.tokens value: {data.currency.tokens}')
    print(f'data.currency.bound_tokens value: {data.currency.bound_tokens}')
    print(f'data.currency.money value: {data.currency.money}')
    print(f'data.currency.jade value: {data.currency.jade}')
    print(f'data.currency.jewel_frags value: {data.currency.jewel_frags}')
    print(f'data.currency.enchanting_dust value: {data.currency.enchanting_dust}')
    print(f'data.currency.dungeon_points value: {data.currency.dungeon_points}')
    print(f'data.currency.diamonds value: {data.currency.diamonds}')
    print(f'data.currency.rubies value: {data.currency.rubies}')
    print(f'data.currency.sapphires value: {data.currency.sapphires}')
    print(f'data.currency.emeralds value: {data.currency.emeralds}')
    print(f'data.currency.opals value: {data.currency.opals}')
    print(f'data.guild.guild_name value: {data.guild.guild_name}')
    print(f'data.guild.guild_level value: {data.guild.guild_level}')
    print(f'data.guild.guild_weekly_dungeon_points value: {data.guild.weekly_dungeon_points}')
    print(f'data.jade_boosts.crit_hit_chance value: {data.jade_boosts.crit_hit_chance}')
    print(f'data.jade_boosts.crit_hit_damage value: {data.jade_boosts.crit_hit_damage}')
    print(f'data.jade_boosts.heroism value: {data.jade_boosts.heroism}')
    print(f'data.jade_boosts.leadership value: {data.jade_boosts.leadership}')
    print(f'data.jade_boosts.archaeology value: {data.jade_boosts.archaeology}')
    print(f'data.jade_boosts.jewelcrafting value: {data.jade_boosts.jewelcrafting}')
    print(f'data.jade_boosts.serendipity value: {data.jade_boosts.serendipity}')
    print(f'data.jade_boosts.e_peen value: {data.jade_boosts.e_peen}')
    print(f'data.jade_boosts.jade_god value: {data.jade_boosts.jade_god}')
    print(f'data.id value: {data.id}')
    print(f'data.name value: {data.name}')
    print(f'data.level value: {data.level}')
    print(f'data.current_area value: {data.current_area}')
    print(f'data.experience value: {data.experience}')
    print(f'data.spouse value: {data.spouse}')
    print(f'data.surname value: {data.surname}')
    print(f'data.total_autos value: {data.total_autos}')
    print(f'data.total_kills value: {data.total_kills}')
    print(f'data.total_quests value: {data.total_quests}')
    print(f'data.tradeskills value: {data.tradeskills}')
    print(f'data.stats.health value: {data.stats.health}')
    print(f'data.stats.attack value: {data.stats.attack}')
    print(f'data.stats.defence value: {data.stats.defence}')
    print(f'data.stats.accuracy value: {data.stats.accuracy}')
    print(f'data.stats.evasion value: {data.stats.evasion}')
    print(f'data.token_boosts.exp_boost value: {data.token_boosts.exp_boost}')
    print(f'data.token_boosts.gold_boost value: {data.token_boosts.gold_boost}')
    print(f'data.token_boosts.stat_boost value: {data.token_boosts.stat_boost}')
    print(f'data.token_boosts.quest_boost value: {data.token_boosts.quest_boost}')
    print(f'data.token_boosts.global_boost value: {data.token_boosts.global_boost}')
    print(f'data.token_boosts.health_boost value: {data.token_boosts.health_boost}')
    print(f'data.token_boosts.attack_boost value: {data.token_boosts.attack_boost}')
    print(f'data.token_boosts.defence_boost value: {data.token_boosts.defence_boost}')
    print(f'data.token_boosts.accuracy_boost value: {data.token_boosts.accuracy_boost}')
    print(f'data.token_boosts.evasion_boost value: {data.token_boosts.evasion_boost}')
    print(f'data.token_boosts.jack_of_all_jades value: {data.token_boosts.jack_of_all_jades}')
    print(f'data.token_boosts.dungeon_mastery value: {data.token_boosts.dungeon_mastery}')
    print(f'data.token_boosts.areaboss_taxonomy value: {data.token_boosts.areaboss_taxonomy}')
    print(f'data.token_boosts.tradeskill_slots value: {data.token_boosts.tradeskill_slots}')
    print(f'data.token_boosts.jewellery_slots value: {data.token_boosts.jewellery_slots}')
    print(f"data.equipment.shortsword['orb'] value: {data.equipment.shortsword['orb']}")
    print(f"data.equipment.shortsword['level'] value: {data.equipment.shortsword['level']}")
    print(f"data.equipment.dagger['orb'] value: {data.equipment.dagger['orb']}")
    print(f"data.equipment.dagger['level'] value: {data.equipment.dagger['level']}")
    print(f"data.equipment.helmet['orb'] value: {data.equipment.helmet['orb']}")
    print(f"data.equipment.helmet['level'] value: {data.equipment.helmet['level']}")
    print(f"data.equipment.shoulders['orb'] value: {data.equipment.shoulders['orb']}")
    print(f"data.equipment.shoulders['level'] value: {data.equipment.shoulders['level']}")
    print(f"data.equipment.wrist['orb'] value: {data.equipment.wrist['orb']}")
    print(f"data.equipment.wrist['level'] value: {data.equipment.wrist['level']}")
    print(f"data.equipment.gloves['orb'] value: {data.equipment.gloves['orb']}")
    print(f"data.equipment.gloves['level'] value: {data.equipment.gloves['level']}")
    print(f"data.equipment.chestpiece['orb'] value: {data.equipment.chestpiece['orb']}")
    print(f"data.equipment.chestpiece['level'] value: {data.equipment.chestpiece['level']}")
    print(f"data.equipment.leggings['orb'] value: {data.equipment.leggings['orb']}")
    print(f"data.equipment.leggings['level'] value: {data.equipment.leggings['level']}")
    print(f"data.equipment.boots['orb'] value: {data.equipment.boots['orb']}")
    print(f"data.equipment.boots['level'] value: {data.equipment.boots['level']}")