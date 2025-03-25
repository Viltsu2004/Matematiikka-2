import math

import numpy as np


#Teht 1 a) ja b)
a = 2.493
b = 0.911

print(f'\n{np.degrees(a):.3f}°')
print(f'\n{np.degrees(b):.3f}°')

#Teht 2. a) ja b)
c = 137.7
d = 62.3

print(f'\n{np.radians(c):.3f}°')
print(f'\n{np.radians(d):.3f}°')

#Teht.3
matik_lst = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for l in matik_lst:
    print(f'\n{np.radians(l):.4} rad')

