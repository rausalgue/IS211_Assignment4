#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Four Part 2"""

#import needed libraries
import random
import time
import decimal

def generate_lists (size):
    #print size
    iteration = 0
    list_dict = {}

    for lp in range(100):
        iteration +=1
        list_dict [iteration] = random.sample(range(1,100000), size)
        #print lp

    return list_dict

def insertion_sort(list):
    start = time.time()

    for index in range(1, len(list)):
        current_value = list[index]

        position = index

        while position > 0 and list[position - 1] > current_value:
            list[position] = list[position - 1]
            position = position - 1

        list[position] = current_value

    stop = time.time()
    duration = stop - start
    # print(duration)
    return duration

def shell_sort(list):
    start = time.time()
    sublist_count = len(list) // 2

    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is",list)

        sublist_count = sublist_count // 2

    stop = time.time()
    duration = stop - start
    # print(duration)
    return duration

def gap_insertion_sort(list, start, gap):
    for i in range(start + gap, len(list), gap):
        current_value = list[i]
        position = i

        while position >= gap and list[position - gap] > current_value:
            list[position] = list[position - gap]
            position = position - gap
            list[position] = current_value

def python_sort(list):
    start = time.time()

    list.sort()

    stop = time.time()
    duration = stop - start
    # print(duration)
    return duration

def run_insertion_sort():
    generated_list = generate_lists(500)

    total_duration_500 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = insertion_sort(generated_list[x])

        total_duration_500 = total_duration_500 + duration
        #print x, duration

    average_500 = total_duration_500 / x
    print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = insertion_sort(generated_list[x])

        total_duration_1000 = total_duration_1000  + duration
        #print x, duration


    average_1000 = total_duration_1000  / x
    print 'Average of 1,000', average_1000

    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = insertion_sort(generated_list[x])

        total_duration_10000 = total_duration_10000 + duration
        #print x, duration

    average_10000 = total_duration_10000 / x
    print 'Average of 10,000', average_10000

    final_avg = decimal.Decimal(average_500 + average_1000 + average_10000)
    return final_avg

def run_shell_sort():
    generated_list = generate_lists(500)

    total_duration_500 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = shell_sort(generated_list[x])

        total_duration_500 = total_duration_500 + duration
        #print x, duration

    average_500 = total_duration_500 / x
    print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = shell_sort(generated_list[x])

        total_duration_1000 = total_duration_1000 + duration
        # print x, duration

    average_1000 = total_duration_1000 / x
    print 'Average of 1,000', average_1000

    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = shell_sort(generated_list[x])

        total_duration_10000 = total_duration_10000 + duration
        # print x, duration

    average_10000 = total_duration_10000 / x
    print 'Average of 10,000', average_10000

    final_avg = decimal.Decimal(average_500 + average_1000 + average_10000)
    return final_avg

def run_python_sort():
    generated_list = generate_lists(500)

    total_duration_500 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = python_sort(generated_list[x])

        total_duration_500 = total_duration_500 + duration
        # print x, duration

    average_500 = total_duration_500 / x
    print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = python_sort(generated_list[x])

        total_duration_1000 = total_duration_1000 + duration
        # print x, duration

    average_1000 = total_duration_1000 / x
    print 'Average of 1,000', average_1000

    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration = python_sort(generated_list[x])

        total_duration_10000 = total_duration_10000 + duration
        # print x, duration

    average_10000 = total_duration_10000 / x
    print 'Average of 10,000', average_10000

    final_avg = decimal.Decimal(average_500 + average_1000 + average_10000)
    return final_avg

def main():
    calc_seq = run_shell_sort()
    print 'Shell Sort took {} seconds to run, on average'.format(round(calc_seq,7))

    calc_seq = run_python_sort()
    print 'Python Sort took {} seconds to run, on average'.format(round(calc_seq,7))

    calc_seq = run_insertion_sort()
    print 'Insertion Sort took {} seconds to run, on average'.format(round(calc_seq, 7))

if __name__ == "__main__":
    main()