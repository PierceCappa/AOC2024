from math import *


map = []
antennas = {}

def PrintBoard(board):
    for row in board:
        print(row)

def ValidPoint(x, y, height, width):
    return x >= 0 and x < width and y >= 0 and y < height

def DistanceBetweenPoints(x1, y1, x2, y2):
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

def ReverseVector(vec):
    return (vec[0] * -1, vec[1] * -1)

def GetNewPoint(x, y, vx, vy):
    return (x + vx, y + vy)

def GetVector(x, y): 
    val = gcd(x, y)
    return (x / val, y / val)

def GetPoints(x1, y1, x2, y2, vx, vy, height, width, map):

    points = []
    points.append(GetNewPoint(x1, y1, vx, vy))
    points.append(GetNewPoint(x2, y2, vx * -1, vy * -1))

    nvx, nvy = GetVector(vx, vy)
    if nvx != vx and nvy != vy:
        while nvx != vx and nvy != vy:
            points.append(GetNewPoint(x1, y1, nvx, nvy))
            points.append(GetNewPoint(x2, y2, nvx * -1, nvy * -1))
            nvx + nvx
            nvy + nvy

    for (px, py) in points:

        if ValidPoint(px, py, height, width):

            d1 = DistanceBetweenPoints(x1, y1, px, py)
            d2 = DistanceBetweenPoints(x2, y2, px, py)

            if d1 / d2 == .5 or d2 / d1 == .5:
                map[px][py] = '#'

def GetAntinodes(point, other_antenna, height, width, maps):
    for other_point in other_antenna:
        if point != other_point:
            x1, y1 = point[0], point[1]
            x2, y2 = other_point[0], other_point[1]
            xv, yv = (x1 - x2, y1 - y2)

            GetPoints(x1, y1, x2, y2, xv, yv, height, width, maps)




with open("input.txt") as input_file:
    data = input_file.read()
    map = data.split("\n")
    map = [list(line.rstrip()) for line in map]


height = len(map)
width = len(map[0])


for row_index in range(0, height):
    for letter_index in range(0, width):
        if map[row_index][letter_index] != '.':
            antenna = map[row_index][letter_index]
            if antenna not in antennas:
                antennas[antenna] = []
            antennas[antenna].append((row_index, letter_index))
            


for key in antennas:
    for val in antennas[key]:
        GetAntinodes(val, antennas[key], height, width, map)


count = 0

for row in map:
    for item in row:
        if item == '#':
            count += 1

PrintBoard(map)
print(count)


