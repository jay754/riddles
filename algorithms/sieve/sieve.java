/*

http://introcs.cs.princeton.edu/java/14array/PrimeSieve.java.html
http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Purpose: finding prime numbers

bit complexity: O(n(log n)(log log n)) -> Idk even know what this is man I just found it on wikipedia and know that its a good big O.

*/

public class sieve {

	public static void main(String[] args) { 
        int N = Integer.parseInt(args[0]);

        // initially assume all integers are prime
        boolean[] isPrime = new boolean[N + 1];
        for (int i = 2; i <= N; i++) {
            isPrime[i] = true;
        }

        // mark non-primes <= N using Sieve of Eratosthenes
        for (int i = 2; i*i <= N; i++) {

            // if i is prime, then mark multiples of i as nonprime
            // suffices to consider mutiples i, i+1, ..., N/i
            if (isPrime[i]) {
                for (int j = i; i*j <= N; j++) {
                    isPrime[i*j] = false;
                }
            }
        }

        // count primes
        int primes = 0;
        for (int i = 2; i <= N; i++) {
            if (isPrime[i]) primes++;
        }
        System.out.println("The number of primes <= " + N + " is " + primes);
    }
	
}