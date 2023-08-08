execute if block -322 -53 245 polished_blackstone_button 10 run give @p nether_wart
execute if block -321 -53 245 polished_blackstone_button 10 run give @p gunpowder 1
execute if block -320 -53 245 polished_blackstone_button 10 run give @p sugar
execute if block -319 -53 245 polished_blackstone_button 10 run give @p rabbit_foot
execute if block -318 -53 245 polished_blackstone_button 10 run give @p glistering_melon_slice
execute if block -317 -53 245 polished_blackstone_button 10 run give @p blaze_powder
execute if block -316 -53 245 polished_blackstone_button 10 run give @p ghast_tear
execute if block -315 -53 245 polished_blackstone_button 10 run give @p magma_cream
execute if block -314 -53 245 polished_blackstone_button 10 run give @p golden_carrot
execute if block -313 -53 245 polished_blackstone_button 10 run give @p redstone
execute if block -312 -53 245 polished_blackstone_button 10 run give @p glowstone_dust
execute if entity @p [hasitem={item=splash_potion, data=33}] run scoreboard players set @p potions_comp 1
execute if score @p potions_comp matches 1 run function story/potions/notify
execute if score @p potions_comp matches 1 if score @p tmp matches 1 run function story/potions/complete 