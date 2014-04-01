/*

http://en.wikipedia.org/wiki/Bubble_sort

Sorting algorithm

worst case performance: O(n)^2
best case performace: O(n)^2

*/

public class bubblesort {

        public static void main(String[] args){

                int[] Array = {5,6,4,8};

                list(Array);

        }

        public static void list(int a[]){

                for (int i = 1; i <= a.length;  i++) {

                        int count = i;

                        for(int j=i+1; j < a.length; j++){

                                if(a[count] > a[j]){
                                        int t = a[count];
                                        a[count] = a[j];
                                        a[j] = t;
                                }

                        }

                }

                for (int Item : a){
                        System.out.println(Item);
                }

        }

}