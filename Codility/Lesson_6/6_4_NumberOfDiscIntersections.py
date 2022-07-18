#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 27-jun-2022
# Description: Code challenge from Lesson 6.4 (NumbersOfDistinctIntersections) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------


#PERSONAL NOTE: Very difficult. It took me few days to get 100% score in performance.
# My first insight was to sort the list by the left most intersections (start of disc), 
# but I could not get the right solution. It was only when I learned about the bisect module that
# I managed to come up with a solution with O(N*log(N)) or O(N) time complexity.

#LESSON LEARNED: bisect module is very useful. Namely for methods "insort" (inserts
# an element in a sorted list, keeping it sorted) and "bisect" (returns the index/position of a sorted 
# list where element x should be inserted in order to keep the list sorted). Bisect methods
# use binary search algorithm.

""" 
        Time complexity:
        
        Sorted Lists
        O( n log n) to initially create the list (if it's unsorted data. O(n), if it's sorted )
        O( log n) lookups (this is the binary search part)
        O( n ) insert / delete (might be O(1) or O(log n) average case, depending on your pattern)

        Whereas with a set(), you're incurring

        O(n) to create
        O(1) lookup
        O(1) insert / delete
"""


from bisect import insort, bisect_right

def solution(A): #TOTAL SCORE: 100% (100% correct, 100% performance)
    count = 0
    discs = []
    lefts_sorted = []
    for i, disc in enumerate (A):
        discs.append(( i - A[i], A[i] + i)) #creat a list with the left (start) and right (end) points of each disc
        insort(lefts_sorted, i - A[i]) #create a sorted list by the left most points (ascending order)

    for i, (left, right) in enumerate (discs):

        # finds the amount of discs whose left (start) points are to the left of the current disc right end
        offset = bisect_right(lefts_sorted, right)

        count += offset - (i + 1) #decrease i to not count intersections discs twice. Decrease 1 to not count itself.

        if(count > 10000000):
            return -1

    return count


def solution1(A): #TOTAL SCORE: 62% (100% correct, 25% performance)

    len_A = len(A)
    count = 0
    for i, r1 in enumerate (A):
        count += min(r1, len_A - i -1)

        for j in range (i+r1+1, len_A):
            r2 = A[j]
            if (j - r2 <= i + r1):
                count += 1
        if count > 10000000:
            return -1
    return count


def solution2(A): #TOTAL SCORE: 62% (100% correct, 25% performance)

    len_A = len(A)
    min_dict = dict()
    count = 0

    for i in range (1, len_A):
        m = max (0,  i - A[i])
        for j in range(m, i):
            if(j in min_dict):
                min_dict[j] = min_dict[j] + 1
            else:
                min_dict[j] = 1
    
    for i, r1 in enumerate (A):
        count += min(r1, len_A - i -1)

        if i + r1 in min_dict:
            count += min_dict[i + r1]
        
        if count > 10000000:
            return -1
    return count
            


def solution3(A): #TOTAL SCORE: 56% (100% correct, 12% performance)

    #len_A = len(A)
    count = 0
    sorted_discs = []
    for i, disc in enumerate (A):
        sorted_discs.append(( i - A[i], A[i] + i))
    
    sorted_discs = sorted(sorted_discs, key=lambda borders: borders[1] - borders[0], reverse=True)

    print(sorted_discs)
    
    i = 0 
    for i, disc in enumerate (sorted_discs):
        
        j = i + 1
        
        for j in range(i+1, len(sorted_discs)):
            disc2 = sorted_discs[j]
            if( (disc2[0] >= disc[0] and disc2[0] <= disc[1]) or (disc2[1] >= disc[0] and disc2[1] <= disc[1])): 
                count += 1

        if count > 10000000:
            return -1

    return count





print(solution([1,5,2,1,4,0]))
print(solution([0]*100000))


# assert(solution([1,5,2,1,4,0]) == 11)
# assert(solution([0]*100000) == 0)
