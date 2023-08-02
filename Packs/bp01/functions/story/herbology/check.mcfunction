execute if score @p plant0 matches 0 if block -259 -53 137 yellow_flower run scoreboard players set @p plant0 1
execute if score @p plant1 matches 0 if block -256 -53 137 red_flower 1 run scoreboard players set @p plant1 1
execute if score @p plant2 matches 0 if block -253 -53 137 red_flower 8 run scoreboard players set @p plant2 1
execute if score @p plant3 matches 0 if block -250 -53 137 red_flower 9 run scoreboard players set @p plant3 1
execute if score @p plant0 matches 1 if score @p plant1 matches 1 if score @p plant2 matches 1 if score @p plant3 matches 1 run scoreboard players set @p herbology_complete 1
execute if score @p herbology matches 1 if score @a herbology_complete matches 1 run function story/herbology/complete