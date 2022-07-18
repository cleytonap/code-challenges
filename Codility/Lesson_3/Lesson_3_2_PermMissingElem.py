#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 17-jun-2022
# Description: Code challenge from Lesson 3.2 (PermMissingElem) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

""" An array A consisting of N different integers is given. The array contains integers in the range 
[1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)]. """

def solution(A):
   
    if(len(A) == 0): return 1
    
    sum_obtained = 0
    sum_expected = 0
    for i, e in enumerate(A):
        sum_obtained += e
        sum_expected += i
    
    sum_expected += (i+1) + (i+2)
    
    return sum_expected - sum_obtained


def solution2(A):

    sort = [i for i in range(len(A)+2)]

    for e in A:
        sort[e] = 0

    return sum(sort)