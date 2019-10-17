import numpy as np
import time
from matplotlib import pyplot as plt


def partition(arr, low, high):
    i = (low - 1)  # 最小元素索引
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引

# 快速排序函数
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def randPartition(arr, low, high):
    pivot = np.random.randint(high - low) + low
    arr[pivot], arr[high] = arr[high], arr[pivot]
    return partition(arr, low, high)


# 随机快速排序函数
def randQuickSort(arr, low, high):
    if low < high:
        pi = randPartition(arr, low, high)
        randQuickSort(arr, low, pi - 1)
        randQuickSort(arr, pi + 1, high)


# arr = [10, 7, 8, 9, 1, 5]
space = np.arange(0, 100000, 100000)
spend = np.zeros(int (100000/100000))
randSpend = np.zeros(int (100000/100000))
for index,i in enumerate(space):
    print(index)
    arr = np.random.randint(0, 100, i)
    randArr = arr.copy()
    n = len(arr)
    # startTime = time.time()
    # quickSort(arr, 0, n - 1)
    # endTime = time.time()
    # spend[index] = endTime - startTime
    randStartTime = time.time()
    randQuickSort(randArr, 0, n - 1)
    randEndTime = time.time()
    randSpend[index] = randEndTime - randStartTime
# arr = np.random.randint(0, 100, 50000)
# print(arr)
# n = len(arr)
# startTime = time.time()
# quickSort(arr, 0, n - 1)
# endTime = time.time()
# print("排序后的数组:")
# for i in range(n):
#     print("%d" % arr[i])
# print("快速排序所用时间为 %s 秒" % (endTime - startTime))
for i, j in zip(space, spend):
    print(i, "个数组排序所花时间为", j, "秒")
plt.plot(space, spend, label = 'QuickSort')
plt.plot(space, randSpend, label='RandQuickSort')
plt.legend()
plt.show()