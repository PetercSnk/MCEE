execute if block -267 -43 241 blackstone if score @p spell0 matches 0 run function story/spells/spell0
execute if block -267 -43 241 blackstone if score @p spell0 matches 0 run scoreboard players set @p spell0 1
execute if block -267 -43 238 ice if score @p spell1 matches 0 run function story/spells/spell1
execute if block -267 -43 238 ice if score @p spell1 matches 0 run scoreboard players set @p spell1 1
execute if block -267 -43 232 diamond_block if score @p spell2 matches 0 run function story/spells/spell2
execute if block -267 -43 232 diamond_block if score @p spell2 matches 0 run scoreboard players set @p spell2 1
execute if score @p spell0 matches 1 if score @p spell1 matches 1 if score @p spell2 matches 1 run scoreboard players set @p spells_comp 1
execute if score @p spells_comp matches 1 run function story/spells/notify
execute if score @p spells_comp matches 1 if score @p tmp matches 1 run function story/spells/complete
