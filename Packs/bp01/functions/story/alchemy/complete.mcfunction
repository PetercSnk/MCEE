scoreboard objectives remove alch0
scoreboard objectives remove alch1
scoreboard objectives remove alch2
scoreboard objectives remove alch3
clear @p
dialogue change @e [type=npc, tag=npc6] alchemy5
dialogue open @e [type=npc, tag=npc6] @p alchemy5
scoreboard set @p alchemy 0