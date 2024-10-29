
''' 
The merging procedure is an essential part of “Merge Sort” (which is considered in one of the next problems).

Given: A positive integer n≤10^5 and a sorted array A[1..n] of integers from −10^5 to 10^5, a positive integer m≤10^5 and a sorted array B[1..m] of integers from −10^5 to 10^5.

Return: A sorted array C[1..n+m] containing all the elements of A and B.

'''
# Merging all the elements of A and B into a sorted array C:
def merge_sort(A,B):
    
    i = 0
    j = 0

    n = len(A)
    m = len(B)

    C = []

    while i < n and j < m:
        if A[i] < B[j]:
            C.append(A[i])
            i += 1 
        else:
            C.append(B[j])
            j += 1
    
    while i < n:
        C.append(A[i])
        i += 1

    while j < m:
        C.append(B[j])
        j += 1
    
    
    return C

n = 4
m = 3

A = '2 4 10 18'
B = '-5 11 12'

numbers_listA = A.split()
numbers_listB = B.split()

A = [int(num) for num in numbers_listA]
B = [int(num) for num in numbers_listB]
C = merge_sort(A,B)
print(*C)

