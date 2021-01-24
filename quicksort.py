def partition(arr, low, high):
    i = (low - 1)
    #pivot = arr[high]  # pivot
    for j in range(low, high):
        if arr[j] < arr[high]:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

n = int(input("how many number you want to enter:"))
l = []
for i in range(n):
    l.append(int(input()))
quickSort(l, 0, n - 1)
print("Sorted array is:")
for i in range(n):
    print(l[i],end=" ")
