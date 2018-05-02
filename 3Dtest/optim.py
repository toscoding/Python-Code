
import random
import cmath

c = 0  # total dans le cercle
r = 1*10**100
pim = cmath.pi
p = 0
total=0
while (p != pim):
    total = total + 1
    x = random.randrange(-r, r)
    y = random.randrange(-r, r)
    d = ((y * y) + (x * x))
    if ((r * r) >= d):
        c = c + 1
    co = total - c
    p = (4 * (c / total))
    print (p)


