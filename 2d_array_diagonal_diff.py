import math
import os
import re
import sys
import random

def diagonalDifference(arr):
    leftToRight_diagonal_sum = 0
    rightToLeft_diagonal_sum = 0
    
    for i in range(0, len(arr)):
        leftToRight_diagonal_sum += arr[i][i]
        
    for j in range(0, len(arr)):
        rightToLeft_diagonal_sum += arr[j][len(arr)-1-j]
        
    return abs(leftToRight_diagonal_sum - rightToLeft_diagonal_sum)

if __name__ == "__main__":
    fptr = open(os.environ['OUTPUT_PATH', 'w'])
    n = int(input().strip())
    
    arr = []
    
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    # print(result)
    
    fptr.write(str(result) + '\n')
    fptr.close()