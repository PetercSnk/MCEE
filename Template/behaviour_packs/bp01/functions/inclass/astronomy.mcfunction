execute if score @p potions_comp matches 0 run dialogue change @e [type=npc, tag=npc3] inclass0
execute if score @p herbology_comp matches 0 run dialogue change @e [type=npc, tag=npc4] inclass1
execute if score @p spells_comp matches 0 run dialogue change @e [type=npc, tag=npc5] inclass2
execute if score @p alchemy_comp matches 0 run dialogue change @e [type=npc, tag=npc6] inclass3
scoreboard players set @p astronomy 1
scoreboard players set @p tmp 1