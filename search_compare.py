#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignemnt Week Four"""

#import needed libraries
import random
import argparse
from pprint import pprint
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

def sequential_search(list, value):
    pos = 0
    found = False

    start = time.time()
    while pos < len(list) and not found:
        if list[pos] == value:
            found = True
        else:
            pos = pos + 1
    stop = time.time()
    duration = stop - start
    #print(duration)
    return duration, found

def ordered_sequential_search(list, value):
    pos = 0
    found = False

    start = time.time()
    while pos < len(list) and not found:
        if list[pos] == value:
            found = True
        else:
            pos = pos + 1
    stop = time.time()
    duration = stop - start
    # print(duration)
    return duration, found

def binary_search_iterative(list, value):
    first = 0
    last = len(list) - 1
    found = False

    start = time.time()

    while first <= last and not found:
        midpoint = (first + last) / 2

        if list[midpoint] == value:
            found = True
        else:
            if value < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    stop = time.time()
    duration = stop - start
    return duration, found

def binary_search_recursive(list, value):
    found = False

    start = time.time()

    if len(list) == 0:
        found = False
    else:
        midpoint = len(list) // 2
        if list[midpoint] == value:
            found = True
        else:
            if value < list[midpoint]:
                duration, found = binary_search_recursive(list[:midpoint], value)
            else:
                duration, found = binary_search_recursive(list[midpoint + 1:], value)

    stop = time.time()
    duration = stop - start
    return duration, found

def run_sequential_search():
    generated_list = generate_lists(500)

    total_duration_500 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration, value = sequential_search(generated_list[x], -1)

        total_duration_500 = total_duration_500 + duration
        # print x, duration, value

    average_500 = total_duration_500 / x
    #print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration, value = sequential_search(generated_list[x], -1)
        # print duration

        total_duration_1000 = total_duration_1000 + duration
        # print x, duration, value

    average_1000 = total_duration_1000 / x
    #print 'Average of 1,000', average_1000

    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration, value = sequential_search(generated_list[x], -1)
        # print duration

        total_duration_10000 = total_duration_10000 + duration
        # print x, duration, value

    average_10000 = total_duration_10000 / x
    #print 'Average of 10,000', average_10000

    final_avg_sequential = decimal.Decimal(average_500 + average_1000 + average_10000)

    return final_avg_sequential

def run_orsequential_search():
    #print 'hi'
    generated_list = generate_lists(500)

    total_duration_500 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        generated_list[x].sort()
        #print(generated_list[x])
        duration, value = ordered_sequential_search(generated_list[x], -1)

        total_duration_500 = total_duration_500 + duration
        #print x, duration, value

    average_500 = total_duration_500 / x
    #print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = ordered_sequential_search(generated_list[x], -1)
        # print duration

        total_duration_1000 = total_duration_1000 + duration
        # print x, duration, value

    average_1000 = total_duration_1000 / x
    #print 'Average of 1,000', average_1000

    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = ordered_sequential_search(generated_list[x], -1)
        # print duration

        total_duration_10000 = total_duration_10000 + duration
        # print x, duration, value

    average_10000 = total_duration_10000 / x
    #print 'Average of 10,000', average_10000

    final_avg_sequential = decimal.Decimal(average_500 + average_1000 + average_10000)

    return final_avg_sequential

def run_bsi_search():
    #print ' hi'
    generated_list = generate_lists(500)

    total_duration_500 = 0
    #pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = binary_search_iterative(generated_list[x], -1)

        total_duration_500 = total_duration_500 + duration
        #print x, duration, value

    average_500 = total_duration_500 / x
    #print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = binary_search_iterative(generated_list[x], -1)

        total_duration_1000 = total_duration_1000 + duration
        # print x, duration, value


    average_1000 = total_duration_1000 / x

    #print average_1000, total_duration_1000, x
    #print 'Average of 1000', average_1000


    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = binary_search_iterative(generated_list[x], -1)

        total_duration_10000 = total_duration_10000 + duration
        # print x, duration, value

    average_10000 = total_duration_10000 / x
    #print 'Average of 10,000', average_10000

    final_avg_sequential = decimal.Decimal(average_500 + average_1000 + average_10000)

    return final_avg_sequential

def run_bsr_search():
    #print ' hi'
    generated_list = generate_lists(500)

    total_duration_500 = 0
    #pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = binary_search_recursive(generated_list[x], -1)

        total_duration_500 = total_duration_500 + duration
        #print x, duration, value

    average_500 = total_duration_500 / x
    #print 'Average of 500', average_500

    generated_list = generate_lists(1000)

    total_duration_1000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        generated_list[x].sort()
        duration, value = binary_search_recursive(generated_list[x], -1)

        total_duration_1000 = total_duration_1000 + duration
        # print x, duration, value


    average_1000 = total_duration_1000 / x

    #print average_1000, total_duration_1000, x
    #print 'Average of 1000', average_1000

    generated_list = generate_lists(10000)

    total_duration_10000 = 0
    # pprint (generated_list)
    for x in range(1, 101):
        # print(generated_list[x])
        duration, value = binary_search_recursive(generated_list[x], -1)

        total_duration_10000 = total_duration_10000 + duration
        # print x, duration, value

    average_10000 = total_duration_10000 / x
    #print 'Average of 10,000', average_10000

    final_avg_sequential = decimal.Decimal(average_500 + average_1000 + average_10000)

    return final_avg_sequential

def main():

    calc_seq = run_sequential_search()
    print 'Sequential Search took {} seconds to run, on average'.format(round(calc_seq,7))

    calc_seq = run_orsequential_search()
    print 'Ordered Sequential Search took {} seconds to run, on average'.format(round(calc_seq, 7))

    calc_seq = run_bsi_search()
    print 'Recursive Binary Search took {} seconds to run, on average'.format(round(calc_seq, 7))

    calc_seq = run_bsr_search()
    print 'Sequential Search took {} seconds to run, on average'.format(round(calc_seq, 7))



    #Calculate the AVG Processing Time


if __name__ == "__main__":
    main()