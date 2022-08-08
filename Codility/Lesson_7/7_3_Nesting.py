
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 24-jun-2022
# Description: Code challenge from Lesson 7.3 (Nesting) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#PERSONAL NOTE: very easy one. 5 minutes to get 100% score in the first attempt.

# LESSON LEARNED: assert() is absolutely necessary (always!!!). Even when we think 
# the solution is perfectly straightforward.

""" A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S consists only of the characters "(" and/or ")". """


def solution(S):
    # write your code in Python 3.6
    
    if not S: return 1
    count = 0

    for c in S:
        if c == '(':
            count += 1
        else:
            if count == 0:
                return 0
            
            count -= 1
    
    return 1 if count == 0 else 0
    

def solution1(S):

    if not S: return 1 #empty string

    stack = []

    for c in S:

        if c == '(':
            stack.append(c)
        else: #c == ')'
            if not stack:
                return 0
            stack.pop()
    
    if not stack: #stack is empty
        return 1
    
    return 0


assert(solution("(()(())())") == 1)
assert(solution("(") == 0)
assert(solution(")") == 0)