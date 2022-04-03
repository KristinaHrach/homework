import math
radius1 = 1
radius2 = 0.5
radius3 = 0.2
volume1 = 4 / 3 * math.pi * radius1 ** 3
volume2 = 4 / 3 * math.pi * radius2 ** 3
volume3 = 4 / 3 * math.pi * radius3 ** 3
sum1 = volume1 + volume2 
all_sum = sum1 + volume3
print(all_sum)
density_of_snow = 0.7
mass = density_of_snow * all_sum
print(mass)
