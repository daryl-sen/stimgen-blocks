import random

color_indices = random.sample(range(0,4),2)
alt_indices = random.sample(range(0,4),2)
while (alt_indices == color_indices) or (alt_indices[0] in color_indices) or (alt_indices[1] in color_indices):
    print(f'Regenerating..({alt_indices}) not acceptable')
    alt_indices = random.sample(range(0,4),2)

print(0 in [1,0])
print(color_indices)
print(alt_indices)