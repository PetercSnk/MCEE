execute if score @p pillar0 matches 1 run particle pillar0 -215 -58 265
execute if block -215 -58 265 emerald_block run scoreboard players set @p pillar0 2
execute if score @p pillar0 matches 2 run particle pillar1 -215 -58 265
execute if score @p pillar1 matches 1 run particle pillar0 -215 -58 206
execute if block -215 -58 206 emerald_block run scoreboard players set @p pillar1 2
execute if score @p pillar1 matches 2 run particle pillar1 -215 -58 206
execute if score @p pillar2 matches 1 run particle pillar0 -369 -58 265
execute if block -369 -58 265 emerald_block run scoreboard players set @p pillar2 2
execute if score @p pillar2 matches 2 run particle pillar1 -369 -58 265
execute if score @p pillar3 matches 1 run particle pillar0 -369 -58 206
execute if block -369 -58 206 emerald_block run scoreboard players set @p pillar3 2
execute if score @p pillar3 matches 2 run particle pillar1 -369 -58 206
execute if score @p pillar0 matches 2 if score @p pillar1 matches 2 if score @p pillar2 matches 2 if score @p pillar3 matches 2 run scoreboard players set @p end_stage 4 