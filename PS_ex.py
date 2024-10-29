
''' 
Problem
Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5, a positive integer k≤1000.

Return: The k smallest elements of a sorted array A.

'''
# Ensuring max heap property for subtree:
def heapify(A, n, i):
    largest = i
    left = 2 * i
    right = 2 * i + 1

    if left <= n and A[left - 1] > A[largest -1]:
        largest = left
    
    if right <= n and A[right - 1] > A[largest - 1]:
        largest = right
    
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        heapify(A, n, largest)

# Building max heap from array:
def build_max_heap(A):
    n = len(A)

    for i in range(n //2, 0, -1):
        heapify(A, n, i)

# Sorting array in ascending order:
def heap_sort(A):
    n = len(A)
    build_max_heap(A)

    for i in range(n, 1, -1):
        A[i-1], A[0] = A[0], A[i-1]
        heapify(A, i-1, 1)


# k smallest elements in A:
def smallest_k(A, k):
    heap_sort(A)
    return A[:k]

n = 10
k = 3
string = '4 -6 7 8 -9 100 12 13 56 17'
A = [int(num) for num in string.split()]
result = smallest_k(A,k)
print(*result)

