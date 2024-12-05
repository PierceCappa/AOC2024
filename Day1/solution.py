import sys
import csv
import collections

right = []
left = []
with open("input.txt", newline='\n') as input_file:
    for row in input_file:
        row_output = row.split("   ")
        right.append(int(row_output[0]))
        left.append(int(row_output[1]))

counter_right = collections.Counter(right)

total = 0
for i in range(0, len(left)):
    total = total + (left[i] * counter_right[left[i]])

print(total)