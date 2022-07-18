
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 18-jul-2022
# Description: Code challenge from Lesson 10.3 (Flags) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#LESSON LEARNED: BINARY SEARCH!At first I could not figure out a non-quadratic (O(N2)) solution. 
# Only when I saw the comment below I could devise a good-enough solution O(N log N), using binary search!

        # If we know that x flags can be set, then we also know that
        # x−1, x−2, . . . , 1 flags can be set. Otherwise, if x flags cannot be set, then x+1, x+2, . . . , √
        # N
        # flags cannot be set either


""" A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly four peaks: elements 1, 3, 5 and 10.

You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.



Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

For example, given the mountain range represented by array A, above, with N = 12, if you take:

two flags, you can set them on peaks 1 and 5;
three flags, you can set them on peaks 1, 5 and 10;
four flags, you can set only three flags, on peaks 1, 5 and 10.
You can therefore set a maximum of three flags in this case.

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

For example, the following array A:

    A[0] = 1
    A[1] = 5
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..400,000];
each element of array A is an integer within the range [0..1,000,000,000]. """


def checkFlag(peaks, x): #constraints: len(peaks) >= 2. Peaks is sorted in ascending order.

    flags = x - 1 #Always put a flag in the first peak
    prevPeak = peaks[0]
    for i in range(1, len(peaks)):
        if x <= peaks[i] - prevPeak:
            flags -= 1
            prevPeak = peaks[i]
            if flags == 0:
                return True
    return False

def solution(A): 
    N = len(A)
    peaks = []

    #Find peaks
    for i in range(1, N -1):
        if (A[i-1] < A[i] > A[i+1]):
            peaks.append(i)

    #Edge cases
    numPeaks = len(peaks)
    if numPeaks == 0 or numPeaks == 1: return numPeaks

    flags = [i for i in range(2, numPeaks + 1)]

    #Binary search:
    while len(flags) > 1:
        x = len(flags) // 2
        if checkFlag(peaks, flags[x]):
            flags = flags[x:] #It is possible to improve performance by avoiding list slices!
        else:
            flags = flags[:x]

    return flags[0]
    


assert(solution([1,5,3,4,3,4,1,2,3,4,6,2]) == 3)
solution([1,5,3,4,3,4,1,2,3,4,6,2]*4)
assert(solution([1]) == 0)
assert(solution([1, 3]) == 0)
assert(solution([1, 3, 1]) == 1)
assert(solution([3, 3, 1]) == 0)
assert(solution([1,5,3,4,3,4,1,2,3,4,6,2]) == 3)

#assert(solution([1,5,3,4,3,4,1,2,3,4,6,2]*10000) == 345) # ????

# import timeit
# #assert(solution([1,5,3,4,3,4,1,2,3,4,6,2]*10000) == 345) # ????
# print(timeit.timeit(lambda: solution([1,5,3,4,3,4,1,2,3,4,6,2]*4), number=1))
# print(timeit.timeit(lambda: solution3([1,5,3,4,3,4,1,2,3,4,6,2]*4), number=1))