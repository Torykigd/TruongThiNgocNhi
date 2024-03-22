import anvil.server

anvil.server.connect(BAI3)

# Hàm sắp xếp dãy số nguyên bằng Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Hàm sắp xếp dãy số nguyên bằng Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Hàm sắp xếp dãy số nguyên bằng Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Hàm sắp xếp dãy số nguyên bằng Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Event handler cho sự kiện khi nhấn nút sắp xếp
@anvil.server.callable
def sort_numbers(numbers, algorithm):
    numbers = [int(x) for x in numbers.split(",")]
    
    if algorithm == "Insertion Sort":
        sorted_numbers = insertion_sort(numbers)
    elif algorithm == "Selection Sort":
        sorted_numbers = selection_sort(numbers)
    elif algorithm == "Bubble Sort":
        sorted_numbers = bubble_sort(numbers)
    elif algorithm == "Merge Sort":
        sorted_numbers = merge_sort(numbers)
    else:
        sorted_numbers = numbers
        
    return sorted_numbers
