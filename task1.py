from collections import deque


def main():
    print("Running Karatsubas large interger multiplication")
    a = int(input("Enter the value for the first integer: "))
    b = int(input("Enter the value for the second integer: "))

    print("The product is: ", karatsuba_mult(a, b))


def karatsuba_mult(a, b):
    deque_a = deque(map(int, str(a)))
    deque_b = deque(map(int, str(b)))

    while len(deque_a) > len(deque_b):
        deque_b.appendleft(0)
    while len(deque_b) > len(deque_a):
        deque_a.appendleft(0)
    if len(deque_a) == 1 and len(deque_b) == 1:
        return a * b

    c2 = karatsuba_mult(a1, b1)
    c0 = karatsuba_mult(a0, b0)
    c1 = karatsuba_mult(a1+a0, b1+b0) - (c2 + c0)

    return c2 * 10**(2*k) + c1 * 10**k + c0

main()
