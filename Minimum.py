def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min_index=i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index=j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)

elements = [2,6,5,1,3,4]
selection_sort(elements)