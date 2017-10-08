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

def ordered_sequential_search():
    print 'os'

def binary_search_iterative():
    print 'bs'

def binary_search_recursive():
    print 'bsr'

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
    print 'Average of 500', average_500

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
    print 'Average of 1,000', average_1000

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
    print 'Average of 10,000', average_10000

    final_avg_sequential = decimal.Decimal(average_500 + average_1000 + average_10000)

    return final_avg_sequential

def main():

    calc_seq = run_sequential_search()
    print 'Sequential Search took {} seconds to run, on average'.format(round(calc_seq,5))



    #Calculate the AVG Processing Time


if __name__ == "__main__":
    main()