import sys

#Kadanes algorithm most efficient solve O(n)


def maxNum(arr):
    current_max = float('-inf')
    global_max = current_max
    
    i = 0

    for i in arr:
        current_max = max(i, current_max + i)
        global_max = max(global_max , current_max)

    return global_max
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(maxNum(arr))
