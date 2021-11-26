def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    while True:
        middle = round((start + end)/ 2)
        if (array[middle] < value):
            start = middle
        elif (array[middle] > value):
            end = middle
        else:
            return middle


print(binarySearch([5, 10, 15, 20, 25, 30, 35, 40], 20))
