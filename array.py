import math



def binarySearch(array, value): 
    left = 0
    right = len(array)

    while True:
        mid = math.floor((left + right)/2)

        if array[mid] == value: 
            return mid
        elif array[mid] < value: 
            left = mid
        elif value < array[mid]: 
            right = mid
        else:
            return -1
    return -1


def interpolationSearch(array, value): pass


def gallopingSearch(array, value): pass


def insertionSort(array): pass


def selectionSort(array): pass


def bubbleSort(array): pass


def shellSort(array): pass


def mergeSort(array): pass


def quickSort(array): pass


def countingSort(array): pass


def radixSort(array): pass


def heapSort(array): pass
