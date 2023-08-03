structure load npc0 -73 -60 157 0_degrees none true false false
structure load npc1 -73 -60 155 0_degrees none true false false
structure load npc2 -73 -60 153 0_degrees none true false false
structure load npc3 -73 -60 151 0_degrees none true false false
structure load npc4 -73 -60 149 0_degrees none true false false
structure load npc5 -73 -60 147 0_degrees none true false false
structure load npc6 -73 -60 145 0_degrees none true false false
structure load npc7 -73 -60 143 0_degrees none true false false
structure load npc80 -73 -60 141 0_degrees none true false false
structure load npc81 -71 -60 141 0_degrees none true false false
structure load npc82 -69 -60 141 0_degrees none true false false
structure load npc83 -67 -60 141 0_degrees none true false false
structure load npc84 -65 -60 141 0_degrees none true false false
structure load npc85 -63 -60 141 0_degrees none true false false
structure load npc9 -73 -60 139 0_degrees none true false false

tag @e [type=npc, name=npc0] add npc0
tag @e [type=npc, name=npc1] add npc1
tag @e [type=npc, name=npc2] add npc2
tag @e [type=npc, name=npc3] add npc3
tag @e [type=npc, name=npc4] add npc4
tag @e [type=npc, name=npc5] add npc5
tag @e [type=npc, name=npc6] add npc6
tag @e [type=npc, name=npc7] add npc7
tag @e [type=npc, name=npc80] add npc80
tag @e [type=npc, name=npc81] add npc81
tag @e [type=npc, name=npc82] add npc82
tag @e [type=npc, name=npc83] add npc83
tag @e [type=npc, name=npc84] add npc84
tag @e [type=npc, name=npc85] add npc85
tag @e [type=npc, name=npc9] add npc9

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

tp @e [type=npc, tag=npc0] -30 -59 216
tp @e [type=npc, tag=npc1] -285 -59 243
tp @e [type=npc, tag=npc2] -257 -59 245
tp @e [type=npc, tag=npc3] -330 -53 242
tp @e [type=npc, tag=npc4] -342 -48 235
tp @e [type=npc, tag=npc5] -261 -43 244
tp @e [type=npc, tag=npc6] -263 -38 238
tp @e [type=npc, tag=npc7] -236 -33 234
tp @e [type=npc, tag=npc80] -288 -59 222
tp @e [type=npc, tag=npc81] -284 -53 228
tp @e [type=npc, tag=npc82] -281 -48 227
tp @e [type=npc, tag=npc83] -282 -43 227
tp @e [type=npc, tag=npc84] -281 -38 236
tp @e [type=npc, tag=npc85] -280 -33 226
