
#------------------------------------------------------------------------------
# Author: Cleyton Pires (https://github.com/cleytonap)
# Date: 21-jun-2022
# Description: Code challenge from Lesson 5.3 (GenomicRangeQuery) of Codility
# https://app.codility.com/programmers/
# TOTAL SCORE: 100%
#------------------------------------------------------------------------------


#LESSON LEARNED: Initially I avoid using string methods (ex. find) to solve the problem,
# for I thought it was suspiciously too simple and, therefore, wouldnt be performatic. After many
# frustrated attempts, the simplest solution using str.find() was the only one to get
# total score 100%.

""" 
A DNA sequence can be represented as a string consisting of the letters A, C, G and T, which correspond to the 
types of successive nucleotides in the sequence. Each nucleotide has an impact factor, which is an integer. 
Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively. You are going to answer 
several queries of the form: What is the minimal impact factor of nucleotides contained in a particular part of 
the given DNA sequence?

The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters. There are M 
queries, which are given in non-empty arrays P and Q, each consisting of M integers. The K-th query (0 ≤ K < M) 
requires you to find the minimal impact factor of nucleotides contained in the DNA sequence between positions 
P[K] and Q[K] (inclusive).

For example, consider string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
The answers to these M = 3 queries are as follows:

The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice), whose impact factors are 
3 and 2 respectively, so the answer is 2.
The part between positions 5 and 5 contains a single nucleotide T, whose impact factor is 4, so the answer is 4.
The part between positions 0 and 6 (the whole string) contains all nucleotides, in particular nucleotide A 
whose impact factor is 1, so the answer is 1.

Write a function:

def solution(S, P, Q)

that, given a non-empty string S consisting of N characters and two non-empty arrays P and Q consisting of M 
integers, returns an array consisting of M integers specifying the consecutive answers to all queries.

Result array should be returned as an array of integers.

For example, given the string S = CAGCCTA and arrays P, Q such that:

    P[0] = 2    Q[0] = 4
    P[1] = 5    Q[1] = 5
    P[2] = 0    Q[2] = 6
the function should return the values [2, 4, 1], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P and Q is an integer within the range [0..N - 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.
 """

def solution(S, P, Q): # Total score: 100% (100% performance)
    
    res = []

    for p, q in zip(P,Q):
        s = S[p : q + 1]
        if(s.find('A') != -1):
            res.append(1)
        elif (s.find('C') != -1):
            res.append(2)
        elif (s.find('G') != -1):
            res.append(3)
        else:
            res.append(4)
    
    return res



def minImpactFactor2(seq):

    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    min_impact = 5

    for nucleotide in seq:
        min_impact = min(min_impact, impact[nucleotide])

    return min_impact



def minImpactFactor(seq):
    if 'A' in seq:
        return 1
    if 'C' in seq:
        return 2
    if 'G' in seq:
        return 3
    return 4 # 'T'
    

def solution1(S, P, Q): # Total score: 62% (0% performance)
    
    res = []
    min_p = min(P)
    S = S[min_p:max(Q)+1]
    for p, q in zip(P,Q):
        seq = set(S[p - min_p : q - min_p +1]) #remove duplicates
        res.append(minImpactFactor(seq))
    
    return res

def solution2(S, P, Q): # Total score: 75% (33% performance)
    
    count = {'A': set(), 'C': set(), 'G': set(), 'T': set()}

    min_p = min(P)
    max_q = max(Q)

    S = S[min_p:max_q+1]

    res = []

    for i, e in enumerate (S):
        count[e].add(i + min_p)

    for p, q in zip(P,Q):
        found_min = False
        set_ = count['A']
        for e in set_:
            if e + min_p >= p and e + min_p <= q:
                res.append(1)
                found_min = True
                break
        if(found_min == False):
            set_ = count['C']
            for e in set_:
                if e + min_p >= p and e + min_p <= q:
                    res.append(2)
                    found_min = True
                    break
        if(found_min == False):
            set_ = count['G']
            for e in set_:
                if e + min_p >= p and e + min_p <= q:
                    res.append(3)
                    found_min = True
                    break
        if(found_min == False):
            res.append(4)
    
    return res

def solution3(S, P, Q):  # Total score: 87% (66% performance)

    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    comp = []
    i = 0
    while (i < len(S)):
        count = 1
        nucleotide = S[i]
        i += 1
        while (i < len(S) and S[i] == nucleotide):
            count += 1
            i += 1
        
        comp.append((impact[nucleotide], count))
    print(comp)    

    #comp = [(1,2),(2,1),(3,10),(4,5),(1,2),(2,10)]

    min_factor = []
    for p, q in zip (P, Q):

        i = 0
        _min = 4
        counter = 0
        nuc, _ = comp[0]

        while (i < len(comp) and counter <= p): # finds the beginning of the sequence
            nuc, count = comp[i]
            counter += count
            i += 1

        
        _min = nuc

        while (counter <= q): # finds the end of the sequence
            nuc, count = comp[i]
            counter += count
            _min = min(_min,nuc)
            i += 1

        min_factor.append(_min)

    return min_factor


def solution4(S, P, Q):  # Total score: 87% (66% performance)

    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    min_p = min(P)
    S = S[min_p: max(Q) + 1]

    comp = []
    i = 0
    while (i < len(S)):
        count = 1
        nucleotide = S[i]
        i += 1
        while (i < len(S) and S[i] == nucleotide):
            count += 1
            i += 1
        
        comp.append((impact[nucleotide], count))

    #comp = [(1,2),(2,1),(3,10),(4,5),(1,2),(2,10)]

    min_factor = []
    for p, q in zip (P, Q):

        i = 0
        _min = 4
        counter = 0
        nuc, _ = comp[0]

        while (counter <= p - min_p): # finds the beginning of the sequence
            nuc, count = comp[i]
            counter += count
            i += 1

        
        _min = nuc

        while (counter <= q - min_p): # finds the end of the sequence
            nuc, count = comp[i]
            counter += count
            _min = min(_min,nuc)
            if(_min == 1):
                break
            i += 1

        min_factor.append(_min)

    return min_factor


def get_next(s, index):
    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    i = index + 1
    while i < len(s) and s[i].isdigit():
        i += 1
    
    return impact[s[index]], int(s[index + 1:i]), i
    



def solution5(S, P, Q):  # Total score: 87% (66% performance)

    impact = {'A': 1, 'C': 2, 'G': 3, 'T': 4}

    min_p = min(P)
    S = S[min_p: max(Q) + 1]

    zip_S = ''
    i = 0
    while (i < len(S)):
        count = 1
        nucleotide = S[i]
        i += 1
        while (i < len(S) and S[i] == nucleotide):
            count += 1
            i += 1
        
        zip_S += nucleotide + str(count) 
    print(zip_S)    

    i = 0
    comp = []
    while (i < len(zip_S)):
        nuc, count, i = get_next(zip_S, i) 
        comp.append((nuc, count))

    print (comp)
    #comp = [(1,2),(2,1),(3,10),(4,5),(1,2),(2,10)]

    min_factor = []
    for p, q in zip (P, Q):

        i = 0
        _min = 4
        counter = 0
        nuc, _ = comp[0]
        set_ = set()

        while (counter <= p - min_p): # finds the beginning of the sequence
            #nuc, count, i = get_next(comp, i)
            nuc, count = comp[i]
            i += 1
            counter += count

        
        set_.add(nuc)

        while (counter <= q - min_p): # finds the end of the sequence
            #nuc, count, i = get_next(comp, i)
            nuc, count = comp[i]
            set_.add(nuc)
            if(nuc == 1):
                break
            i += 1
            counter += count           
              

        min_factor.append(min(set_))

    return min_factor




S = 'GC'*100000

P = [0]*50000
Q = [40000]*50000

print(solution(S, P, Q))

#assert(solution('CAGCCTA', [2,5,0], [4,5,6]) == [2,4,1])

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))

print(solution('AACGGGGGGGGGGTTTTTAACCCCCCCCCC', [5,5,0], [15,5,6]))

print(solution('AAAAAAA', [2,5,0], [4,5,6]))