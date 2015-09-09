#include <iostream>
#include <stdlib.h>
#include <stdio.h>

void merge(int a[], int length, int mid, int r);

void mergeSort(int array[], int left, int right){
  if(left < right){
    int mid = left+(right-left)/2;
    mergeSort(array, left, mid);
    mergeSort(array, mid+1, right);
    merge(array, left, mid, right);
  }
}

void merge(int a[], int left, int mid, int right){
  int i, j, k;
  int leftSize = mid - left + 1;
  int rightSize = right - mid;

  int leftArray[leftSize];
  int rightArray[rightSize];

  for(i=0;i<leftSize;i++){
    leftArray[i] = a[left+1];
  }

  for(j=0;j<rightSize;j++){
    rightArray[j] = a[mid + 1 + j];
  }

  i = 0;
  j = 0;
  k = left;

  while(i < leftSize && j < rightSize){
    if (leftArray[i] <= rightArray[j]){
      a[k] = leftArray[i];
      i++;
    }
    else{
      a[k] = rightArray[j];
      j++;
    }
    k++;
  }

  while(i < leftSize){
    a[k] = leftArray[i];
    i++;
    k++;
  }

  while(j < rightSize){
    a[k] = rightArray[j];
    j++;
    k++;
  }
}

void print(int array[], int length){
  for(int i=0;i<length;i++){
    std::cout << array[i] << std::endl;
  }
}

int main(){
  int array[] = {21, 41,5, 4,19,34};
  int size = sizeof(array)/sizeof(int);
  // print(array, size);

  mergeSort(array, 0, size - 1);
  print(array, size);
  return 0;
}
