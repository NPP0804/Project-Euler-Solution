# Self Powers
# Find the last 10 digits of the series 1^1 + 2^2 + ... + N ^ N
# with N is user's input

import sys

def selfPowers(N):
    limit = 10000000000
    answer = 0
    for i in range(1, N + 1):
        powerResult = (i ** i) % limit
        answer = (answer + powerResult) % limit
    return answer

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("usage : answer.py <Number>")
        exit()

    N = int(sys.argv[1])

    print(selfPowers(N))
