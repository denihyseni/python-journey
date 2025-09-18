import time


arr = [13,11,12,7,4,3,1,0]
target = 4
left = 0
right = len(arr) - 1


while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        print(f'Target found ')
        break
    elif arr[mid] < target:
        left = mid + 1
        print('Pointer is smaller')
        time.sleep(0.5)
    else:
        right= mid -1
        print('Pointer is bigger')
        time.sleep(0.5)

