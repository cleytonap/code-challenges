#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 17-jun-2022
# Description: Code challenge from Lesson 2.2 (OddOccurrencesInArray) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------
def solution(A):
    
    counts = {}

    for i, e in enumerate(A):

        if(e in counts):
            counts[e] = counts[e] + 1
        else:
            counts[e] = 1
    
    for e in counts:
        if (counts[e] % 2 != 0):
            return e
    
    return -1 # error!


def solution2(A):
    
    if(len(A) == 1): return A[0]

    aux = [] # Using list I get TIMEOUT ERROR in the performance tests. It works if set is used instead of list !!! 
             # Sets are way faster than lists when using the 'in' operator

    for a in A:
        
        if a in aux:
            aux.remove(a)
        else:
            aux.append(a)
    
    return aux[0]

