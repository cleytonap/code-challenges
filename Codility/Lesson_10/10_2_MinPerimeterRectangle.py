#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 28-jun-2022
# Description: Code challenge from Lesson 10.2 (MinPerimeterRectangle) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#LESSON LEARNED: use sqrt to find if a number is prime.
        # If a number n is not a prime, it can be factored into two factors a and b:

        # n = a * b

        # Now a and b can't be both greater than the square root of n, since then the product a * b would be greater than sqrt(n) * sqrt(n) = n. 
        # So in any factorization of n, at least one of the factors must be smaller than the square root of n, and if we can't find any factors 
        # less than or equal to the square root, n must be a prime.



""" An integer N is given, representing the area of some rectangle.

The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

For example, given integer N = 30, rectangles of area 30 are:

(1, 30), with a perimeter of 62,
(2, 15), with a perimeter of 34,
(3, 10), with a perimeter of 26,
(5, 6), with a perimeter of 22.
Write a function:

def solution(N)

that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

For example, given an integer N = 30, the function should return 22, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..1,000,000,000]. """

import math
def solution(N):
 
    a = math.floor(N**0.5)

    while N % a != 0:
        a -= 1
    
    b = N // a

    return 2*(a + b)


assert(solution(1) == 4)
assert(solution(80) == 36)
assert(solution(1000) == 130)
assert(solution(2) == 6)
assert(solution(982451653) == 1964903308)

