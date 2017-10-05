import math



#SEARCHING ALGORITHMS
def linearSearch(array, value):
    for i,element in enumerate(array):
        if element is value:
            return i

def binarySearch(array, value): 
    left = 0
    right = len(array)

    while True:
        mid = math.floor((left + right)/2)

        if array[mid] == value: 
            return mid
        elif array[mid] < value: 
            left = mid + 1
        elif value < array[mid]: 
            right = mid - 1
        elif left == right:
            return -1
    return -1

def interpolationSearch(array, value): 
    left = 0
    right = len(array) - 1

    while True:
        pos = math.floor(left + (((right - left)/(array[right] - array[left])) * (value - array[left])))
        if array[pos] == value: 
            return pos
        elif array[pos] < value: 
            left = pos + 1
        elif value < array[pos]: 
            right = pos - 1
        elif left == right:
            return -1
    return -1

def gallopingSearch(array, value): 
    left = 0
    right = len(array) - 1

    if value < array[left] or value > array[right]: return -1

    step = 1

    while left <= right and array[left] < value:
        left += step
        step *= 2

    if left <= right:
        right = left
    left /= 2

    while True:
        mid = math.floor((left + right)/2)

        if array[mid] == value: 
            return mid
        elif array[mid] < value: 
            left = mid + 1
        elif value < array[mid]: 
            right = mid - 1
        elif left == right:
            return -1
    return -1

def jumpSearch(array, value):
    step = math.floor(math.sqrt(len(array)))
    left = 0
    right = step

    while True:
        if right >= len(array):
            right = len(array) - 1

        if array[right] < value:
            if right == len(array) - 1: return -1
            else:
                left = right + 1
                right += (step + 1)
        elif array[right] > value:
            break
        elif array[right] == value:
            return right

    for i in range(left, right + 1):
        if array[i] ==  value: 
            return i
    return -1
def ternarySearch(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        mid1 = round(left + (right - left) / 3)
        mid2 = round(mid1 + (right - left) / 3)

        if array[mid1] == value: return mid1
        if array[mid2] == value: return mid2

        if value < array[mid1]:
            right = mid1 - 1
        elif array[mid1] < value < array[mid2]:
            left = mid1 + 1
            right = mid2 - 1
        elif array[mid2] < value:
            left = mid2 + 1
    return -1
#SEARCHING ALGORITHMS



#SORTING ALGORITHMS
def insertionSort(array): pass

def selectionSort(array): pass

def bubbleSort(array): pass

def shellSort(array): pass

def mergeSort(array): pass

def quickSort(array): pass

def countingSort(array): pass

def radixSort(array): pass

def heapSort(array): pass
#SORTING ALGORITHMS
