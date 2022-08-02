import math
PI = math.pi
def calculateTriArea(b, h):
    area = b * h / 2
    return area

def calculateCircArea(r):
    area = 2 * r * PI
    return area

print(calculateTriArea(2, 3))
print(calculateCircArea(9))