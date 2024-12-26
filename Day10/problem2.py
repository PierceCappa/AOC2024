
input_map = []

def FindEnd(last_val: int, input_top, x: int, y: int) -> int:



    if x < 0 or x >= len(input_top[0]) or y < 0 or y >= len(input_top):
        return 0

    val = input_top[x][y]




    if val == last_val + 1:
        if val == 9:
            return 1
        score = 0
        score += FindEnd(val, input_top, x + 1, y)
        score += FindEnd(val, input_top, x - 1, y)
        score += FindEnd(val, input_top, x, y + 1)
        score += FindEnd(val, input_top, x, y - 1)
        return score

    return 0



with open("input.txt") as input_file:
    data = input_file.read()
    data = data.split('\n')

    for line in data:
        input_map.append([int(val) for val in line])

output = 0

for j in range(len(input_map)):
    for i in range(len(input_map[j])):
        if input_map[i][j] == 0:
            print(i, j, "New Path \n\n\n")
            output += FindEnd(-1, input_map, i, j)

print(output)