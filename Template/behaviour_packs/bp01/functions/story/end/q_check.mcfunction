execute if score @p question matches 0 if score @p potions_comp matches 1 run dialogue open @e [type=npc, tag=npc9] @p end3
execute if score @p question matches 0 if score @p potions_comp matches 0 run scoreboard players set @p question 1
execute if score @p question matches 1 if score @p herbology_comp matches 1 run dialogue open @e [type=npc, tag=npc9] @p end4
execute if score @p question matches 1 if score @p herbology_comp matches 0 run scoreboard players set @p question 2
execute if score @p question matches 2 if score @p spells_comp matches 1 run dialogue open @e [type=npc, tag=npc9] @p end5
execute if score @p question matches 2 if score @p spells_comp matches 0 run scoreboard players set @p question 3
execute if score @p question matches 3 if score @p alchemy_comp matches 1 run dialogue open @e [type=npc, tag=npc9] @p end6
execute if score @p question matches 3 if score @p alchemy_comp matches 0 run scoreboard players set @p question 4
execute if score @p question matches 4 if score @p astronomy_comp matches 1 run dialogue open @e [type=npc, tag=npc9] @p end7
execute if score @p question matches 4 if score @p astronomy_comp matches 0 run scoreboard players set @p question 5
execute if score @p question matches 5 run scoreboard players set @p end_stage 2