#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

bool divisible(int num){
	int i;

	for(i = 1; i<20;i++){
		if (num % i != 0){
			return false;
		}
	}

	return true;
}

int main(int argc, char **argv){
	// int bob = 10;

	int i = 1;

	while (true){
		if (divisible(i)){
			printf("%d\n", i);
			break;
		}

		i++;
	}

	return 1;
}