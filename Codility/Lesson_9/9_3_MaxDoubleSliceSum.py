#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 29-jun-2022
# Description: Code challenge from Lesson 9.3 (MaxDoubleSliceSum) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

# PERSONAL NOTE: Although I had spent few days trying, I could not find an answer
# to this challenge all by myself.
# I had to get the 'insight' to solve the problem from others. 
# Only then I was able to write my own code.


def solution(A):

    N = len(A)
    maxSlice1 = [0]*len(A) #max slice from start to end (left to right) up to position i
    maxSlice2 = [0]*len(A) #max slice from end to start (right to left) up to position i

    for i in range (1, N - 1): # (N - 1) because Z < N
        maxSlice1[i] = max(maxSlice1[i-1] + A[i], 0)
        maxSlice2[(N-1)-i] = max(maxSlice2[(N-1)-i+1] + A[(N-1)-i], 0)

    maxDoubleSlice = 0
    for i in range (1, N - 1): # (N - 1) because Z        
        maxDoubleSlice = max(maxDoubleSlice, maxSlice1[i-1] + maxSlice2[i+1])
            
    return maxDoubleSlice

    

def solution1(A): # Wrong !

    if(len(A) == 3): return 0

    max_slice = 0
    s1 = 0
    s2 = 0
    
    i = 1

    while (i <  len(A) -1):

        a = A[i]
        s2 = 0
       
        if(a > 0):        
            s1 += a
        else:
            j = i + 1
         
            while (j < len(A) -1 and A[j] > 0):
                s2 += A[j]
                j += 1

            max_slice = max(max_slice, s1 + s2)

            s1 = max (s2, s1 + s2 + a)

            i = j 

            continue
            
        max_slice = max(max_slice, s1 + s2)
        i += 1

    return max_slice






assert(solution([1,4, 5, -10, 11, -20, 2, 3, -1, 30,1]) == 45) #45


assert(solution([3, 2, -6, 4, 0]) == 6)

assert(solution([3, 2, 6, 4]) == 6)


assert(solution([3, 2, 6, 4, 0]) == 10)

assert(solution([3, 2, 6, -1, 4, 5, -2, 2,6]) == 18) #18
assert(solution([3, 2, 6, -1, 4, 5, -1, 2]) == 17) #17
assert(solution([0,2,-4,5,-6,0]) ==7) #7
assert(solution([0,-2,-4,-5,-6,0])==0) #0
assert(solution([3, 2, -6, 4, 0])==6) #6
assert(solution([1,2, 3, -100, -100, 4, 5, -1, 3,1])==12) #12
assert(solution([1,4, 5, -10, 9, -10, 2, 3, -1, 3,1])==18) #18

