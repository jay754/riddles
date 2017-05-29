include <iostream>
include <string>

using namespace std;

int removeElement(int param[],int k, int size){
  int del = 0;
  for(int i=0;i<size;i++){
    if(param[i] == k){
      del++;
    }
  }
  return size-del;
}

int main(){
  return 0;
}
