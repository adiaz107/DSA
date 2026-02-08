
def bubble_sort(arr: list) -> tuple[list, int]:
    comparisons = 0
    end = len(arr)
    while end > 1:
        last_swapped = 0
        for i in range(1, end):
            comparisons += 1
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                last_swapped = i

        end = last_swapped

    return arr, comparisons

def insertion_sort(arr: list) -> tuple[list, int]:
    comparisons = 0

    for i in range(len(arr)):
        for j in range(i, 0, -1):
            comparisons += 1
            if arr[j - 1] > arr[j]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break

    return arr, comparisons

def selection_sort(arr: list) -> tuple[list, int]:
    comparisons = 0
    for i in range(len(arr) - 1, 0, -1):
        maximum = arr[i]
        max_idx = i
        for j in range(i - 1, -1, -1):
            comparisons += 1
            if arr[j] > maximum:
                maximum = arr[j]
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr, comparisons

def merge_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    else:
        mid_idx = len(arr) // 2
        left_sub = merge_sort(arr[:mid_idx])
        right_sub = merge_sort(arr[mid_idx:])
        return merge(left_sub, right_sub)

def merge(left, right):
    ptr_left = 0
    ptr_right = 0

    merged = []

    while ptr_left < len(left) and ptr_right < len(right):
        if left[ptr_left] <= right[ptr_right]:
            merged.append(left[ptr_left])
            ptr_left += 1
        else:
            merged.append((right[ptr_right]))
            ptr_right += 1

    merged += left[ptr_left:]
    merged += right[ptr_right:]

    return merged