#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 20-jun-2022
# Description: Code challenge from Lesson 4.3 (MaxCounters) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

""" You are given N counters, initially set to 0, and you have two possible operations on them:

increase(X) − counter X is increased by 1,
max counter − all counters are set to the maximum value of any counter.
A non-empty array A of M integers is given. This array represents consecutive operations:

if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
For example, given integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the values of the counters after each consecutive operation will be:

    (0, 0, 1, 0, 0)
    (0, 0, 1, 1, 0)
    (0, 0, 1, 2, 0)
    (2, 2, 2, 2, 2)
    (3, 2, 2, 2, 2)
    (3, 2, 2, 3, 2)
    (3, 2, 2, 4, 2)
The goal is to calculate the value of every counter after all operations.

Write a function:

def solution(N, A)

that, given an integer N and a non-empty array A consisting of M integers, returns a sequence of integers representing the values of the counters.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 4
    A[2] = 4
    A[3] = 6
    A[4] = 1
    A[5] = 4
    A[6] = 4
the function should return [3, 2, 2, 4, 2], as explained above.

Write an efficient algorithm for the following assumptions:

N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].
 """
def solution(N, A): # TOTAL SCORE 100% ( 100% performance)
    
    res = [0]*N
    cur_max = 0
    prev_max = 0
    for i, e in enumerate(A):

        if e == N + 1:
            prev_max = cur_max
        else:

            if(res[e-1] < prev_max):
                res[e-1] = prev_max + 1
            else:
                res[e-1] += 1
            cur_max = max(cur_max, res[e-1])
    
    for i, e in enumerate(res):
        res[i] = max(res[i], prev_max)

    return res


def solution1(N, A): # TOTAL SCORE 88% ( 80% performance)
    
    res = [0]*N
    maxi = 0
    for i, e in enumerate(A):

        if e == N + 1:
            res = [maxi]*N
        else:
            res[e-1] += 1
            maxi = max(maxi, res[e-1])
    
    return res

def solution2(N, A): # TOTAL SCORE 66% ( 40% performance)
   
    keys = [i for i in range(N)]
    
    res = dict.fromkeys(keys, 0)
    maxi = 0
    for i, e in enumerate(A):

        if e == N + 1:
            res = dict.fromkeys(keys, maxi)
        else:
            res[e-1] += 1 
            maxi = max(maxi, res[e-1])
    
    print (res.values())
    return list(res.values())





assert(solution(5,[3,6,4,6,1,4,4]) == [3,2,2,4,2])

assert(solution(5,[3,4,4,6,1,4,4]) == [3,2,2,4,2])



N = 100000
A = [1]*20000 + [10001]*20000 + [2]*80000

#print(solution2(N, A))