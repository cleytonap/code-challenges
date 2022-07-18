
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 21-jun-2022
# Description: Code challenge from Lesson 5.2 (CountDiv) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------


""" Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] 
that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three 
numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B. """

def solution(A, B, K): 

    i = A

    while (i <= B and i % K != 0): #find first divisible in range [A, B]
        i += 1

    return (B - i) // K + 1



def solution1(A, B, K): #Brute force. Total Score: 50% (0% performance)
    count = 0
    for i in range(A, B+1):

        if i % K == 0:
            count +=1
    
    return count

print(solution(6,11,2)) # 3
print(solution(7,11,2)) # 2
print(solution(6,11,3)) #2
print(solution(0,11,3)) #4
print(solution(10,100,3)) #30
print(solution(10,100,30)) # 3
print(solution(10,100,300)) #0
print(solution(0,1,11)) #1
print(solution(0,100,1)) #101
