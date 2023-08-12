execute if score @p herbology_comp matches 0 run dialogue change @e [type=npc, tag=npc4] inclass1
execute if score @p spells_comp matches 0 run dialogue change @e [type=npc, tag=npc5] inclass2
execute if score @p alchemy_comp matches 0 run dialogue change @e [type=npc, tag=npc6] inclass3
execute if score @p astronomy_comp matches 0 run dialogue change @e [type=npc, tag=npc7] inclass4
scoreboard players set @p potions 1
scoreboard players set @p tmp 1