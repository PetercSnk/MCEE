execute if score @p potions_comp matches 0 run dialogue change @e [type=npc, tag=npc3] potions0
execute if score @p potions_comp matches 1 if score @p potions matches 1 run scoreboard players set @p potions 0
execute if score @p herbology_comp matches 0 run dialogue change @e [type=npc, tag=npc4] herbology0
execute if score @p herbology_comp matches 1 if score @p herbology matches 1 run scoreboard players set @p herbology 0
execute if score @p spells_comp matches 0 run dialogue change @e [type=npc, tag=npc5] spells0
execute if score @p spells_comp matches 1 if score @p spells matches 1 run scoreboard players set @p spells 0
execute if score @p alchemy_comp matches 0 run dialogue change @e [type=npc, tag=npc6] alchemy0
execute if score @p alchemy_comp matches 1 if score @p alchemy matches 1 run scoreboard players set @p alchemy 0
execute if score @p astronomy_comp matches 0 run dialogue change @e [type=npc, tag=npc7] astronomy0
execute if score @p astronomy_comp matches 1 if score @p astronomy matches 1 run scoreboard players set @p astronomy 0