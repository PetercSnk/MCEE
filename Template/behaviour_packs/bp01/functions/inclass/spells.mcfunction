execute if score @p potions_comp matches 0 run dialogue change @e [type=npc, tag=npc3] inclass0
execute if score @p herbology_comp matches 0 run dialogue change @e [type=npc, tag=npc4] inclass1
execute if score @p alchemy_comp matches 0 run dialogue change @e [type=npc, tag=npc6] inclass3
execute if score @p astronomy_comp matches 0 run dialogue change @e [type=npc, tag=npc7] inclass4
scoreboard objectives add spell0 dummy
scoreboard objectives add spell1 dummy
scoreboard objectives add spell2 dummy
scoreboard players set @p spell0 0
scoreboard players set @p spell1 0
scoreboard players set @p spell2 0
scoreboard players set @p spells 1
scoreboard players set @p tmp 1