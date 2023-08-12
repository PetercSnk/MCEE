execute if score @p potions_comp matches 0 run dialogue change @e [type=npc, tag=npc3] inclass0
execute if score @p spells_comp matches 0 run dialogue change @e [type=npc, tag=npc5] inclass2
execute if score @p alchemy_comp matches 0 run dialogue change @e [type=npc, tag=npc6] inclass3
execute if score @p astronomy_comp matches 0 run dialogue change @e [type=npc, tag=npc7] inclass4
scoreboard objectives add plant0 dummy
scoreboard objectives add plant1 dummy
scoreboard objectives add plant2 dummy
scoreboard objectives add plant3 dummy
scoreboard players set @p plant0 0
scoreboard players set @p plant1 0
scoreboard players set @p plant2 0
scoreboard players set @p plant3 0
scoreboard players set @p herbology 1
scoreboard players set @p tmp 1