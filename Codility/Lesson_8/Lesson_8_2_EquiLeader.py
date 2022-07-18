#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 17-jun-2022
# Description: Code challenge from Lesson 8.2 (EquiLeader) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------


""" A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
 """

def getLeader(A):

    counts = {}

    if len(A) == 1: return 1, A[0]

    for i,a in enumerate(A):
        if a in counts:
            counts[a] += 1            
        else:
            counts[a] = 1

    for k in counts:
        if counts[k] > len(A)/2:
            return counts[k], k

    return 0, -1 #There is no leader


def checkEquiLeader(left_i_size, right_i_size, count_left, count_right):

    if(count_left > left_i_size / 2 and count_right > right_i_size / 2):
        return True
    
    return False


# Find the index S such that the leaders of the sequences A[0], A[1], ..., A[S] and 
# A[S + 1], A[S + 2], ..., A[N - 1] are the same.
def solution(A):

    if len(A) == 1: return 0

    leader_count, leader = getLeader(A)
  
    if(leader_count == 0):
        return 0

    res = 0

    count_left = 0 # count of leaders in the left side of index 'i'
    for i in range (len (A) -1 ):
        left_size = i + 1
        right_size = len(A) - left_size

        if(A[i] == leader):
            count_left += 1
            
        if(checkEquiLeader(left_size, right_size, count_left, leader_count - count_left)):
            res += 1
    
    return res


# ----------------------------------------------------------------
#   TEST CASES
# ----------------------------------------------------------------

A = [ [1,0,1,1,1,0,1,1,1,0,1], #11
      [4,3,4,4,4,2],
      [1],
      [2,2,1,3,4,2,2],
      [2,2,1,3,4,2,2,6,2,2],
      [1,1,1,1,1,1,1,1,1,1,1],
      [1,1,1,1,1,1,1,1,1,1],
      [1,0,2,2,0,3,2,2,0,5,1,2,2,2,2],
      [1,1,1,1,2,3,4,5,6,7,7]]

RES = [8,
       2,
       0,
       0,
       4,
       10,
       9,
       0,
       0,
       1
    ]

for i,a in enumerate(A):
    s = solution(a)
    print(f"Test case #{i+1}. A = {a}")
    print(f"Result: ", "PASS" if s == RES[i] else "FAIL !!!!!", f"Output: {s}. Expected: {RES[i]}") 
    print("----------------------------------------------------------------")
