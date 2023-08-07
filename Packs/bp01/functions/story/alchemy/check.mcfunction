execute if block -257 -38 247 ? if block -258 -38 247 ? if block -259 -38 247 ? if block -260 -38 247 ? if block -261 -38 247 ? if block -262 -38 247 ? if score @p alch0 matches 0 run give @p iron_block 1
execute if block -257 -38 247 ? if block -258 -38 247 ? if block -259 -38 247 ? if block -260 -38 247 ? if block -261 -38 247 ? if block -262 -38 247 ? if score @p alch0 matches 0 run scoreboard players set @p alch0 1
execute if block -264 -38 247 ? if block -265 -38 247 ? if block -266 -38 247 ? if block -267 -38 247 ? if block -268 -38 247 ? if block -269 -38 247 ? if score @p alch1 matches 0 run give @p glowstone 1
execute if block -264 -38 247 ? if block -265 -38 247 ? if block -266 -38 247 ? if block -267 -38 247 ? if block -268 -38 247 ? if block -269 -38 247 ? if score @p alch1 matches 0 run scoreboard players set @p alch1 1
execute if block -257 -38 228 ? if block -258 -38 228 ? if block -259 -38 228 ? if block -260 -38 228 ? if block -261 -38 228 ? if block -262 -38 228 ? if score @p alch2 matches 0 run give @p cobblestone 1
execute if block -257 -38 228 ? if block -258 -38 228 ? if block -259 -38 228 ? if block -260 -38 228 ? if block -261 -38 228 ? if block -262 -38 228 ? if score @p alch2 matches 0 run scoreboard players set @p alch2 1
execute if block -264 -38 228 ? if block -265 -38 228 ? if block -266 -38 228 ? if block -267 -38 228 ? if block -268 -38 228 ? if block -269 -38 228 ? if score @p alch3 matches 0 run give @p log 1 1
execute if block -264 -38 228 ? if block -265 -38 228 ? if block -266 -38 228 ? if block -267 -38 228 ? if block -268 -38 228 ? if block -269 -38 228 ? if score @p alch3 matches 0 run scoreboard players set @p alch3 1
execute if block -250 -38 240 iron_block if -254 -38 240 glowstone if block -250 -38 236 cobblestone if block -254 -38 236 log 1 run function story/alchemy/transmutation
execute if block -252 -38 238 gold_block run scoreboard players set @p alchemy_comp 1
execute if score @p alchemy_comp matches 1 run function story/alchemy/notify
execute if score @p alchemy_comp matches 1 if score @p tmp matches 1 run function story/alchemy/complete
