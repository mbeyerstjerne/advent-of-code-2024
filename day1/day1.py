file = open('day1/input.txt', 'r')

def part1(file):    
    left_number = []
    right_number = []

    for line in file:
        numbers = line.split('   ')
        left_number.append(int(numbers[0]))
        right_number.append(int(numbers[1]))

    left_number.sort()
    right_number.sort()

    sum = 0

    for i in range(len(left_number)):
        diff = abs(left_number[i]-right_number[i])
        sum += diff

    print("The Answer to Part 1 is:", sum)

# part1(file)

from collections import Counter

def part2(file):
    left_number = []
    right_number = []

    for line in file:
        numbers = line.split('   ')
        left_number.append(int(numbers[0]))
        right_number.append(int(numbers[1]))

    left_number_counter = Counter(left_number)
    right_number_counter = Counter(right_number)

    sum_similarity = 0

    #multiply the number of times it appears on the left, by the number of times it appears on the right, by the value itself
    for key, value in left_number_counter.items():
        similarity = right_number_counter[key] * value * key
        sum_similarity += similarity
    
    print("The Answer to Part 2 is:", sum_similarity)

#part2(file)