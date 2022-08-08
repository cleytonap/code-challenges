#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 17-jun-2022
# Description: Code challenge from Lesson 2.2 (OddOccurrencesInArray) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------



""" A non-empty array A consisting of N integers is given. The array contains an odd number of elements, and each element of the array can be paired with another element that has the same value, except for one element that is left unpaired.

For example, in array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.
Write a function:

def solution(A)

that, given an array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7, as explained in the example above.

Write an efficient algorithm for the following assumptions:

N is an odd integer within the range [1..1,000,000];
each element of array A is an integer within the range [1..1,000,000,000];
all but one of the values in A occur an even number of times. """


def solution(A):

    setA = set(A)

    for e in A:
        if e in setA:
            setA.remove(e)
        else:
            setA.add(e)
    
    return setA.pop()

def solution2(A):
    
    counts = {}

    for i, e in enumerate(A):

        if(e in counts):
            counts[e] = counts[e] + 1
        else:
            counts[e] = 1
    
    for e in counts:
        if (counts[e] % 2 != 0):
            return e
    
    return -1 # error!


def solution3(A):
    
    if(len(A) == 1): return A[0]

    aux = [] # Using list I get TIMEOUT ERROR in the performance tests. It works if set is used instead of list !!! 
             # Sets are way faster than lists when using the 'in' operator

    for a in A:
        
        if a in aux:
            aux.remove(a)
        else:
            aux.append(a)
    
    return aux[0]

