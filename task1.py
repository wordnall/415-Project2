from collections import deque
from math import floor
from itertools import islice


def main():
    print("Running Karatsubas large interger multiplication")
    a = deque(input("Enter the value for the first integer: "))
    b = deque(input("Enter the value for the second integer: "))

    for i in range(len(a)):
        a[i] = int(a[i])
    for i in range(len(b)):
        b[i] = int(b[i])

    print("The product is: ", "".join(map(str, karatsuba_mult(a, b))))


def deque_arr(a, b, sub):
    a_neg = False
    if a[0] == '-':
        del a[0]
        a_neg = True

    b_neg = False
    if b[0] == '-':
        del b[0]
        b_neg = True

    while len(a) > len(b):
        b.appendleft(0)
    while len(b) > len(a):
        a.appendleft(0)

    k = 0
    while k < len(a) - 1 and a[k] == b[k]:
        k += 1
    bAbsLess = b[k] < a[k]

    if (not bAbsLess) and sub:
        #swap numbers
        sub = not sub
        #a_neg = not a_neg
        b_neg = not b_neg
        swap = b
        b = a
        a = swap
        swap = a_neg
        a_neg = b_neg
        b_neg = swap

    ##now we know abs(a) >= abs(b)
    ##### find deque op
    if (a_neg and not b_neg and not sub) or (a_neg and b_neg and sub):
        ret_deque = deque()
        deque_sub(a, b, ret_deque)
        ret_deque.appendleft('-')
        return ret_deque
    elif (not a_neg and not b_neg and not sub) or (not a_neg and b_neg and sub):
        return deque_add(a, b)
    elif (not a_neg and b_neg and not sub) or (not a_neg and not b_neg and sub):
        return deque_sub(a, b)
    elif (a_neg and b_neg and not sub) or (a_neg and not b_neg and sub):
        ret_deque = (deque_add(a, b).appendleft('-'))
        return ret_deque

def deque_add(a, b):
    #expects two deques of ints, both positive, with a >= b
    ret_deque = deque()

    carry = 0
    for i in range(len(a) - 1, -1, -1):
        carry += a[i] + b[i]
        str_carry = str(carry)

        if len(str_carry) > 1:
            ret_deque.appendleft(int(str_carry[1]))
            carry = int(str_carry[0])
        else:
            ret_deque.appendleft(carry)
            carry = 0

    if carry > 0:
        ret_deque.appendleft(carry)

    return ret_deque


def deque_sub(a, b, ret_deque):
    ret_deque = deque()

    for i in range(len(a) - 1, -1, -1):
        curr_a = a[i]
        curr_b = b[i]
        if abs(curr_b) > curr_a:
            curr_a += 10

            j = i
            while j >= 0 and a[j] == 0:
                a[j] = 9
                j -= 1

            a[j] -= 1
        ret_deque.appendleft(curr_a - curr_b)
    return #ret_deque.copy()


def karatsuba_mult(a, b):
    ret_neg = False
    if a[0] == '-':
        ret_neg = not ret_neg
        del a[0]
    if b[0] == '-':
        ret_neg = not ret_neg
        del b[0]

    while len(a) > len(b):
        b.appendleft(0)
    while len(b) > len(a):
        a.appendleft(0)

    if len(a) == 1 and len(b) == 1:
        ret_deque = deque(str(a[0] * b[0]))
        for i in range(len(ret_deque)):
            ret_deque[i] = int(ret_deque[i])
        if ret_neg:
            ret_deque.appendleft('-')
        return ret_deque


    #A*B = A1*B1*10^2k+(C1)*10^k+A0*B0, A1 = K+1, A0 = k, K = floor(n/2)
    k = floor(len(a)/2)
    if (len(a) % 2) == 0:
        a1 = deque(islice(a, 0, k))
        b1 = deque(islice(b, 0, k))
        a0 = deque(islice(a, k, len(a)))
        b0 = deque(islice(b, k, len(b)))

    else:
        a1 = deque(islice(a, 0, k + 1))
        b1 = deque(islice(b, 0, k + 1))
        a0 = deque(islice(a, k + 1, len(a)))
        b0 = deque(islice(b, k + 1, len(b)))

    c2 = karatsuba_mult(a1, b1)
    c0 = karatsuba_mult(a0, b0)
    c1 = deque_arr(karatsuba_mult(deque_arr(a1, a0, False), deque_arr(b1, b0, False)), deque_arr(c2, c0, False), True)

    return pow10(c2, 2*k) + pow10(c1, k) + c0


def pow10(num, power):
    temp = num.copy()
    for x in range(power):
        temp.append(0)

    return temp


def powtest():
    num = deque('55')
    print(pow10(num, 3))
    print(num)


def dequeaddtest():
    a = deque(input("Enter value1 for deq add: "))
    b = deque(input("Enter value2 for deq add: "))
    addorsub = input("subtraction?")
    while a or b != 'q':
        while len(a) > len(b):
            b.appendleft(0)
        while len(b) > len(a):
            a.appendleft(0)
        for i in range(len(a)):
            a[i] = int(a[i])
            b[i] = int(b[i])

        print(deque_arr(deque(a), deque(b), addorsub == 't'))
        a = deque(input("Enter value1 for deq add: "))
        b = deque(input("Enter value2 for deq add: "))
        addorsub = input("subtraction?")


#main()
dequeaddtest()