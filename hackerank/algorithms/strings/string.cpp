#include <iostream>
#include <stdlib.h>
#include <string>

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

int main(){
	return 0;
}
