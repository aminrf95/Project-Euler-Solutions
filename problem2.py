#Problem 2:
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Approach 1:
#Generate the terms of the Fibonacci sequence, adding each even term to a running sum.

#Returns the sum of all even Fibonacci terms less than n.
def solution1(n):
    term1 = 1
    term2 = 1
    sum = 0
    next_term = 2
    while(next_term < n):
        next_term = term1 + term2
        if(next_term % 2 == 0):
            sum += next_term
        term1 = term2
        term2 = next_term
    return sum

if(__name__ == "__main__"):
    print(solution1(4000000))