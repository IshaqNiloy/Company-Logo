#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    letter_list = []
    letter_list = [x for x in s]
    letter_occur_dic = {}
    counter = 0
    for letter in letter_list:
        if letter not in letter_occur_dic.keys():
            letter_occur_dic[letter] = 1
        else:
            letter_occur_dic[letter] += 1
    
    dic_sorted_by_value_and_alphabet = sorted(letter_occur_dic.items(), key = lambda x:(-x[1],x[0]))
    
    for item in dic_sorted_by_value_and_alphabet:
        counter += 1
        print('{} {}'.format(item[0], item[1]))
        if counter == 3:
            break
