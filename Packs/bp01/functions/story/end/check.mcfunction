execute if score @p end_stage matches 0 run function story/end/notify
execute if score @p end_stage matches 1 run function story/end/q_check
execute if score @p end_stage matches 2 run function story/end/final_init
execute if score @p end_stage matches 3 run function story/end/f_check
execute if score @p end_stage matches 4 run function story/end/effects1
execute if score @p end_stage matches 4 run function story/end/complete