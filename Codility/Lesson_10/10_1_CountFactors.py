
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 27-jun-2022
# Description: Code challenge from Lesson 10.1 (CountFactors) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#PERSONAL NOTE: Took me about 2 hours. I had to review the theory of prime factorization and search the internet
# for methods to quickly find whether a number is prime or not.
# At the end, I simply implemented the prime factorization algorithm below.
# I have a feelling that there are more efficient ways to solve this problem. But, as I got 100% score and have other
# lessons to complete, I didn't bother to try to improve the code.

        # Finding the Number of Factors
        # We can find the number of factors of a given number using the following steps.

        # Step 1: Find its prime factorization, i.e. express it as the product of primes.
        # Step 3: Write the prime factorization in the exponent form.
        # Step 3: Add 1 to each of the exponents.
        # Step 4: Multiply all the resultant numbers. This product would give the number of factors of the given number.


""" A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647]. """


# fast way to check if a number is prime. Code copied from internet
# Find the square root of x.  Round this down to the nearest whole number. We call this truncating a number.
# Check all of the prime numbers less than or equal to the truncated square root of x.
# If none of these prime numbers divide evenly into the x, then x is prime
def is_prime(n):
    if n == 1:
        return False
    i = 2
    while i*i <= n: #this way (i*i) there is no need to use math.sqrt() method
        if n % i == 0:
            return False
        i += 1
    return True

def solution(N): # 100% correctness and 100% performance

    if N == 1: return 1
    if N == 2: return 2

    if is_prime(N): return 2

    prime_counts = {}
    
    # Perform prime factorization
    while (N > 1):
        prime = 2
        while (N % prime != 0):
            prime += 1
            if prime > N // 2:
                prime = N

        N = N / prime

        if prime in prime_counts:
            prime_counts[prime] += 1
        else:
            prime_counts[prime] = 1   
    
    num_factors = 1
    for prime in prime_counts:
        num_factors *= (prime_counts[prime] + 1)

    return num_factors


def solution1(N): #Brute force --> 100% correctness and 16% performance

    if N == 1: return 1

    if N == 2: return 2

    factors = 2

    for i in range(2, N // 2 + 1):
        if (N % i == 0):
            factors +=1
            print (i)
    
    return factors

def solution2(N): # 100% correctness and 66% performance

    if N == 1: return 1
    if N == 2: return 2

    prime_counts = {}
    
    while (N > 1):
        prime = 2
        while (N % prime != 0):
            prime += 1

        N = N / prime
        if prime in prime_counts:
            prime_counts[prime] += 1
        else:
            prime_counts[prime] = 1
    
    num_factors = 1
    for prime in prime_counts:
        num_factors *= (prime_counts[prime] + 1)

    return num_factors




assert(solution(9) == 3)
assert(solution(780291637) == 2)
assert(solution(3784) == 16)
assert(solution(3) == 2)
assert(solution(6) == 4)
assert(solution(12) == 6)
assert(solution(24) == 8)
assert(solution(48) == 10)
assert(solution(96) == 12)
assert(solution(192) == 14)
assert(solution(384) == 16)
assert(solution(5) == 2)
assert(solution(10) == 4)
assert(solution(20) == 6)
assert(solution(40) == 8)
assert(solution(80) == 10)


assert(solution(24) == 8)
assert(solution(3) == 2)
assert(solution(9) == 3)
assert(solution(11) == 2)



