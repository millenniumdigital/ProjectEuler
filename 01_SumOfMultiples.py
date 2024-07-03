"""
PROBLEM 01 - MULTPLES OF 3 OR 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6, and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""

def sum_multiples(multiple1, multiple2, limit):
    i = 0
    sum_i = 0
    while i < limit:
        if (i % multiple1) == 0 or (i % multiple2) == 0:
            sum_i += i
        i +=  1
    return (sum_i)


def main():
    sum_i = sum_multiples(3, 5, 1000)
    print(sum_i)


if __name__ == "__main__":
    main()
