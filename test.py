def quick_sort_inplace(arr, low, high):
    def partition(low, high):
        pivot = arr[high]
        left_index = low

        for right_index in range(low, high):
            if arr[right_index] < pivot:
                arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
                left_index += 1

        arr[left_index], arr[high] = arr[high], arr[left_index]
        return left_index

    if low < high:
        pivot = partition(low, high)
        quick_sort_inplace(arr, low, pivot - 1)
        quick_sort_inplace(arr, pivot + 1, high)

    return arr

arr = [38, 27, 43, 3, 9, 82, 10]
print(quick_sort_inplace(arr, 0, len(arr) - 1))