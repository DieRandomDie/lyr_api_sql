import mysql.connector as sql
from config import host, user, password, database

CREATE_TABLE = '''create table IF NOT EXISTS users
(
    discord_name                   varchar(50)    not null,
    discord_id                     varchar(50)    not null,
    data_name                      varchar(50)    not null,
    data_id                        varchar(50)    not null,
    data_level                     int            not null,
    data_current_area              smallint       not null,
    data_experience                bigint         not null,
    data_spouse                    varchar(50)    not null,
    data_surname                   varchar(50)    not null,
    data_total_autos               smallint       not null,
    data_total_kills               int            not null,
    data_total_quests              smallint       not null,
    currency_tokens                int            not null,
    currency_bound_tokens          int            not null,
    currency_money                 decimal(20, 6) not null,
    currency_jade                  int            not null,
    currency_jewel_frags           int            not null,
    currency_enchanting_dust       int            not null,
    currency_dungeon_points        int            not null,
    currency_diamonds              int            not null,
    currency_rubies                int            not null,
    currency_sapphires             int            not null,
    currency_emeralds              int            not null,
    currency_opals                 int            not null,
    guild_guild_name               varchar(50)    not null,
    guild_guild_level              smallint       not null,
    guild_weekly_dungeon_points    decimal(20, 2) not null,
    jade_boosts_crit_hit_chance    decimal(20, 2) not null,
    jade_boosts_crit_hit_damage    decimal(20, 2) not null,
    jade_boosts_heroism            decimal(20, 2) not null,
    jade_boosts_leadership         decimal(20, 2) not null,
    jade_boosts_archaeology        decimal(20, 2) not null,
    jade_boosts_jewelcrafting      decimal(20, 2) not null,
    jade_boosts_serendipity        decimal(20, 2) not null,
    jade_boosts_e_peen             decimal(20, 2) not null,
    jade_boosts_jade_god           int            not null,
    stats_health                   int            not null,
    stats_attack                   int            not null,
    stats_defence                  int            not null,
    stats_accuracy                 int            not null,
    stats_evasion                  int            not null,
    token_boosts_exp_boost         decimal(20, 2) not null,
    token_boosts_gold_boost        decimal(20, 2) not null,
    token_boosts_stat_boost        decimal(20, 2) not null,
    token_boosts_quest_boost       decimal(20, 2) not null,
    token_boosts_global_boost      decimal(20, 2) not null,
    token_boosts_health_boost      decimal(20, 2) not null,
    token_boosts_attack_boost      decimal(20, 2) not null,
    token_boosts_defence_boost     decimal(20, 2) not null,
    token_boosts_accuracy_boost    decimal(20, 2) not null,
    token_boosts_evasion_boost     decimal(20, 2) not null,
    token_boosts_jack_of_all_jades decimal(20, 2) not null,
    token_boosts_dungeon_mastery   decimal(20, 2) not null,
    token_boosts_areaboss_taxonomy decimal(20, 2) not null,
    token_boosts_tradeskill_slots  smallint       not null,
    token_boosts_jewellery_slots   smallint       not null,
    equipment_shortsword_level     smallint       not null,
    equipment_shortsword_orb       varchar(50)    not null,
    equipment_dagger_level         smallint       not null,
    equipment_dagger_orb           varchar(50)    not null,
    equipment_helmet_level         smallint       not null,
    equipment_helmet_orb           varchar(50)    not null,
    equipment_shoulders_level      smallint       not null,
    equipment_shoulders_orb        varchar(50)    not null,
    equipment_wrist_level          smallint       not null,
    equipment_wrist_orb            varchar(50)    not null,
    equipment_gloves_level         smallint       not null,
    equipment_gloves_orb           varchar(50)    not null,
    equipment_chestpiece_level     smallint       not null,
    equipment_chestpiece_orb       varchar(50)    not null,
    equipment_leggings_level       smallint       not null,
    equipment_leggings_orb         varchar(50)    not null,
    equipment_boots_level          smallint       not null,
    equipment_boots_orb            varchar(50)    not null,
    primary key (discord_id)
)'''


def update_db(query):
    db = sql.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    cur = db.cursor()

    cur.execute(query)
    cur.close()
    db.close()
