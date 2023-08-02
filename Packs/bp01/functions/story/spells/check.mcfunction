execute if block -267 -43 241 gilded_blackstone if score @p spell0 matches 0 run function spells/spell0
execute if block -267 -43 241 gilded_blackstone if score @p spell0 matches 0 run scoreboard players set @p spell0 1
execute if block -267 -43 238 ice if score @p spell1 matches 0 run function spells/spell1
execute if block -267 -43 238 ice if score @p spell1 matches 0 run scoreboard players set @p spell1 1
execute if block -267 -43 232 diamond_block if score @p spell2 matches 0 run function spells/spell2
execute if block -267 -43 232 diamond_block if score @p spell2 matches 0 run scoreboard players set @p spell2 1
execute if score @p spell0 matches 1 if score @p spell1 matches 1 if score @p spell2 matches 1 run scoreboard players @p spells_complete 1
execute if score @p spells matches 1 if score @p spells_complete matches 1 run function story/spells/complete