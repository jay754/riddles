/*

http://en.wikipedia.org/wiki/Euclidean_algorithm

Purpose: for finding the gcd for 2 integers

*/

public class euclediangcd {

        public static int gcd(int a, int b){

                if (b == 0) {
                        return a;
                }
                else {
                        return gcd(b, (a % b));
                }

        }
        
        public static void main(String[] args){

                System.out.println(gcd(119, 84));

        }
}