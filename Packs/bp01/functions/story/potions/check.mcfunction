execute if entity @p [hasitem={item=splash_potion, data=33}] run scoreboard players set @p potions_comp 1
execute if score @p potions_comp matches 1 run function story/potions/notify
execute if score @p potions_comp matches 1 if score @p tmp matches 1 run function story/potions/complete 