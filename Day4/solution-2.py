def CheckDiag(L1, L2):
    if L1 == "M" and L2 == "S" or L1 == "S" and L2 == "M":
        return True
    
    return False

count = 0


with open("temp.txt", newline='\n') as input_file:
    content = input_file.read()
    content.replace('\r', '')

    word_matrix = content.split("\n")

    height = len(word_matrix)
    width = len(word_matrix[height - 1])

    max_x_index = width - 1
    max_y_index = height - 1

    for y in range(1, max_y_index):
        for x in range(1, max_x_index):
            
            if word_matrix[y][x] == 'A':
                if CheckDiag(word_matrix[y-1][x-1], word_matrix[y+1][x+1]) and CheckDiag(word_matrix[y+1][x-1], word_matrix[y-1][x+1]):
                    count += 1


print(count)



