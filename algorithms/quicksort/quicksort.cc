// qucksort works good

#include <iostream>
#include <stdlib.h>
#include <stdio.h>

void swap(int *a, int *b){
  int temp = *a;
  *a = *b;
  *b = temp;
}

int partition(int arr[], int len, int h){
  int x = arr[h];
  int i = len - 1;

  for(int j=len;j<=h-1;j++){
    if (arr[j] <= x){
      i++;
      swap(&arr[i], &arr[j]);
    }
  }
  swap(&arr[i+1], &arr[h]);
  return i+1;
}

void quicksort(int arr[], int len, int h){
  if(len < h){
    int p = partition(arr, len, h);
    quicksort(arr, len, p-1);
    quicksort(arr, p+1, h);
  }
}

void print(int arr[], int len){
  for(int i=0;i<len;i++){
    std::cout << arr[i] << std::endl;
  }
}

int main(){
  int arr[] = {32, 43, 12, 9, 84, 5};
  int size = sizeof(arr)/sizeof(int);

  // print(arr, size);

  quicksort(arr, 0, size-1);

  print(arr, size);
}
