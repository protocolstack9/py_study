def solution(A):
    """
    Find the minimal average of any slice containing at least two elements
    A: array consisting of N integers
    """
    min_idx = 0
    min_avg = (A[0] + A[1])/2.0

    for i in range(0, len(A)-1):
        min_two = (A[i] + A[i+1]) / 2.0
        if min_two < min_avg:
            min_idx = i
            min_avg = min_two

        if i < len(A)-2:
            min_three = (A[i]+A[i+1]+A[i+2])/3.0
            if min_three < min_avg:
                min_idx = i
                min_avg = min_three

    return min_idx

A = [4, 2, 2, 5, 1, 5, 8]

print(solution(A))
