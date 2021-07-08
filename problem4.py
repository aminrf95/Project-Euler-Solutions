from math import floor
#Problem 4:
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

#Approach 1: We can solve this problem by simply iterating through all tuples (i,j) where 99 < i, j < 1000, and checking if i * j
#is a palindrome, while keeping track of the maximum-value palindrome seen thus far.

#Checks if the string s is a palindrome
def check_palindrome(s):
    for i in range(0,floor(len(s)/2)):
        if(s[i] != s[len(s)-i-1]):
            return False
    return True

if(__name__ == "__main__"):
    max = 0
    for i in range(999,99,-1):
        for j in range(i,99,-1):
            val = i * j
            if(check_palindrome(str(val)) and val > max):
                max = val
    print(max)
