from typing import List
import random


# Merge Sort (returns a new sorted list)
def merge_sort(arr: List[int]) -> List[int]:
    n = len(arr)
    if n <= 1:
        return arr[:]  # return a copy

    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Merge step
    i = j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append remaining elements
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])

    return merged


# In-place Quick Sort (Lomuto partition)
def quick_sort(arr: List[int]) -> None:
    def _partition(a, lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def _quick(a, lo, hi):
        if lo < hi:
            p = _partition(a, lo, hi)
            _quick(a, lo, p - 1)
            _quick(a, p + 1, hi)

    _quick(arr, 0, len(arr) - 1)


# Randomized Quick Sort (to avoid worst-case)
def randomized_quick_sort(arr: List[int]) -> None:
    def _partition(a, lo, hi):
        pivot = a[hi]
        i = lo
        for j in range(lo, hi):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[hi] = a[hi], a[i]
        return i

    def _quick(a, lo, hi):
        if lo < hi:
            # Choose random pivot and swap to end
            r = random.randint(lo, hi)
            a[r], a[hi] = a[hi], a[r]
            p = _partition(a, lo, hi)
            _quick(a, lo, p - 1)
            _quick(a, p + 1, hi)

    _quick(arr, 0, len(arr) - 1)
