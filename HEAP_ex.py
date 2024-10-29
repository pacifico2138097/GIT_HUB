
'''
A binary heap is a binary tree based data structure that is often used to implement priority queues. Binary heaps, in turn, can be easily implemented using an array if the underlying tree is a complete binary tree. The tree nodes have a natural ordering: row by row, starting at the root and moving left to right within each row. If there are n
nodes, this ordering specifies their positions 1,2,…,n within the array. Moving up and down the tree is easily simulated on the array, using the fact that node number jhas parent ⌈j/2⌉and children 2jand 2j+1.

The goal of this problem is to build a heap from the given array. For this, go from the end to the beginning of a given array and let each element "bubble up".

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n≤105 and array A[1..n] of integers from −105 to 105.

Return: A permuted array A satisfying the binary max heap property: for any 2≤i≤n, A[⌊i/2⌋]≥A[i].
'''
# Ensuring that subtree satisfies the Max Heap property:
def heapify(A, n, i):
    largest = i                    # index of root i
    left = 2 * i                   # indeces of left and right children
    right = 2 * i + 1

    if left <= n and A[left - 1] > A[largest -1]:
        largest = left
    
    if right <= n and A[right - 1] > A[largest - 1]:
        largest = right
    
    if largest != i:                                           # if largest index has changed, swap with current node
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1]
        heapify(A, n, largest)

# Transforming array into a max heap using heapify function on all relevant nodes:
def build_max_heap(A):
    n = len(A)

    for i in range(n //2, 0, -1):
        heapify(A, n, i)

n = 5

input_string = '1 3 5 7 2'
A = [int(num) for num in input_string.split()]
build_max_heap(A)
print(*A)