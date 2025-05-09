# 冒泡排序
## 通义灵码提供
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == '__main__':
    arr = [3, 2, 1, 5, 4]
    bubbleSort(arr)
    print(arr)

