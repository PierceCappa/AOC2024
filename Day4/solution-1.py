
#NOTE: this is terrible. I feel bad after coding this. Please do not judge me for the horror below.

word = "XMAS"
word_length = len(word)

count = 0

def CheckWord(input, target):
    if input == target or input[::-1] == target:
        return True


with open("input.txt", newline='\n') as input_file:
    content = input_file.read()
    content.replace('\r', '')

    word_matrix = content.split("\n")

    height = len(word_matrix)
    width = len(word_matrix[height - 1])

    max_x_index = width - word_length
    max_y_index = height - word_length


    for y in range(height):
        for x in range(width):

            if x <= max_x_index:
                test_word = word_matrix[y][x:x + word_length]
                if CheckWord(test_word, word):
              
                    count += 1

            if y <= max_y_index:
                rows = word_matrix[y: y + word_length]
                test_word = ""
                for row in rows:
                    test_word += row[x]

                if CheckWord(test_word, word):

                    count += 1


            if x <= max_x_index and y <= max_y_index:
                rows = word_matrix[y: y + word_length]
                test_word = ""
                index = 0

                for row in rows:
                    test_word += row[x + index]
                    index += 1


                if CheckWord(test_word, word):
           

                    count += 1

            if x - word_length >= -1 and y <= max_y_index:
                rows = word_matrix[y: y + word_length]
                test_word = ""
                index = 0

                for row in rows:
                    test_word += row[x - index]
                    index += 1



                if CheckWord(test_word, word):

                    count += 1


            

print(count)
