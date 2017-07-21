from bestiary.models import Monster, LeaderSkill
from herders.models import RuneInstance, RuneCraftInstance, Summoner
from .models import RunLog, SummonLog, RuneDrop, ItemDrop

element_map = {
    1: Monster.ELEMENT_WATER,
    2: Monster.ELEMENT_FIRE,
    3: Monster.ELEMENT_WIND,
    4: Monster.ELEMENT_LIGHT,
    5: Monster.ELEMENT_DARK,
    6: Monster.ELEMENT_PURE,
}

archetype_map = {
    0: Monster.TYPE_NONE,
    1: Monster.TYPE_ATTACK,
    2: Monster.TYPE_DEFENSE,
    3: Monster.TYPE_HP,
    4: Monster.TYPE_SUPPORT,
    5: Monster.TYPE_MATERIAL
}

leader_skill_stat_map = {
    1: LeaderSkill.ATTRIBUTE_HP,
    2: LeaderSkill.ATTRIBUTE_ATK,
    3: LeaderSkill.ATTRIBUTE_DEF,
    4: LeaderSkill.ATTRIBUTE_SPD,
    5: LeaderSkill.ATTRIBUTE_CRIT_RATE,
    6: LeaderSkill.ATTRIBUTE_CRIT_DMG,
    7: LeaderSkill.ATTRIBUTE_RESIST,
    8: LeaderSkill.ATTRIBUTE_ACCURACY,
}

leader_skill_area_map = {
    0: LeaderSkill.AREA_GENERAL,
    1: LeaderSkill.AREA_ARENA,
    2: LeaderSkill.AREA_DUNGEON,
    5: LeaderSkill.AREA_GUILD,
}

building_id_map = {
    'summoners_tower': 1,
    'summonhenge': 2,
    'pond_of_mana': 3,
    'crystal_mine': 4,
    'gateway': 8,
    'temple_of_wishes': 10,
    'magic_shop': 11,
    'ancient_stones': 12,
    'arcane_tower': 14,
    'crystal_titan': 15,
    'fusion_hexagram': 16,
    'fuse_center': 17,
    'power_up_circle': 20,
    'tranquil_forest': 22,
    'gusty_cliffs': 23,
    'deep_forest_ent': 24,
    'monster_storage': 25,
    'transmogrification_building': 27,
}

decoration_id_map = {
    'guardstone': 4,
    'mana_fountain': 5,
    'sky_tribe_totem': 6,
    'arcane_booster_tower': 7,
    'crystal_altar': 8,
    'ancient_sword': 9,
    'sanctum_of_energy': 10,
    'mysterious_plant': 11,
    'fire_sanctuary': 15,
    'water_sanctuary': 16,
    'wind_sanctuary': 17,
    'light_sanctuary': 18,
    'dark_sanctuary': 19,
    'fallen_ancient_guardian': 31,
    'crystal_rock': 34,
    'fairy_tree': 35,
    'flag_of_battle': 36,
    'flag_of_rage': 37,
    'flag_of_hope': 38,
    'flag_of_will': 39,
}

inventory_type_map = {
    'monster': 1,
    'currency': 6,
    'rune': 8,
    'scroll': 9,
    'booster': 10,
    'essences': 11,
    'monster_piece': 12,
    # '': 15, Unknown. Appears in inventory_info with qty 0
    'guild_monster_piece': 19,
    'rainbowmon': 25,   # Possibly material monsters in general. Appears when wish returns a rainbowmon.
    'rune_craft': 27,
    'craft_stuff': 29,
}

inventory_essence_map = {
    11006: "storage_magic_low",
    12006: "storage_magic_mid",
    13006: "storage_magic_high",
    11001: "storage_water_low",
    12001: "storage_water_mid",
    13001: "storage_water_high",
    11002: "storage_fire_low",
    12002: "storage_fire_mid",
    13002: "storage_fire_high",
    11003: "storage_wind_low",
    12003: "storage_wind_mid",
    13003: "storage_wind_high",
    11004: "storage_light_low",
    12004: "storage_light_mid",
    13004: "storage_light_high",
    11005: "storage_dark_low",
    12005: "storage_dark_mid",
    13005: "storage_dark_high",
}

inventory_craft_map = {
    1001: 'wood',
    1002: 'leather',
    1003: 'rock',
    1004: 'ore',
    1005: 'mithril',
    1006: 'cloth',
    2001: 'rune_piece',
    3001: 'powder',
    4001: 'symbol_harmony',
    4002: 'symbol_transcendance',
    4003: 'symbol_chaos',
    5001: 'crystal_water',
    5002: 'crystal_fire',
    5003: 'crystal_wind',
    5004: 'crystal_light',
    5005: 'crystal_dark',
    6001: 'crystal_magic',
    7001: 'crystal_pure',
}

rune_set_map = {
    1: RuneInstance.TYPE_ENERGY,
    2: RuneInstance.TYPE_GUARD,
    3: RuneInstance.TYPE_SWIFT,
    4: RuneInstance.TYPE_BLADE,
    5: RuneInstance.TYPE_RAGE,
    6: RuneInstance.TYPE_FOCUS,
    7: RuneInstance.TYPE_ENDURE,
    8: RuneInstance.TYPE_FATAL,
    10: RuneInstance.TYPE_DESPAIR,
    11: RuneInstance.TYPE_VAMPIRE,
    13: RuneInstance.TYPE_VIOLENT,
    14: RuneInstance.TYPE_NEMESIS,
    15: RuneInstance.TYPE_WILL,
    16: RuneInstance.TYPE_SHIELD,
    17: RuneInstance.TYPE_REVENGE,
    18: RuneInstance.TYPE_DESTROY,
    19: RuneInstance.TYPE_FIGHT,
    20: RuneInstance.TYPE_DETERMINATION,
    21: RuneInstance.TYPE_ENHANCE,
    22: RuneInstance.TYPE_ACCURACY,
    23: RuneInstance.TYPE_TOLERANCE,
}

rune_stat_type_map = {
    1: RuneInstance.STAT_HP,
    2: RuneInstance.STAT_HP_PCT,
    3: RuneInstance.STAT_ATK,
    4: RuneInstance.STAT_ATK_PCT,
    5: RuneInstance.STAT_DEF,
    6: RuneInstance.STAT_DEF_PCT,
    8: RuneInstance.STAT_SPD,
    9: RuneInstance.STAT_CRIT_RATE_PCT,
    10: RuneInstance.STAT_CRIT_DMG_PCT,
    11: RuneInstance.STAT_RESIST_PCT,
    12: RuneInstance.STAT_ACCURACY_PCT,
}

rune_quality_map = {
    1: RuneInstance.QUALITY_NORMAL,
    2: RuneInstance.QUALITY_MAGIC,
    3: RuneInstance.QUALITY_RARE,
    4: RuneInstance.QUALITY_HERO,
    5: RuneInstance.QUALITY_LEGEND,
}

craft_type_map = {
    1: RuneInstance.CRAFT_ENCHANT_GEM,
    2: RuneInstance.CRAFT_GRINDSTONE,
}

craft_quality_map = {
    1: RuneCraftInstance.QUALITY_NORMAL,
    2: RuneCraftInstance.QUALITY_MAGIC,
    3: RuneCraftInstance.QUALITY_RARE,
    4: RuneCraftInstance.QUALITY_HERO,
    5: RuneCraftInstance.QUALITY_LEGEND,
}

scenario_difficulty_map = {
    1: RunLog.DIFFICULTY_NORMAL,
    2: RunLog.DIFFICULTY_HARD,
    3: RunLog.DIFFICULTY_HELL,
}

summon_source_map = {
    1: SummonLog.SCROLL_UNKNOWN,
    2: SummonLog.SCROLL_MYSTICAL,
    3: SummonLog.SCROLL_LIGHT_AND_DARK,
    4: SummonLog.SCROLL_WATER,
    5: SummonLog.SCROLL_FIRE,
    6: SummonLog.SCROLL_WIND,
    7: SummonLog.SCROLL_LEGENDARY,
    8: SummonLog.SUMMON_EXCLUSIVE,
    9: SummonLog.SUMMON_LEGENDARY_PIECES,
    10: SummonLog.SUMMON_LIGHT_AND_DARK_PIECES,
    11: SummonLog.SCROLL_TRANSCENDANCE,
}

drop_essence_map = {
    11006: RunLog.DROP_ESSENCE_MAGIC_LOW,
    12006: RunLog.DROP_ESSENCE_MAGIC_MID,
    13006: RunLog.DROP_ESSENCE_MAGIC_HIGH,
    11001: RunLog.DROP_ESSENCE_WATER_LOW,
    12001: RunLog.DROP_ESSENCE_WATER_MID,
    13001: RunLog.DROP_ESSENCE_WATER_HIGH,
    11002: RunLog.DROP_ESSENCE_FIRE_LOW,
    12002: RunLog.DROP_ESSENCE_FIRE_MID,
    13002: RunLog.DROP_ESSENCE_FIRE_HIGH,
    11003: RunLog.DROP_ESSENCE_WIND_LOW,
    12003: RunLog.DROP_ESSENCE_WIND_MID,
    13003: RunLog.DROP_ESSENCE_WIND_HIGH,
    11004: RunLog.DROP_ESSENCE_LIGHT_LOW,
    12004: RunLog.DROP_ESSENCE_LIGHT_MID,
    13004: RunLog.DROP_ESSENCE_LIGHT_HIGH,
    11005: RunLog.DROP_ESSENCE_DARK_LOW,
    12005: RunLog.DROP_ESSENCE_DARK_MID,
    13005: RunLog.DROP_ESSENCE_DARK_HIGH,
}

drop_craft_map = {
    1001: RunLog.DROP_CRAFT_WOOD,
    1002: RunLog.DROP_CRAFT_LEATHER,
    1003: RunLog.DROP_CRAFT_ROCK,
    1004: RunLog.DROP_CRAFT_ORE,
    1005: RunLog.DROP_CRAFT_MITHRIL,
    1006: RunLog.DROP_CRAFT_CLOTH,
    2001: RunLog.DROP_CRAFT_RUNE_PIECE,
    3001: RunLog.DROP_CRAFT_POWDER,
    4001: RunLog.DROP_CRAFT_SYMBOL_HARMONY,
    4002: RunLog.DROP_CRAFT_SYMBOL_TRANSCENDANCE,
    4003: RunLog.DROP_CRAFT_SYMBOL_CHAOS,
    5001: RunLog.DROP_CRAFT_CRYSTAL_WATER,
    5002: RunLog.DROP_CRAFT_CRYSTAL_FIRE,
    5003: RunLog.DROP_CRAFT_CRYSTAL_WIND,
    5004: RunLog.DROP_CRAFT_CRYSTAL_LIGHT,
    5005: RunLog.DROP_CRAFT_CRYSTAL_DARK,
    6001: RunLog.DROP_CRAFT_CRYSTAL_MAGIC,
    7001: RunLog.DROP_CRAFT_CRYSTAL_PURE,
}

drop_currency_map = {
    1: ItemDrop.DROP_CURRENCY_CRYSTALS,
    2: ItemDrop.DROP_CURRENCY_SOCIAL,
    3: ItemDrop.DROP_CURRENCY_REAL_MONEY,
    4: ItemDrop.DROP_CURRENCY_GLORY_POINT,
    5: ItemDrop.DROP_CURRENCY_GUILD_POINT,
    6: ItemDrop.DROP_COSTUME_POINT,
    102: ItemDrop.DROP_CURRENCY_MANA,
    103: ItemDrop.DROP_CURRENCY_ENERGY,
    104: ItemDrop.DROP_CURRENCY_ARENA_WING,
}

timezone_server_map = {
    'America/Los_Angeles': Summoner.SERVER_GLOBAL,
    'Europe/Berlin': Summoner.SERVER_EUROPE,
    'Asia/Seoul': Summoner.SERVER_KOREA,
    'Asia/Shanghai': Summoner.SERVER_ASIA,
}

valid_rune_drop_map = {
    1: [RuneDrop.TYPE_ENERGY],
    2: [RuneDrop.TYPE_FATAL],
    3: [RuneDrop.TYPE_BLADE],
    4: [RuneDrop.TYPE_SWIFT],
    5: [RuneDrop.TYPE_FOCUS],
    6: [RuneDrop.TYPE_GUARD],
    7: [RuneDrop.TYPE_ENDURE],
    8: [RuneDrop.TYPE_SHIELD],
    9: [RuneDrop.TYPE_REVENGE],
    10: [RuneDrop.TYPE_WILL],
    11: [RuneDrop.TYPE_NEMESIS],
    12: [RuneDrop.TYPE_VAMPIRE],
    13: [RuneDrop.TYPE_DESTROY],
    6001: [RuneDrop.TYPE_RAGE, RuneDrop.TYPE_WILL, RuneDrop.TYPE_NEMESIS, RuneDrop.TYPE_VAMPIRE, RuneDrop.TYPE_DESTROY],
    8001: [RuneDrop.TYPE_DESPAIR, RuneDrop.TYPE_ENERGY, RuneDrop.TYPE_FATAL, RuneDrop.TYPE_BLADE, RuneDrop.TYPE_SWIFT],
    9001: [RuneDrop.TYPE_VIOLENT, RuneDrop.TYPE_FOCUS, RuneDrop.TYPE_GUARD, RuneDrop.TYPE_ENDURE, RuneDrop.TYPE_SHIELD, RuneDrop.TYPE_REVENGE],
}

secret_dungeon_map = {
    # Secret dungeon ID: Monster Com2US ID
    1011: 10103,
    1012: 10105,
    1013: 10201,
    1014: 10202,
    1015: 10203,
    1016: 10204,
    1017: 10205,
    1018: 10301,
    1019: 10302,
    1020: 10303,
    1021: 10304,
    1022: 10305,
    1023: 10401,
    1024: 10402,
    1025: 10403,
    1026: 10404,
    1027: 10601,
    1028: 10602,
    1029: 10603,
    1030: 10604,
    1031: 10702,
    1032: 10703,
    1033: 10705,
    1034: 10801,
    1035: 10802,
    1036: 10803,
    1037: 10901,
    1038: 10902,
    1039: 10903,
    1040: 10905,
    1041: 11101,
    1042: 11103,
    1043: 11104,
    1044: 11105,
    1045: 12101,
    1046: 12102,
    1047: 12103,
    1048: 13201,
    1049: 13202,
    1050: 13203,
    1051: 13204,
    1052: 13205,
    1053: 14801,
    1054: 14802,
    1055: 14803,
    1056: 14804,
    1057: 15201,
    1058: 15203,
    1059: 13604,
    1060: 13605,
    1061: 12605,
    1062: 12814,
    2011: 10101,
    2012: 10102,
    2013: 10104,
    2014: 10405,
    2015: 10501,
    2016: 10502,
    2017: 10503,
    2018: 10504,
    2019: 10505,
    2020: 10605,
    2021: 10701,
    2022: 10704,
    2023: 10804,
    2024: 10805,
    2025: 10904,
    2026: 11001,
    2027: 11002,
    2028: 11003,
    2029: 11004,
    2030: 11005,
    2031: 11102,
    2032: 11301,
    2033: 11302,
    2034: 11303,
    2035: 11304,
    2036: 11305,
    2037: 11401,
    2038: 11402,
    2039: 11403,
    2040: 11404,
    2041: 11405,
    2042: 11501,
    2043: 11502,
    2044: 11503,
    2045: 11504,
    2046: 11505,
    2047: 11701,
    2048: 11702,
    2049: 11703,
    2050: 11704,
    2051: 11705,
    2052: 12001,
    2053: 12002,
    2054: 12003,
    2055: 12004,
    2056: 12005,
    2057: 12104,
    2058: 12105,
    2059: 13701,
    2060: 13702,
    2061: 13703,
    2062: 13704,
    2063: 13705,
    2064: 14001,
    2065: 14002,
    2066: 14003,
    2067: 14004,
    2068: 14005,
    2069: 14805,
    2070: 15001,
    2071: 15002,
    2072: 15003,
    2073: 15004,
    2074: 15005,
    2075: 15202,
    2076: 15204,
    2077: 15205,
    2078: 15301,
    2079: 15303,
    2080: 15305,
    2081: 15401,
    2082: 15402,
    2083: 15403,
    2084: 16001,
    2085: 16002,
    2086: 16003,
    2087: 16004,
    2088: 16005,
    2089: 14901,
    2090: 14902,
    2091: 14903,
    2092: 14904,
    2093: 14905,
    2094: 15601,
    2095: 15602,
    2096: 15603,
    2097: 15604,
    2098: 15605,
    2099: 16501,
    2100: 16502,
    2101: 16503,
    2102: 16504,
    2103: 16505,
    2104: 15901,
    2105: 15902,
    2106: 15903,
    2107: 15904,
    2108: 15905,
    2109: 17201,
    2110: 17202,
    2111: 17203,
    2112: 17204,
    2113: 17205,
    2114: 17701,
    2115: 17702,
    2116: 17703,
    2117: 17704,
    2118: 17705,
    2119: 17801,
    2120: 17802,
    2121: 17803,
    2122: 17804,
    2123: 17805,
    3011: 12705,
    3012: 12905,
    3013: 13005,
    3014: 13105,
    3015: 12805,
    2124: 15801,
    2125: 15802,
    2126: 15803,
    2127: 15804,
    2128: 15805,
    2129: 18501,
    2130: 18502,
    2131: 18503,
    2132: 18504,
    2133: 18505,
    2134: 18402,
    2135: 18405,
    2136: 18701,
    2137: 18702,
    2138: 18703,
    2139: 18704,
    2140: 18705,
    2141: 19001,
    2142: 19002,
    2143: 19003,
    2144: 19004,
    2145: 19005,
    2146: 19501,
    2147: 19502,
    2148: 19503,
    2149: 19504,
    2150: 19505,
    2151: 20201,
    2152: 20202,
    2153: 20203,
    2154: 20204,
    2155: 20205,
    2156: 20701,
    2157: 20702,
    2158: 20703,
    2159: 20704,
    2160: 20705,
    2161: 20801,
    2162: 20802,
    2163: 20803,
    2164: 20804,
    2165: 20805,
    2166: 20301,
    2167: 20302,
    2168: 20303,
    2169: 20304,
    2170: 20305,
}