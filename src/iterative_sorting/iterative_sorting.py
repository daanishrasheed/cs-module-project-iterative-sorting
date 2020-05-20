# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for j in range(i+1, len(arr)):
            if arr[smallest_index] > arr[j]:
                smallest_index = j


        # TO-DO: swap
        # Your code here
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here
    o = [0 for i in range(256)]
    c = [0 for i in range(256)]
    a = ["" for _ in arr]
    for i in arr:
        c[ord(i)] += 1

    for i in range(256):
        c[i] += c[i-1]

    for i in range(len(arr)):
        o[c[ord(arr[i])]-1] = arr[i]
        c[ord(arr[i])] -= 1

    for i in range(len(arr)):
        arr[i] = o[i]

    return arr
