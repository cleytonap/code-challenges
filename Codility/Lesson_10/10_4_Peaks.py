



def checkPeaks(A, peaks, k): #constraints: len(peaks) >= 2. Peaks is sorted in ascending order.

    
    if len(A) % k != 0:
        return False

    if k > len(peaks):
        return False

    i = 0
    block_size = len(A) // k
    while i < len(A):
        
        for j in range(i, block_size + i):
            if j in peaks:
                break
        else: #did not hit break!
            return False #did not find a peak in current block!
        
        i = i + block_size

    return True

        

def solution(A):
    #Find peaks
    N = len(A)
    peaks = set()
    for i in range(1, N -1):
        if (A[i-1] < A[i] > A[i+1]):
            peaks.add(i)

    nPeaks = len(peaks)

    if nPeaks == 0 or nPeaks == 1: return nPeaks

    for k in range(nPeaks, 0, -1):
        if checkPeaks(A, peaks, k):
            return k
    

    return -1 #error
    

assert(solution([1,5,3,4,3,4,1,2,3,4,6,2]) == 3)