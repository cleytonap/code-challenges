
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 23-jun-2022
# Description: Code challenge from Lesson 7.2 (Fish) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#LESSON LEARNED: Only by replacing list insert() with append() method the 100% performance score
# was finally reached. 
# append() --> linear performance
# insert() --> Quadritic performance

# PERSONAL NOTE: It was difficult to come up with a decent solution, specially to get 100% in performance score. It took me a full day.


""" You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
 """


def solution(A, B):

    goingRight = []
    countLeft = 0
    for size, direction in zip(A, B):

        if direction == 1: # 1 ---> going right (downstream)
            goingRight.append(size)
        else: # 0 <--- going left (upstream)
            while goingRight and size > goingRight[-1]:
                goingRight.pop() #eat smaller fish going to the opposite direction
            if not goingRight: #all fishes going right were eaten or there was no fish going right
                countLeft += 1

    return countLeft + len(goingRight)


def solution1(A, B): # TOTAL SCORE: 100%

    group_going_ds = []
    count_fish = 0

    if len(A) == 1:
        return 1

    if(len(set(B)) == 1): # All fishes going in the same direction
        return len(A)

    # <----------Upstream (0)           downstream (1)--------->
    for i, (fish_size, fish_dir) in enumerate(zip(A, B)):

        if fish_dir == 0:  # <---------- fish going upstream
            for i, f in enumerate (group_going_ds[::-1]):
                if f > fish_size:
                    group_going_ds = group_going_ds[:len(group_going_ds)-i]    
                    break
            else: # only executes if break was not reached
                #Either there was no fish going downstream or they were all eaten by the big fish going upstream
                count_fish += 1 #fish going upstream will never meet another fish in the opposite direction
                group_going_ds = []

        else: # 1 - fish going downstream -------->
            group_going_ds.append(fish_size)

    return count_fish + len(group_going_ds)




A = [1,2,3,4,5,6]

for i, a in enumerate(A[::-1]):
    print (i,a)


assert(solution([4,3,2,1,5], [1,1,1,1,0]) == 1)


assert(solution([4,3,2,1,5], [0,0,0,0,0]) == 5)

assert(solution([4,3,2,1,5], [1,1,1,1,1]) == 5)

assert(solution([4,3,2,1,5], [0,0,1,0,0]) == 3)


assert(solution([4,3,2,1,5], [0,1,1,0,0]) == 2)

assert(solution([4,3,2,1,5], [0,1,0,0,0]) == 2)