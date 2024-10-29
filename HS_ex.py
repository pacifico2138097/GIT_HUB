
''' 
The heap sort algorithm first transforms a given array into a max heap (recall the problem “Building a Heap”). It then repeats the following two simple steps n−1 times:

Swap the last element of the heap with its root and decrease the size of the heap by 1.
"Sift-down" the new root element to its proper place.

Given: A positive integer n≤105 and an array A[1..n] of integers from −10^5 to 10^5.

Return: A sorted array A.
'''
# Ensuring subtree satisfies the max heap property:
def heapify(A, n, i):
    largest = i                   # index of root i
    left = 2 * i                  # indeces of left and right children
    right = 2 * i + 1

    if left <= n and A[left - 1] > A[largest -1]:
        largest = left
    
    if right <= n and A[right - 1] > A[largest - 1]:
        largest = right
    
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        heapify(A, n, largest)

# Converting array into a max heap:
def build_max_heap(A):
    n = len(A)

    for i in range(n //2, 0, -1):     # starting from last-non leaf node to the root
        heapify(A, n, i)

# Sorting array:
def heap_sort(A):
    n = len(A)
    build_max_heap(A)

    for i in range(n, 1, -1):           
        A[i-1], A[0] = A[0], A[i-1]
        heapify(A, i-1, 1)

string = '2 6 7 1 3 5 4 8 9'

n = 9
A = [int(num) for num in string.split()]
heap_sort(A)
print(*A)