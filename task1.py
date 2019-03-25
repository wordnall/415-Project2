from collections import deque
from math import floor
from itertools import islice

def main():
    print("Running Karatsubas large interger multiplication")
    a = deque(input("Enter the value for the first integer: "))
    b = deque(input("Enter the value for the second integer: "))

    print("The product is: ", karatsuba_mult(a, b))


def karatsuba_mult(a, b):

    while len(a) > len(b):
        b.appendleft(0)
    while len(deque_b) > len(deque_a):
        a.appendleft(0)

    if len(a) == 1 and len(b) == 1:
        return deque(str(int(a) * int(b)))


    #A*B = A1*B1*10^2k+(?)*10^k+A0*B0, A1 = K+1, A0 = k, K = floor(n/2)
    k = floor(len_a/2)
    if k % 2:
        a1 = deque(islice(deque_a, 0, k))
        b1 = deque(islice(deque_b, 0, k))
    else:
        a1 = deque(islice(deque_a, 0, k+1))
        b1 = deque(islice(deque_b, 0, k + 1))

    a0 = deque(islice(deque_a, k, len_a))

    b0 = deque(islice(deque_a, k, len_b))

    c2 = karatsuba_mult(a1, b1)
    c0 = karatsuba_mult(a0, b0)
    c1 = karatsuba_mult(a1+a0, b1+b0) - (c2 + c0)

    return pow10(c2, 2*k) + pow10(c1, k) + c0


def pow10(num, power):
    temp = num.copy()
    for x in range(power):
        temp.append('0')

    return temp


def powtest():
    num = deque('55')
    print(pow10(num, 3))
    print(num)


main()

