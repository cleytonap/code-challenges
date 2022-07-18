#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 23-jun-2022
# Description: Code challenge from Lesson 7.1 (Brackets) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------

#PERSONAL NOTE: This was easy. Solved in few minutes.

""" A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

def solution(S)

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")". """

def solution(S):
    
    if not S:
        return 1
    
    close_open_map = {'}': '{', ']': '[', ')':'(' }
    stack = []

    for c in S:
        if c in close_open_map:
            if(len(stack) == 0 or stack.pop() != close_open_map[c]):
                return 0
        else:
            stack.append(c)

    if(len(stack) == 0):
        return 1
        
    return 0


print(solution('{[()()]}'))
print(solution('([)()]'))