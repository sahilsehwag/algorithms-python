import math
import pprint
import sys



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

    step = 1

    while True:
        if array[left] < value:
            if left > right: break
            left += step
            step *= 2
        else: 
            if left <= right:
                right = left
                left = left / 2
                break

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


def fibonacciSeach(array, value):
    pass
#SEARCHING ALGORITHMS



#SORTING ALGORITHMS
def insertionSort(array): 
    for i in range(1, len(array)):
        if array[i] < array[i-1]:
            for j in range(i, 0, -1):
                if array[j-1] <= array[j]:
                    break
                else:
                    array[j], array[j-1] = array[j-1], array[j]


def selectionSort(array): 
    i = 0

    while i < len(array):
        min = array[i]
        minIndex = i

        for j in range(i, len(array)):
            if array[j] < min:
                min = array[j]
                minIndex = j

        array[minIndex], array[i] = array[i], array[minIndex]
        i += 1


def bubbleSort(array): 
    i = len(array)
    while i > 0:
        for j in range(i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        i -= 1


def shellSort(array): 
    k = math.floor(len(array) / 2)

    while k > 0:
        for i in range(0, len(array) - k):
            if array[i] > array[i+k]:
                for j in range(i, -1, -k):
                    if array[j] <= array[j+k]:
                        break
                    else:
                        array[j], array[j+k] = array[j+k], array[j]
            
        k = math.floor(k/2)


# def mergeSort(array): 
    # def merge(array, left, right):
        # result = []

        # l = 0
        # for i in range(len(left) + len(right)):


    # def partition(array, left, mid, right):
        # mid = math.floor(len(array))
        # if left >= right:
            # return
        # return partition(array, left, mid)
        # return partition(array, mid+1, right)

    # partition(array, left, right)



def quickSort(array): pass

def countingSort(array): 
    counts = [0] * (max(array)+1)

    for e in array:
        counts[e] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i-1]

    sortedArray = [None] * len(array)
    for e in array:
        if counts[e] > 0:
            sortedArray[counts[e]-1] = e
            counts[e] -= 1

    return sortedArray


def radixSort(array): 
    if len(array) == 0: return array

    maxValue = max(array)
    k = 10
    m = 1

    while maxValue % k // m != 0 or maxValue // k != 0:
        digits = [[] for _ in range(10)]
        for e in array:
            digits[e % k // m].append(e)

        array = []
        for es in digits:
            for e in es:
                array.append(e)

        m *= 10
        k *= 10

    return array


def heapSort(array): pass
#SORTING ALGORITHMS
