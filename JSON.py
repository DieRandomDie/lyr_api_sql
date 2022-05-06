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

json_text = getApi('7aa25915cc3d82bda3c1b5c1179d98fc').replace(' ','_').replace('-','_')
data = json.loads(json_text,object_hook=lambda d: SimpleNamespace(**d))

orbs = []
levels = []
for index, key in enumerate(vars(data.equipment)):
    orbs.append(key.split("_")[0])
    levels.append(vars(data.equipment)[key])

data.equipment.shortsword = {'orb': orbs[0], 'level': levels[0]}
data.equipment.dagger = {'orb': orbs[1], 'level': levels[1]}
data.equipment.helmet = {'orb': orbs[2], 'level': levels[2]}
data.equipment.shoulders = {'orb': orbs[3], 'level': levels[3]}
data.equipment.wrist = {'orb': orbs[4], 'level': levels[4]}
data.equipment.gloves = {'orb': orbs[5], 'level': levels[5]}
data.equipment.chestpiece = {'orb': orbs[6], 'level': levels[6]}
data.equipment.leggings = {'orb': orbs[7], 'level': levels[7]}
data.equipment.boots = {'orb': orbs[8], 'level': levels[8]}

print(data.currency.tokens)
print(data.currency.bound_tokens)
print(data.currency.money)
print(data.currency.jade)
print(data.currency.jewel_frags)
print(data.currency.enchanting_dust)
print(data.currency.dungeon_points)
print(data.currency.diamonds)
print(data.currency.rubies)
print(data.currency.sapphires)
print(data.currency.emeralds)
print(data.currency.opals)
print(data.guild.guild_name)
print(data.guild.guild_level)
print(data.guild.weekly_dungeon_points)
print(data.jade_boosts.crit_hit_chance)
print(data.jade_boosts.crit_hit_damage)
print(data.jade_boosts.heroism)
print(data.jade_boosts.leadership)
print(data.jade_boosts.archaeology)
print(data.jade_boosts.jewelcrafting)
print(data.jade_boosts.serendipity)
print(data.jade_boosts.e_peen)
print(data.jade_boosts.jade_god)
print(data.id)
print(data.name)
print(data.level)
print(data.current_area)
print(data.experience)
print(data.spouse)
print(data.surname)
print(data.total_autos)
print(data.total_kills)
print(data.total_quests)
print(data.stats.health)
print(data.stats.attack)
print(data.stats.defence)
print(data.stats.accuracy)
print(data.stats.evasion)
print(data.token_boosts.exp_boost)
print(data.token_boosts.gold_boost)
print(data.token_boosts.stat_boost)
print(data.token_boosts.quest_boost)
print(data.token_boosts.global_boost)
print(data.token_boosts.health_boost)
print(data.token_boosts.attack_boost)
print(data.token_boosts.defence_boost)
print(data.token_boosts.accuracy_boost)
print(data.token_boosts.evasion_boost)
print(data.token_boosts.jack_of_all_jades)
print(data.token_boosts.dungeon_mastery)
print(data.token_boosts.areaboss_taxonomy)
print(data.token_boosts.tradeskill_slots)
print(data.token_boosts.jewellery_slots)
print(data.equipment.shortsword)
print(data.equipment.dagger)
print(data.equipment.helmet)
print(data.equipment.shoulders)
print(data.equipment.wrist)
print(data.equipment.gloves)
print(data.equipment.chestpiece)
print(data.equipment.leggings)
print(data.equipment.boots)


'''
CURRENCY
currency.tokens
currency.bound_tokens
currency.money
currency.jade
currency.jewel_frags
currency.enchanting_dust
currency.dungeon_points
currency.diamonds
currency.rubies
currency.sapphires
currency.emeralds
currency.opals

GUILD DATA
guild.guild_name
guild.guild_level
guild.guild_weekly_dungeon_points

JADE BOOSTS
jade_boosts.crit_hit_chance
jade_boosts.crit_hit_damage
jade_boosts.heroism
jade_boosts.leadership
jade_boosts.archaeology
jade_boosts.jewelcrafting
jade_boosts.serendipity
jade_boosts.e-peen
jade_boosts.jade_god

SIMPLE DATA
id
name
level
current_area
experience
spouse
surname
total_autos
total_kills
total_quests
tradeskills

STATS
stats.health
stats.attack
stats.defence
stats.accuracy
stats.evasion

TOKEN BOOSTS
token_boosts.exp_boost
token_boosts.gold_boost
token_boosts.stat_boost
token_boosts.quest_boost
token_boosts.global_boost
token_boosts.health_boost
token_boosts.attack_boost
token_boosts.defence_boost
token_boosts.accuracy_boost
token_boosts.evasion_boost
token_boosts.jack_of_all_jades
token_boosts.dungeon_mastery
token_boosts.areaboss_taxonomy
token_boosts.tradeskill_slots
token_boosts.jewellery_slots

NEEDS WORK
equipment
'''
