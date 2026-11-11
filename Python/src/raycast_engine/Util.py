import math


def distance(x1, y1, x2, y2):
    return math.sqrt(abs(x1 -x2)**2 + abs(y1 - y2)**2)

def getPointInDir(x, y, dist, dir):
    x = math.cos(math.radians(dir)) * dist + x
    y = math.sin(math.radians(dir)) * dist + y
    return x, y