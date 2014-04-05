import math

def triplets():
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                print a*b*c
                break

triplets()
