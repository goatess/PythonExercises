import math

def calculateTriArea(b, h):
    area = b * h / 2
    return area

def calculateCircArea(r):
    area = 2 * r * math.pi
    return area

print(calculateTriArea(2, 3))
print(calculateCircArea(9))