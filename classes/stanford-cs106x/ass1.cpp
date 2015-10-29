//assignment number1

#include <iostream>
#include <stdlib.h>
#include <algorithm>
#include <string.h>

// exercise number 1

int flip(){
  return rand()%2;
}

void heads(){
  int count = 0;
  int i = 0;
  std::string word;

  while(count < 3){
    if(flip()==0){
      word = "tails";
    }

    if(flip()==1){
      word = "heads";
      count++;
    }
    else{
      count = 0;
    }

    std::cout << word << std::endl;
    i++;
  }

  std::cout << i << std::endl;
}

int nCr(int n, int r){
  if(r==0){
    return 1;
  }
  else if(r==n){
    return 1;
  }
  else{
    nCr(n-1, r-1) + nCr(n-1,r);
  }
}

int main(){
  return 0;
}

//
