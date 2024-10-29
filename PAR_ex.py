
'''
A partition procedure is an essential part of the Quick Sort algorithm, the subject of one of the following problems. Its main goal is to put the first element of a given array to its proper place in a sorted array. It can be implemented in linear time, by a single scan of a given array. Moreover, it is not hard to come up with an in-place algorithm.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1]for all q+1≤i≤n.
'''
# Partitioning a list: 
def partition(n,A):
    pivot = A[0]
    less_than = []
    greater_than = []

    for i in range(1, n):                 
        if A[i] <= pivot and A[i]!=pivot: 
            less_than.append(A[i])        # if conditions are met, add element to less_than list
   
    for i in range(1,n): 
        if A[i] > pivot:                   
            greater_than.append(A[i])     # if conditions are met, add element to greater_than list
    
    return less_than + [pivot] + greater_than  # concatenation of the two lists

n = 9
A = ' 7 2 5 6 1 3 9 4 8'

A = list(map(int, A.split())) # converting string into list of integers
result = partition(n, A)
print(*result)
