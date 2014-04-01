/*

http://en.wikipedia.org/wiki/Prime_number

Purpose: finding whether or not a number is a prime number 

WARNING: A word of advice anytime you have to find a prime number use this

Otherwise you should use Sieve of Eratosthenes.

*/

public class prime {

	public static void main(String[] args) {
        System.out.println(isPrime(99));
    }
        
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
}