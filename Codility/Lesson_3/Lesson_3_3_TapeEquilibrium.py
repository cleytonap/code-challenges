
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 17-jun-2022
# Description: Code challenge from Lesson 3.3 (TapeEquilibrium) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

""" A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

For example, consider array A such that:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
We can split this tape in four places:

P = 1, difference = |3 − 10| = 7
P = 2, difference = |4 − 9| = 5
P = 3, difference = |6 − 7| = 1
P = 4, difference = |10 − 3| = 7
Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

For example, given:

  A[0] = 3
  A[1] = 1
  A[2] = 2
  A[3] = 4
  A[4] = 3
the function should return 1, as explained above. """


def solution(A):
  
    totalSum = sum(A)
    leftSum = A[0]
    min_diff = float('inf')
    for i in range(1, len(A)):
        rightSum = totalSum - leftSum
        min_diff = min(min_diff, abs(leftSum - rightSum))
        leftSum += A[i]

    return min_diff

def solution2(A):

    min = 9999999999999 #lazy
    right_sum = sum(A)
    left_sum = 0
    for i in range(len(A) -1):

        left_sum += A[i] 
        right_sum -= A[i]

        res = abs(left_sum - right_sum)

        if(res < min):
            min = res

    return min

#------------------------------------------------------------------------------
# Test cases
#------------------------------------------------------------------------------

A = [[1,2],
     [-1,2],
     [3,3],
     [3,1,2,4,3],
     [4,5,1,5,7,9,0,0,1]
]

RES = [1,3,0,1, 2]

for i, a in enumerate(A):
    print(f'A = {a}. Expected: {RES[i]}. Output: {solution(a)}')