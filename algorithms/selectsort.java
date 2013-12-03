/*

http://en.wikipedia.org/wiki/Select_sort

Sorting algorithm

worst case performance: O(n)^2
best case performace: O(n)^2

*/

public class selectsort {

        public static void main(String[] args){

                int[] list = {10, 3, 6, 11, 14, 7};

                for (int Item : list){
                        System.out.println(Item);
                }

                Sort(list);

        }

        public static void Sort(int[] a) {

                for (int i = 0; i < a.length; i++) {

                        int count = i;

                        for (int j = i + 1; j < a.length; j++ ){

                                if (a[count] > a[j]){
                                        count = j;
                                }

                        int holder = a[i];
                        a[i] = a[count];
                        a[count] = holder;

                        }

                }

                for (int Item : a) {
                        System.out.println(Item);
                }        
        }
}