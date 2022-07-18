#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 22-jun-2022
# Description: Code challenge from Lesson 6.3 (Triangle) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#PERSONAL NOTE: Easy challenge. Completed in few minutes.

""" An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647]. """

def solution(A):

    len_A = len(A)
    if(len_A < 3): return 0    
    A = sorted(A)

    for i in range(len_A - 2):
        p, q, r = A[i:i+3]
        if(p+q > r and p+r> q and r+q > p):
            return 1

    return 0

assert(solution([10,2,5,1,8,20]) == 1)
assert(solution([10,2,50]) == 0)
assert(solution([10,41,50]) == 1)
assert(solution([-10,2,50]) == 0)
assert(solution([-10,-2,0]) == 0)
assert(solution([range(1000000)]) == 0)