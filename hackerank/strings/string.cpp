#include <iostream>
#include <stdlib.h>
#include <string>

/* This questions are just tested withe test cases given by default/locally */ 

/*

Hacker Rank number 3

alternating characters

*/

int characters(std::string word){
	int i=1;
	int count = 0;

	for(i;i < word.length();i++){
		if( word[i-1] == 'A'){
			if(word[i] == 'A'){
				count += 1;
			}
		}
		else if(word[i-1]=='B'){
			if(word[i]=='B'){
				count += 1;
			}
		}
	}

	return count;
}

/*

https://www.hackerrank.com/challenges/two-strings

*/

bool sub(std::string input1, std::string input2){
	int i=0;
	for(i=0;i<input1.length();i++){
		if(input2.find(input1[i]))	
			return true;
	}
	return false;
}

/*

This solution isn't correct, but is pretty close

https://www.hackerrank.com/challenges/common-child

def test(input1, input2):
	map1 = {}
	map2 = {}

	for i in range(len(input1)):
		if input1[i] not in map1:
			if input1[i] in input2:
				map1[input1[i]] = i

	for i in range(len(input2)):
		if input2[i] not in map2:
			if input2[i] in input1:
				map2[input2[i]] = i

	result_dict = {}

	result = map1.keys()[0]
	result_position = 0

	for i in range(len(map1.keys())):
		if map2[map2.keys()[i-1]] >= map1[map1.keys()[i]]:
			result = map1.keys()[i]
			result_position = map1[result]

	if map1[result] > map2[result]:
		result_position = map2[result]
	
	for i in range(len(map1.keys())):
		if map2[map2.keys()[i-1]] > result_position and map1[map1.keys()[i-1]] > result_position:
			if map2.keys()[i-1] not in result:
				result += map2.keys()[i-1]

	print result, map1, map2

test("SHINCHAN", "NOHARAAA")

*/

int main(){
	return 0;
}