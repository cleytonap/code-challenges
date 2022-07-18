#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 17-jun-2022
# Description: Code challenge from Lesson 8.1 (Dominator) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

""" 
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

def solution(A)

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
 """
 
def solution (A):
    counts = {}

    if len(A) == 0: return -1

    if len(A) == 1: return 0

    for i,a in enumerate(A):
        if a in counts:
            counts[a] += 1
            if counts[a] > len(A)/2:
                return i        
        else:
            counts[a] = 1

    return -1 #There is no leader


# ----------------------------------------------------------------
#   TEST CASES
# ----------------------------------------------------------------

A = [ [],
      [1],
      [2,2,1,3,4,2,2],
      [2,2,1,3,4,2,2,6,2,2],
      [1,1,1,1,1,1,1,1,1,1,1],
      [1,2,3,4,5,6,3,3,3,2]]

RES = [-1,
       0,
       6,
       9,
       5,
       -1]

for i,a in enumerate(A):
    s = solution(a)
    print(f"Test case #{i+1}. A = {a}")
    print(f"Result: ", "PASS" if s == RES[i] else "FAIL !!!!!", f"Output: {s}. Expected: {RES[i]}") 
    print("----------------------------------------------------------------")
