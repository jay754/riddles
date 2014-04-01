#include <iostream>

using namespace std;

int binarysearch(int a[], int size, int value);

int binarysearch(int a[], int size, int value){

    int low = 0;
    int high = size - 1;

    while (low <= high){

        int mid = (low + high) / 2;

        if(a[mid] > value){
            high = mid - 1;
        }
        else if (a[mid] < value){
            low = mid + 1;
        }
        else{
            return mid;
        }
    }

    return -1;
}

int main(){
    int a[] = {1, 3, 4, 8, 6};
    int size = sizeof(a)/sizeof(int);
    cout << binarysearch(a, size ,3) << endl;
}
	