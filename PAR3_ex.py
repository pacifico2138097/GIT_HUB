'''
Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
'''
# Partitioning a list:
def partit_with_repeats(A):
    n = len(A)
    if n == 0:
        return []
    
    pivot = A[0]
    less_than = []
    equal_to = []
    greater_than = []

    for i in range(n):
        if A[i] < pivot:
            less_than.append(A[i])
        elif A[i] > pivot:
            greater_than.append(A[i])
        else:
            equal_to.append(A[i])
    
    B = less_than + equal_to + greater_than
    return B

n = 9

A = '4 5 6 4 1 2 5 7 4'
A = list(map(int, A.split()))
B = partit_with_repeats(A)
print(*B)