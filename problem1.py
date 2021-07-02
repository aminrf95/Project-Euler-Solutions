#Problem 1 from Project Euler:
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#Approach1:
#First we find all of the multiples of 3 below 1000.
#Next, we find all of the multiples of 5 below 1000.
#Then, we sum all of the values of the UNION of these two sets (numbers that are multiples of both 3 and 5 should not be summed twice).

#Returns the sum of all the multiples of 3 or 5 below 1000.
def solution1():
    mult3 = set(multiples_of_three(1000))
    mult5 = set(multiples_of_five(1000))
    mult3_and_5 = mult3.union(mult5)
    return sum(mult3_and_5)

#Approach2:
#The above approach does redundant work by doing multiple loops through the numbers 1 to 1000.
#We can simplify this by doing a single loop and keeping a running sum, adding values that are either multiples of 3 or 5.
#This will still give us a runtime of O(n).

#Returns the sum of all the multiples of 3 or 5 below 1000.
def solution2():
    sum = 0
    max = 1000
    for i in range(1,max):
        if(i % 3 == 0 or i % 5 == 0):
            sum += i
    return sum

#Approach3:
#We are still doing extraneous work in the above approach.
#We do not have to check every value from 1 to 1000, as we can directly generate the multiples of 3 and 5
#by executing 3*i and 5*i for i = 1,2,3... while 3*i < 1000.
#Since 3*i is always less than 5*i for i = 1,2,3.., we will always add 5*i to our running sum (if 5*i < 1000),
#and only add 3*i to our running sum if it is NOT a multiple of 5, so as to avoid double-counting.
#The while loop will execute 1000/3 times, giving us a runtime of O(n/3), which is still just O(n).

#Returns the sum of all the multiples of 3 or 5 below 1000.
def solution3():
    sum = 0
    max = 1000
    i = 1
    while(3*i < max):
        if(5*i < max):
            sum += 5*i
        if(3*i % 5 != 0):
            sum += 3*i
        i += 1
    return sum

#Returns a list of all multiples of 3 below max.
def multiples_of_three(max):
    multiples = []
    for i in range(1,max):
        if(i % 3 == 0):
            multiples.append(i);
    return multiples

#Returns a list of all multiples of 5 below max.
def multiples_of_five(max):
    multiples = []
    for i in range(1,max):
        if(i % 5 == 0):
            multiples.append(i);
    return multiples

if(__name__ == "__main__"):
    print(solution3())
