import math
#Problem 6:
# The sum of the squares of the first ten natural numbers is,
# 1^2+2^2+...+10^2=385
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#3025-385=2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#Approach 1: This problem can be solved by simply looping through the numbers 1 to 100, and keeping track of two running sums.
#The first running sum is just the sum of the first 100 natural numbers, and the second running sum is the sum of
#the squares of the first 100 natural numbers. We then return the difference between the square of the normal sum,
#and the the sum of squares.

def solution1():
    sum_squares = 0
    sum = 0
    for i in range(1,101):
        sum += i
        sum_squares += i*i
    return ((sum*sum) - sum_squares)


if(__name__ == "__main__"):
    print(solution1())
