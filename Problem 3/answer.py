# Largest Prime Factor
# Find the largest prime factor of N
# with N is user's input

import sys

def largestPrime(N):
    if N < 2:
        return None
    factor = 2
    while (factor * factor <= N):
        while (N % factor == 0 and N != factor):
            N = N // factor
        factor += 1
    return N

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("usage : answer.py <Number>")
        exit()

    N = int(sys.argv[1])

    print(largestPrime(N))
