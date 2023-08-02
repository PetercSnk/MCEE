scoreboard objectives remove spell0
scoreboard objectives remove spell1
scoreboard objectives remove spell2
clear @p
dialogue change @e [type=npc, tag=npc5] spells3
dialogue open @e [type=npc, tag=npc5] @p spells3
scoreboard set @p spells 0