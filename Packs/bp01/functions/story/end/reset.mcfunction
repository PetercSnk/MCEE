function init/scoreboard

dialogue change @e [type=npc, tag=npc0] intro0
dialogue change @e [type=npc, tag=npc1] intro3
dialogue change @e [type=npc, tag=npc2] intro7
dialogue change @e [type=npc, tag=npc3] potions0
dialogue change @e [type=npc, tag=npc4] herbology0
dialogue change @e [type=npc, tag=npc5] spells0
dialogue change @e [type=npc, tag=npc6] alchemy0
dialogue change @e [type=npc, tag=npc7] astronomy0
dialogue change @e [type=npc, tag=npc80] studentreps0
dialogue change @e [type=npc, tag=npc81] studentreps0
dialogue change @e [type=npc, tag=npc82] studentreps0
dialogue change @e [type=npc, tag=npc83] studentreps0
dialogue change @e [type=npc, tag=npc84] studentreps0
dialogue change @e [type=npc, tag=npc85] studentreps0
dialogue change @e [type=npc, tag=npc9] 3complete0

tp @e [type=npc, tag=npc0] -30 -59 216 facing -38 -58 225
tp @e [type=npc, tag=npc1] -285 -59 243 facing -287 -59 247
tp @e [type=npc, tag=npc2] -257 -59 245 facing -259 -59 245
tp @e [type=npc, tag=npc3] -330 -53 242 facing -331 -53 227
tp @e [type=npc, tag=npc4] -342 -48 235 facing -352 -48 232
tp @e [type=npc, tag=npc5] -264 -43 238 facing -269 -43 238
tp @e [type=npc, tag=npc6] -263 -38 238 facing -270 -38 231
tp @e [type=npc, tag=npc7] -236 -33 234 facing -231 -33 226
tp @e [type=npc, tag=npc80] -288 -59 222
tp @e [type=npc, tag=npc81] -284 -53 228
tp @e [type=npc, tag=npc82] -281 -48 227
tp @e [type=npc, tag=npc83] -282 -43 227
tp @e [type=npc, tag=npc84] -281 -38 236
tp @e [type=npc, tag=npc85] -280 -33 226
tp @e [type=npc, tag=npc9] -269 -53 219

tp @p -41 -58 226
execute as @p run function init/misc