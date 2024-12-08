
map = []

Clear = '.'
Obsticle = '#'
Visited = 'X'

GuardDirection = (0, -1)
GuardPosition = (-1, -1)

bounds_x = -1
bounds_y = -1

def ChangeDirection(direction):
    if direction == (0, -1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, 1)
    elif direction == (0, 1):
        return (-1, 0)
    else:
        return (0, -1)

def NextPosition(direction, position):
    return position[0] + direction[0], position[1] + direction[1]

def PrintBoard(board):
    for row in board:
        print(row)

grid = []


with open("test.txt") as input_file:
    data = input_file.read()
    map = data.split("\n")
    map = [list(line.rstrip()) for line in map]

bounds_y = len(map)
bounds_x = len(map[0])

for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == "^":
            map[i][j] = Visited
            GuardPosition = (j, i)


next_x, next_y = NextPosition(GuardDirection, GuardPosition)

while next_x >= 0 and next_x < bounds_x and next_y >= 0 and next_y < bounds_y:
    # print(GuardPosition, GuardDirection)
    # PrintBoard(map)
    if map[next_y][next_x] == Obsticle:
        GuardDirection = ChangeDirection(GuardDirection)
    
    else:
        GuardPosition = (next_x, next_y)
        map[next_y][next_x] = Visited

    next_x, next_y = NextPosition(GuardDirection, GuardPosition)
    

count = 0
for i in range(0, len(map)):
    for j in range(0, len(map[j])):
        if map[i][j] == Visited:
            count += 1

print(bounds_x, bounds_y, GuardPosition)

print(count)
