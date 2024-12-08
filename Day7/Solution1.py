
count = 0

def TestResult(sum, goal, index, values):
    if index == len(values) - 1:
        if sum == goal:
            return True
        return False
    
    next_index = index + 1
    next_value = sum + values[next_index]

    if TestResult(next_value, goal, next_index, values) == True:
        return True
    
    next_value = sum * values[next_index]

    if TestResult(next_value, goal, next_index, values) == True:
        return True
    
    next_value = int(str(sum) + str(values[next_index]))
    
    if TestResult(next_value, goal, next_index, values) == True:
        return True
    
    return False

with open("input.txt", newline='\n') as input_file:
    for line in input_file:
        parts = line.split(":")
        goal = int(parts[0])
        values = [int(value) for value in parts[1].rstrip().split(" ")[1:]]
        if TestResult(values[0], goal, 0, values) == True:
            count += goal


print(count)