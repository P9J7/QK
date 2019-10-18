import numpy as np
import time
from matplotlib import pyplot as plt
import sys


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)


def randPartition(arr, low, high):
    pivot = np.random.randint(high - low) + low
    arr[pivot], arr[high] = arr[high], arr[pivot]
    return partition(arr, low, high)


def randQuickSort(arr, low, high):
    if low < high:
        pi = randPartition(arr, low, high)
        randQuickSort(arr, low, pi - 1)
        randQuickSort(arr, pi + 1, high)


def experiment(start, end, step):
    space = np.linspace(start, end, step + 1, dtype=int)
    print(space)
    spend = np.zeros(step + 1)
    print(spend)
    randSpend = np.zeros(step + 1)
    print(randSpend)
    for index,i in enumerate(space):
        print(index)
        arr = np.random.randint(0, 100, i)
        # 生成顺序数组
        # arr = np.linspace(0, 100, i + 1)
        randArr = arr.copy()
        n = len(arr)
        startTime = time.clock()
        quickSort(arr, 0, n - 1)
        endTime = time.clock()
        spend[index] = endTime - startTime
        randStartTime = time.clock()
        randQuickSort(randArr, 0, n - 1)
        randEndTime = time.clock()
        randSpend[index] = randEndTime - randStartTime
    return space, spend, randSpend


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    space, spend, randSpend = experiment(0, 100000, 5)
    for i, j in zip(space, spend):
        print(i, "个数组快速排序所花时间为", j, "秒")
    for i, j in zip(space, randSpend):
        print(i, "个数组随机快速排序所花时间为", j, "秒")
    plt.plot(space, spend, label = 'QuickSort')
    plt.plot(space, randSpend, label='RandQuickSort')
    plt.legend()
    plt.show()