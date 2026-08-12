def merge_sort(A, lb, ub):
    if lb < ub:
        mid = (lb + ub) // 2

        merge_sort(A, lb, mid)
        merge_sort(A, mid + 1, ub)

        merge(A, lb, mid, ub)


def merge(A, lb, mid, ub):
    i = lb
    j = mid + 1
    k = lb

    B = [0] * len(A)

   
    while i <= mid and j <= ub:
        if A[i] <= A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1

        k += 1

    
    while i <= mid:
        B[k] = A[i]
        i += 1
        k += 1

   
    while j <= ub:
        B[k] = A[j]
        j += 1
        k += 1

   
    for k in range(lb, ub + 1):
        A[k] = B[k]



n = int(input("Enter number of elements: "))

A = []

print("Enter the elements:")
for i in range(n):
    A.append(int(input()))

merge_sort(A, 0, n - 1)

print("Sorted array:")
print(*A)
