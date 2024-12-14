
files = []

file_check = True
file_id = 0

def GetAvailableSpace(input, sizeNeeded):
    count = 0
    start = -1
    for i in range(0, len(input)):
        if input[i] == '.':
            if start == -1:
                start = i
            count += 1
            if count == sizeNeeded:
                return start
        else:
            count = 0
            start = -1
        
                
    return -1

with open("input.txt") as input_file:
    data = input_file.read()

    for char in data:
        size = int(char)
        next_char = '.'
        if file_check == True:
            next_char = str(file_id)
            file_id += 1
            file_check = False
        else :
            file_check = True

        for i in range(0, size):
            files.append(next_char)

free_index = 0
i = len(files) - 1
while i >= 0:
    if files[i] != '.':

        end_index = i
        char = files[i]
        while files[i] == char:

            i -= 1

        length = end_index - i


        available_start = GetAvailableSpace(files, length)

        if available_start != -1 and available_start < i:
            for j in range(0, length):

                files[available_start + j] = files[end_index - j]
                files[end_index - j] = '.'


        i += 1
    i -= 1


output = 0
for i in range(0, len(files) - 1):
    if files[i] != '.':
        output += i * int(files[i]) 

print(output)