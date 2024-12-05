import re

sum = 0


with open("input.txt", 'r') as input_file:
    index = 0
    content = input_file.read()

    do_val = True

    while len(content) != 0:

        index = content.find("mul(")
        do_index = content.find("do()")
        dont_index = content.find("don't()")

        if do_index == -1:
            do_index = 99999

        if dont_index == -1:
            dont_index = 99999

        if index == -1:
            #done
            break

        if do_index < index and do_index < dont_index and do_index != -1:
            do_val = True
            content = content[do_index + 4:]
        elif dont_index < index and dont_index < do_index and dont_index != -1:
            do_val = False
            content = content[dont_index + 7:]
        else:

            
            content = content[index + 4:]

            if do_val == True:

                num_one = 0

                index = 0
                valid_num = True

                num_one = content[:content.find(",")]
                if len(num_one) < 4:

                    content = content[content.find(",") + 1:]

                    if num_one.isdigit() == True:
                        num_two = content[:content.find(")")]
                        if len(num_two) < 4:
                            content = content[content.find(")") + 1:]
                            if num_two.isdigit() == True:
                                print(num_one)
                                print(num_two)
                                sum += int(num_one) * int(num_two)
print(sum)

