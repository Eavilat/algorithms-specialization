#Quicksort algorithm implementation in Python
import numpy as np

arr = np.loadtxt("data.txt")

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1

    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def choose_pivot_first():
    pass

def choose_pivot_last(arr, low, high):
    arr[low], arr[high] = arr[high], arr[low]

def choose_pivot_median(arr, low, high):
    length = high - low + 1
    mid = low + (length - 1) // 2

    first = arr[low]
    middle = arr[mid]
    last = arr[high]
    if (first <= middle <= last) or (last <= middle <= first):
        median_index = mid
    elif (middle <= first <= last) or (last <= first <= middle):
        median_index = low
    else:
        median_index = high

    arr[low], arr[median_index] = arr[median_index], arr[low]

def quicksort(arr, low, high, comparisons, choose_pivot):
    if low < high:
        m = high - low + 1
        comparisons[0] += m - 1

        choose_pivot(arr, low, high)
        p = partition(arr, low, high)

        quicksort(arr, low, p - 1, comparisons, choose_pivot)
        quicksort(arr, p + 1, high, comparisons, choose_pivot)
def count_comparisons(arr, choose_pivot):
    comparisons = [0]
    quicksort(arr, 0, len(arr) - 1, comparisons, choose_pivot)
    return comparisons[0]

result = count_comparisons(arr, choose_pivot_median)
print(result)

