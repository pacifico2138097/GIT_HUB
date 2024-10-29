
''' 
The task is to implement a linear time randomized algorithm for the selection problem.

Given: A positive integer n≤105 and an array A[1..n] of integers from −10^5 to 10^5, a positive number k≤n .

Return: The k-th smallest element of A
'''

# Returning the k-th smallest element of array A: 
def selection(A, k):
    def quickselection(A, low, high, k):
        if low < high:
           pivot_index = partition(A, low, high)
    
           if pivot_index == k:
             return A[k]
           elif pivot_index < k:
             return quickselection(A, pivot_index + 1,high,  k)
           else:
             return quickselection(A, low, pivot_index - 1, k)
        
        else: 
            return A[low]

# Partitioning array:
    def partition(A, low, high):
        pivot = A[high]
        i = low - 1

        for j in range(low, high):
            if A[j] <= pivot:
             i += 1
             A[i], A[j] = A[j], A[i]
    
        A[i+1], A[high] = A[high], A[i+1]
        return i + 1
    
    k -= 1
    return quickselection(A, 0, len(A)-1, k)
    
    
data_string = '2 36 5 21 8 13 11 20 5 4 1'
A = list(map(int, data_string.split()))
k = 8
n = len(A)
n = 11
result = selection(A, k)
print(result)


          