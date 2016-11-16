"""

print all the characters present in the given string only once in a reverse order.
Time & Space complexity should not be more than O(N).

e.g.
1)Given a string aabdceaaabbbcd
the output should be - dcbae

2)Sample String - aaaabbcddddccbbdaaeee
Output - eadbc

3)I/P - aaafffcccddaabbeeddhhhaaabbccddaaaa
O/P - adcbhef

"""

def question1(word):
    result = list()
    for i in word[::-1]:
        if i not in result:
            result.append(i)
    return "".join(result)

print question1("aaaabbcddddccbbdaaeee")
