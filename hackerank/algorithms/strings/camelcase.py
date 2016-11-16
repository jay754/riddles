"""
This questions are just tested withe test cases given by default/locally */

link: https://www.hackerrank.com/challenges/camelcase

CamelCase

"""

def camelcase(word):
    count = 1
    for i in word:
        if i.isupper(): count += 1
    return count

print camelcase("saveChangesInTheEditor")
