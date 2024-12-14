
files = []

file_check = True
file_id = 0

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
for i in range(len(files) - 1, -1, -1):
    if files[i] != '.':
        while files[free_index] != '.':
            free_index += 1
        if i < free_index:
            break
        files[free_index] = files[i]
        files[i] = '.'

output = 0
for i in range(0, len(files)):
    if files[i] != '.':
        output += i * int(files[i]) 
    else:
        break
print(output)