# Powerful digit sum
# Find the maximum digital sum of a^b where a, b < N
# with N is user's input

import sys

def powerfulDigitSum(N):
    maxSum = 0
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in str(i ** j):
                sum += int(k)
            if sum > maxSum :
                maxSum = sum
    return maxSum

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("usage : answer.py <Number>")
        exit()

    N = int(sys.argv[1])

    print(powerfulDigitSum(N))
