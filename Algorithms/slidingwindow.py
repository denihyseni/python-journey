#All solved by me with the help of ChatGpt which only gives me nudges if im on the right path or not and google on websites like stackoverflow w3 schools etc the whole thought process and implementation is done by me


import sys

def maxSum(arr,n,k):
    max_sum = -sys.maxsize
    current_sum = 0
    i = 0

    if i < 1:
        for j in range(k):
            current_sum += arr[i+j]
            max_sum = max(current_sum , max_sum)
    i = i + 1

    for i in range(1,n-k+1):
        current_sum = current_sum - arr[i-1] + arr[i+k]
        max_sum = max(current_sum , max_sum)

    return max_sum

if __name__ == "__main__":
    arr = [5, 2, -1, 0, 3, 4, 7 , 6, 5 , -4]
    k = 4
    n = len(arr)
    print(maxSum(arr,n,k))
    
            