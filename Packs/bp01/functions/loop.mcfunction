execute if score @p potions matches 1 run function story/potions/check
execute if score @p herbology matches 1 run function story/herbology/check
execute if score @p spells matches 1 run function story/spells/check
execute if score @p alchemy matches 1 run function story/alchemy/check
execute if score @p astronomy matches 1 run function story/astronomy/check
execute if score @p classes_comp > @p int if score @p 3complete_comp matches 0 run scoreboard players set @p 3complete 1
execute if score @p 3complete matches 1 run function story/3complete/check
execute if score @p weather matches 0 run weather clear