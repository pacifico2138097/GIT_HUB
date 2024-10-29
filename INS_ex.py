
''' 

Insertion sort is a simple algorithm with quadratic running time that builds the final sorted array one item at a time.
Given: A positive integer n≤10^3 and an array A[1..n] of integers.

Return: The number of swaps performed by insertion sort algorithm on A[1..n].

'''

# Returning the number of swaps performed by insertion_sort: 
def insertion_sort(a):
    swap_count = 0
    n = len(a)

    for i in range(1, n):
        key = a[i]          # current element to be placed
        j = i - 1           # element to the left

        while j >= 0 and key < a[j]:
            a[j+1] = a[j]
            j -= 1
            swap_count += 1

        a[j+1] = key

    return swap_count
    

n = 6
a = '6 10 4 5 1 2'
a = list(map(int, a.split()))

swap_count = insertion_sort(a)
print(swap_count)


