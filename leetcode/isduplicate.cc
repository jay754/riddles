#include <iostream>

using namespace std;

bool isDuplicate(int params[], int size){
  sort(params, params+size);
  for(int i=0;i<size;i++){
    if(params[i]==params[i+1]){
      return true;
    }
  }
  return false;
}

int main(){
  int a[4] = {2,23,5,5};
  cout << isDuplicate(a,4) << endl;
  return 0;
}
