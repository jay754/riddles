/*

http://projecteuler.net/problem=10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

This should've been done using Sieve.

*/

public class euler10 {

	public static boolean isPrime(int n){
        if(n<2){
            return false;
        }
        else if(n==2 || n==3){
            return true;
        }
        else if(n%2==0){
            return false;
        }
        for(int i=3;i<=Math.ceil(Math.sqrt(n));i+=2){
            if(n%i==0){
                return false;
            }
        }
        return true;
    }
    //142913828922
    public static void main(String []args){
        long n=2;
        
        for(int i=3;i<2000000;i+=2){
            if(isPrime(i)){
                n = n + i;
            }
        }
        System.out.println(n);
    }

}