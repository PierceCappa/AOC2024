
safe = 0


def CheckFloor(input) -> bool:
    increasing = None
    last_value = input[0]
    for next_value in input[1:]:
        
        if next_value > last_value:
            if increasing == None:
                increasing = True
            elif increasing == False:
                return False
        elif next_value < last_value:
            if increasing == None:
                increasing = False
            elif increasing == True:
                return False
        else:
            return False

        if abs(next_value - last_value) > 3:
            return False
        last_value = next_value


    return True



with open("input.txt", newline='\n') as input_file:
    for row in input_file:
        row_data  = row.split(" ")
        row_data = [int(x) for x in row_data]

        failure = True

        if CheckFloor(row_data) == False:
            for i in range(0, len(row_data)):
                outcome = None
                if i == 0:
                    outcome = CheckFloor(row_data[1:])
                elif i == len(row_data) - 1:
                    outcome = CheckFloor(row_data[:len(row_data) - 1])
                else:
                    outcome = CheckFloor(row_data[:i] + row_data[i + 1:])

                if outcome == True:
                    failure = False
                    break
        else:
            failure = False
            
        if not failure:
            safe += 1


print(safe)