def lowerValue(array):
    lowerValue = array[0] 
    for i in range(0, len(array)):
        if array[i] < lowerValue:
            lowerValue = array[i]
    return lowerValue

def ordenedList(array):
    oldList = array
    newList = []
    for i in range(0, len(array)):
        value = lowerValue(oldList)
        newList.append(value)
        oldList.remove(value)
    return newList


def binarySearch(array, value):
    array = ordenedList(array)
    start, end = 0, len(array) - 1
    if value < array[start] or value > array[end]:
        return - 1
    while True:
        middle = round((start + end)/2)
        if value < array[middle]:
            end = middle
        elif value > array[middle]:
            start = middle
        else:
            return middle
        if value < array[middle]: 
            if value > array[start]: 
                if value != array[middle - 1]:
                    return - 1
