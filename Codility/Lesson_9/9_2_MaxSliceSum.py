
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 18-jun-2022
# Description: Code challenge from Lesson 9.2 (MaxSliceSum) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

""" A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

For example, given array A such that:

A[0] = 3  A[1] = 2  A[2] = -6
A[3] = 4  A[4] = 0
the function should return 5 because:

(3, 4) is a slice of A that has sum 4,
(2, 2) is a slice of A that has sum −6,
(0, 1) is a slice of A that has sum 5,
no other slice of A has sum greater than (0, 1).
Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000];
each element of array A is an integer within the range [−1,000,000..1,000,000];
the result will be an integer within the range [−2,147,483,648..2,147,483,647].
 """
def solution(A):
    
    max_ending = max_slice = A[0]
    for i in range(1, len(A)):
        a = A[i]
        max_ending = max(a, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice


print(solution([3,2,-6,4,0,3]))
print(solution([-3,-2,-6,-4])) # -2
print(solution([3,2,-6,4,0])) # 5
