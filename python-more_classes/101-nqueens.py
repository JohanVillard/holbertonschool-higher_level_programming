#!/usr/bin/python3

# Put the queen_1 at 0, 0
#   Safe ? queen_1 vs None
#       True: Put the queen_2 at 1, 0

#           Safe ? queen_1 vs queen_2
#           False: Move queen_2 at 1, 1
#           Safe ? queen_1 vs queen_2
#           False: Move queen_2 at 1, 2
#           Safe ? queen_1 vs queen_2
#               True: Put the queen_3 at 2, 0

#               Safe ? queen_1 vs queen_3
#               False: Move queen_3 at 3, 0
#               Safe ? queen_1 vs queen_3
#               False: Move queen_3 at 3, 1
#               Safe ? queen_1 vs queen_3
#               False: Move queen_3 at 3, 2
#               Safe ? queen_1 vs queen_3
#               False: Move queen_3 at 3, 3
#               Safe ? queen_1 vs queen_3
#               False: Move queen_3 at 3, 4
#                   True: Put the queen_N at N, 0
#               ---------------------------------

# current_solution[8]

## col 0
for row0 = 0 to N

