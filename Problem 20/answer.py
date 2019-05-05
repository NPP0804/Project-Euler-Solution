# Factorial Digit Sum
# Find the sum of the digits in the number N!
# with N is user's input

import sys

# My Implementation of factorial function
# Assumed the input N is always true (>=0)
def factorial(N):
    if N < 0 : return None
    result = 1
    for i in range(2, N+1):
        result *= i
    return result

def factorialDigitSum(N):
    if N < 0 : return None
    factorialResult = factorial(N)
    answer = 0
    for i in str(factorialResult):
        answer += int(i)
    return answer

if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("usage : answer.py <Number>")
        exit()

    N = int(sys.argv[1])

    print(factorialDigitSum(N))
