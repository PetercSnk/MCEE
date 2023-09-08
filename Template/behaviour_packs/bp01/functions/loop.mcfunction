execute if block -39 -57 226 polished_blackstone_button 12 run function init/init
execute if score @p intro_stage > @p zero run function story/intro/check
execute if score @p potions matches 1 run function story/potions/check
execute if score @p herbology matches 1 run function story/herbology/check
execute if score @p spells matches 1 run function story/spells/check
execute if score @p alchemy matches 1 run function story/alchemy/check
execute if score @p astronomy matches 1 run function story/astronomy/check
execute if score @p end matches 1 run function story/end/check
execute if score @p classes_comp > @p int if score @p 3complete_comp matches 0 run function story/3complete/check
execute if score @p classes_comp matches 5 if score @p 5complete_init matches 0 run function story/3complete/5complete
execute if score @p weather matches 0 run weather clear
execute if score @p weather matches 1 run weather thunder
execute if score @p time matches 0 run time set day
execute if score @p time matches 1 run time set night
execute if score @p agent matches 1 if entity @c [tag=!skin_1] run tag @c add skin_1
execute if score @p agent matches 2 if entity @c [tag=!skin_2] run tag @c add skin_2
execute if score @p agent matches 3 if entity @c [tag=!skin_3] run tag @c add skin_3
execute if score @p npc1_001 matches 1 run function guides/npc1_001
execute if score @p 001_potions matches 1 run function guides/001_potions
execute if score @p 001_herbology matches 1 run function guides/001_herbology
execute if score @p 001_spells matches 1 run function guides/001_spells
execute if score @p 001_alchemy matches 1 run function guides/001_alchemy
execute if score @p 001_astronomy matches 1 run function guides/001_astronomy