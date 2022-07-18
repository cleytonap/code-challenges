#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 20-jun-2022
# Description: Code challenge from Lesson 4.4 (MissingIntegers) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------


""" This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
 """

def solution(A):
    
    sort = sorted(set(A)) # set() --> remove duplicates

    if(sort[-1] <= 0):
        return 1
    
    offset = 0
    while(sort[offset] <= 0): # disregards negative numbers (or zero)
        offset += 1
    
    for i in range(len(sort)-offset):
        if (sort[i + offset] != i + 1):
            return i + 1
        
    return i+2