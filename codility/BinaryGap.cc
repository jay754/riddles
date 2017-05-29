#include <iostream>
#include <string>

using namespace std;

int binaryGap(string b){
  int count=0;
  int max=0;
  for(int i=0;i<b.size();i++){
    if(b[i]=='0' && b[i+1]=='0'){
      count++;
    }else{
      if(count>max){
        max = count;
      }
      count = 0;
    }
  }
  return max+1;
}

int main(){
	std::cout << binaryGap("10100011000000") << '\n';
	return 0;
}
