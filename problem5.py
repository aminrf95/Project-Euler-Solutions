import math
#Problem 5:
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Approach 1: We can find the least common multiple by examining all of the prime factorizations for the numbers 1 to 20,
#and then multiplying each prime factor with the highest power.
#To do this, we will keep a dictionary of primes below 20 that map to the highest power we have seen so far.
#For each number from 2 to 20, we will count how many times each prime factor divieds the number, and compare that count
#with the value in our dictionary, updating the dictionary if it is a larger value.
#When we are finished with this, we multiply the factors raised to the powers stored in the dictionary, and output the value.

def solution1():
    primes = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0,
        13: 0,
        17: 0,
        19: 0
    }

    for i in range(2,21):
        num = i
        for f in primes.keys():
            f_count = 0
            while(num % f == 0):
                f_count += 1
                num = num / f
            primes[f] = max(primes[f], f_count)

    out = 1
    for f in primes.keys():
        out *= math.pow(f,primes[f])
    return out


if(__name__ == "__main__"):
    print(solution1())
