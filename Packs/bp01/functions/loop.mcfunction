#execute as @a if score @a act matches 1 run say ACT 1
#execute as @a if score @a act matches 2 run say ACT 2
#execute as @a if score @a guide matches 1 run function test
#execute as @a if score @a pause matches 0 run scoreboard players add @a tick 1
#execute as @a if score @a act matches 1 if score @a guide matches 1 run function test

#scoreboard players add @a tick 1
execute as @a if score @a act matches 0 run function act/0/a0
execute as @a if score @a act matches 1 run function act/1/a1
