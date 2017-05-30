#include <iostream>
#include <algorithm>

using namespace std;

bool validAnagram(string word1, string word2){
  std::sort(word1.begin(), word1.end());
  std::sort(word2.begin(), word2.end());

  if(word1.size() != word2.size()){
    return false;
  }

  for(int i;i<word1.size();i++){
    if(word1[i] != word2[i]){
      return false;
    }
  }

  return true;
}

int main(){
  string word1 = "tac";
  string word2 = "cat";
  std::cout << validAnagram(word1,word2) << '\n';
  return 0;
}
