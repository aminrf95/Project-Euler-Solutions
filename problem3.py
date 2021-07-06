import math
#Problem 3:
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#Approach 1: We split this problem into two parts. First we find all of the factors of our target number n.
#Next, for each factor f (starting with the largest factor), we find the factors of f.
#The first f that has only two factors will be the largest prime factor.
#Both parts rely on a subroutine that returns a list of factors for a given natural number n.
#This subroutine can be implemented by finding all i <= sqrt(n) such that n % i == 0.
#Every such i and n/i will be a factor (with special care taken not to double count sqrt(n)).

def solution1(n):
    #Find all factors of n
    factor_list = factors(n)
    #Starting with the largest factor and working down,
    #check if the factor is prime by finding its list of factors.
    #If the list only contains 2 elements, it is prime.
    #Return the first prime factor.
    for f in reversed(factor_list):
        if(len(factors(f)) == 2):
            return f
    return -1

#Returns a list of all factors of n
def factors(n):
    factors = []
    for i in range(1,math.ceil(math.sqrt(n))+1):
        if(n % i == 0):
            factors.append(i)
    for f in reversed(factors):
        if(f*f != n):
            factors.append(n/f)
    return factors

if(__name__ == "__main__"):
    print(solution1(600851475143))
