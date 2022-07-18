
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 22-jun-2022
# Description: Code challenge from Lesson 5.4 (MinAvgTwoSlices) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------


""" A non-empty array A consisting of N integers is given. A pair of integers (P, Q), 
such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains 
at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] 
divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

For example, array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
contains the following example slices:

slice (1, 2), whose average is (2 + 2) / 2 = 2;
slice (3, 4), whose average is (5 + 1) / 2 = 3;
slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
The goal is to find the starting position of a slice whose average is minimal.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the starting position of the slice 
with the minimal average. If there is more than one slice with a minimal average, you should return 
the smallest starting position of such a slice.

For example, given array A such that:

    A[0] = 4
    A[1] = 2
    A[2] = 2
    A[3] = 5
    A[4] = 1
    A[5] = 5
    A[6] = 8
the function should return 1, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [2..100,000];
each element of array A is an integer within the range [−10,000..10,000]. """

def solution(A):

    min_index = 0    
    min_avg = 10000000000
    max_sum = A[0]
    p = 0

    for q in range (1,len(A)):
            
        prev_avg = (max_sum + A[q]) / (q - p + 1)
        curr_avg = (A[q] + A[q-1]) / 2 

        if( curr_avg <= prev_avg):
            max_sum = A[q] + A[q-1]
            p = q -1
        else:
            max_sum += A[q]

        temp_min_avg = min(prev_avg,curr_avg)
        if (temp_min_avg < min_avg):
            min_avg = temp_min_avg
            min_index = p
    
    return min_index

def solution2(A): #TOTAL SCORE: 100%

    min_index = 0    
    min_avg = 10000000000
    slice_len = 1
    prev_e = A[0]
    max_sum = A[0]
    p = 0

    for i in range (1,len(A)):
        
        e = A[i]
        
        prev_avg = (max_sum + e) / (slice_len + 1)
        curr_avg = (e + prev_e) / 2 
        if( curr_avg <= prev_avg):
            max_sum = e + prev_e
            slice_len = 2    
            p = i -1
            if(curr_avg < min_avg):
                min_avg = curr_avg
                min_index = i - 1   #p     
        else:
            max_sum += e
            slice_len += 1
            if (prev_avg < min_avg):
                min_avg = prev_avg
                min_index = p

        #min_avg = min(min_avg, min(prev_avg, curr_avg))
    
        prev_e = e

    return min_index


print(solution([4,2,1,3,0,12,8,1,3,0])) #2

print(solution([4,2,1,0,0,12,8,1,0,0])) #3

print(solution([-4,2,2,-5,1,-8,10])) #3

print(solution([-5,1,-10,1])) #0

print(solution([4,2,2,5,1,5,8])) #1

print(solution([-4,2,2,5,1,5,-8])) #5

print(solution([-5,1])) #0
print(solution([1,2,-5])) #1
print(solution([10,2,1,-5])) #2




