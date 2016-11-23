"""
This questions are just tested withe test cases given by default/locally */

link: https://www.hackerrank.com/challenges/beautiful-binary-string/

Beautiful Binary String

"""

import re
from cmath import polar
from itertools import permutations

def BeautifulBinaryString(string):
    return len(re.findall("010", "0100101010"))

# def BeautifulBinaryString(string):
#     count = 0
#     for i in range(len(string)-2):
#         if string[i:i+3] == "010":
#             count += 1
#
#     if count == 0:
#         return 0
#     else:
#         return count-1

# print BeautifulBinaryString("0100101010")

nums = raw_input().split(" ")
top = set(float(i) for i in nums)
print format(sum(top)/len(top))
