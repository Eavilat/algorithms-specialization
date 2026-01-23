# Merge Sort Algorithm Implementation

def merge_sort(arr):
  if len(arr) <= 1:
    return arr, 0

  mid = len(arr) // 2
  left, left_inv = merge_sort(arr[:mid])
  right, right_inv = merge_sort(arr[mid:])
  merged, split_inv = merge(left, right)

  return merged, left_inv + right_inv + split_inv

def merge(left, right):
  i = 0
  j = 0
  inv = 0
  arr = []

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      arr.append(left[i])
      i += 1
    else:
      arr.append(right[j])
      j += 1
      inv += len(left[i:])


  while i < len(left):
      arr.append(left[i])
      i += 1


  while j < len(right):
      arr.append(right[j])
      j += 1

  return arr, inv

example = [3,2,5,1,6,7,0,4]

sorted_arr, inversions = merge_sort(example)

print(sorted_arr)
print(inversions)