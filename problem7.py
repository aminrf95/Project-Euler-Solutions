import math
#Problem 7:
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

#Approach 1: This problem can be solved by using the factors function from problem 3.
#We simply keep a counter of primes starting at 0, and a counter i starting at 2.
#In the body of a while loop we increment the prime counter if i is prime by checking if it has only two factors.
#We then increment i, and loop until we reach the 10001st prime.

def solution1():
    i = 2
    prime_count = 0
    prime = -1
    while(prime_count < 10001):
        if(len(factors(i)) == 2):
            prime_count += 1
            prime = i
        i += 1
    return prime


#Returns a list of all factors of n
def factors(n):
    if(n == 2):
        return [1,2]
    factors = []
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if(n % i == 0):
            factors.append(i)
    for f in reversed(factors):
        if(f*f != n):
            factors.append(n/f)
    return factors

if(__name__ == "__main__"):
    print(solution1())
