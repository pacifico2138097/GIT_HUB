
''' 
Comparing the algorithms for sorting and “Median” finding we notice that, beyond the common divide-and-conquer philosophy and structure, they are exact opposites. “Merge Sort” splits the array in two in the most convenient way (first half, second half), without any regard to the magnitudes of the elements in each half; but then it works hard to put the sorted subarrays together. In contrast, the median algorithm is careful about its splitting (smaller numbers first, then the larger ones), but its work ends with the recursive call.

Quick sort is a sorting algorithm that splits the array in exactly the same way as the median algorithm; and once the subarrays are sorted, by two recursive calls, there is nothing more to do. Its worst-case performance is Θ(n2), like that of median-finding. But it can be proved that its average case is O(nlogn); furthermore, empirically it outperforms other sorting algorithms. This has made quicksort a favorite in many applications— for instance, it is the basis of the code by which really enormous files are sorted.

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n≤10^5 and an array A[1..n] of integers from −10^5 to 10^5.

Return: A sorted array A[1..n].

'''
# Ensuring max heap property for subtree:
def heapify(A, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and A[left] > A[largest]:
        largest = left
    
    if right < n and A[right] > A[largest]:
        largest = right
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, n, largest)

# Sorting array in ascending order:
def heap_sort(A):
    n = len(A)

    for i in range(n //2 -1, -1, -1):
        heapify(A, n, i)
    
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

n = 7

input_string = '5 -2 4 7 8 -10 11'
A = [int(num) for num in input_string.split()]
heap_sort(A)

print(" ".join(map(str, A)))