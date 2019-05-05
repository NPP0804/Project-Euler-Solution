# Multiple of 3 and 5
# Find the sum of all the multiples of 3 or 5 in range [0,N)
# with N is user's input

import sys

# Find sum of all the multiple of P in range [0,N)
def sumMultipleP(N, P):
    sum = 0;
    for i in range(P, N, P):
        sum += i
    return sum

def Multiple35(N):
    return sumMultipleP(N,3) + sumMultipleP(N,5) - sumMultipleP(N, 15)

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("usage : answer.py <Maximum Boundary>")
        exit()

    N = int(sys.argv[1])

    print(Multiple35(N))
