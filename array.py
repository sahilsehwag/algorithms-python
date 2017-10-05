import math


def linearSearch(array, value):
    for i,element in enumerate(array):
        if element is value:
            return i

def binarySearch(array, value): 
    low = 0
    high = len(array)

    while True:
        mid = math.floor((low + high)/2)

        if array[mid] == value: 
            return mid
        elif array[mid] < value: 
            low = mid + 1
        elif value < array[mid]: 
            high = mid - 1
        elif low == high:
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
