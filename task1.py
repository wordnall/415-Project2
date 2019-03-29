
from collections import deque
from math import floor
from itertools import islice


def main():
    print("Running Karatsubas large interger multiplication")
    a = deque(input("Enter the value for the first integer: "))
    b = deque(input("Enter the value for the second integer: "))

    while a or b != 'q':
        for i in range(len(a)):
            a[i] = int(a[i])
        for i in range(len(b)):
            b[i] = int(b[i])
        product = karatsuba_mult(a, b)
        while len(product) > 0 and product[0] == 0:
            product.popleft()
        print("The product is: ", "".join(map(str, product)))

        print("Running Karatsubas large interger multiplication")
        a = deque(input("Enter the value for the first integer: "))
        b = deque(input("Enter the value for the second integer: "))


def main2():
    print("Running exponentiator using karatsuba multiplication")
    a = int(input("Enter the value for the first integer: "))
    b = int(input("Enter the value for the second integer: "))

    while a or b != 'q':
        product = exp(a, b)
        while len(product) > 0 and product[0] == 0:
            product.popleft()
        print("The product is: ", "".join(map(str, product)))

        print("Running exponentiator using karatsuba multiplication")
        a = int(input("Enter the value for the first integer: "))
        b = int(input("Enter the value for the second integer: "))


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
    aAbsGrtrEql = a[k] >= b[k]

    # make b positive
    if b_neg:
        b_neg = not b_neg
        sub = not sub

    # if subtracting large positive b, swap
    if (not aAbsGrtrEql) and sub:
        # form is (+/-a) - (+B)
        # change this to:
        #    (-B) + (+/-a)
        sub = not sub
        b_neg = not b_neg
        swap = b
        b = a
        a = swap
        swap = a_neg
        a_neg = b_neg
        b_neg = swap
    # now we know abs(a) >= abs(b)
    ##### find deque op
    if (a_neg and not b_neg and not sub) or (a_neg and b_neg and sub):
        ret_deque = (deque_sub(a, b).appendleft('-'))
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


def deque_sub(a, b):
    ret_deque = deque()

    for i in range(len(a) - 1, -1, -1):
        curr_a = a[i]
        curr_b = b[i]
        if abs(curr_b) > curr_a:
            curr_a += 10

            j = i - 1
            while j >= 0 and a[j] == 0:
                a[j] = 9
                j -= 1

            a[j] -= 1
        ret_deque.appendleft(curr_a - curr_b)
    return ret_deque


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

    retval = deque_arr(deque_arr(pow10(c2, 2*k), pow10(c1, k), False), c0, False)

    return retval


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
    a = input("Enter value1 for deq add: ")
    b = input("Enter value2 for deq add: ")
    addorsub = input("subtraction?")
    while a or b != 'q':
        print(deque_add(deque(a), deque(b), addorsub == 't'))
        a = input("Enter value1 for deq add: ")
        b = input("Enter value2 for deq add: ")
        addorsub = input("subtraction?")


def test():
    print("Running Karatsubas large interger multiplication")
    errorCount = 0
    for k in range(1, 1000, 1):
        a = deque(str(k))
        for j in range(1, 1000, 1):
            b = deque(str(j))

            for i in range(len(a)):
                a[i] = int(a[i])
            for i in range(len(b)):
                b[i] = int(b[i])
            product = karatsuba_mult(a, b)
            while len(product) > 0 and product[0] == 0:
                product.popleft()
            if "".join(map(str, product)) != str(j*k):
                errorCount += 1
                print("Erroneous inputs found:\n", "a: ", a, "\n", "b: ", b, "\n", )

    print("Total erroneous inputs: ", errorCount)


# def exp(a, b):
#     temp = deque(str(a))
#     a = temp
#     for i in range(len(temp)):
#         a[i] = int(a[i])
#
#     ret_val = 0
#     while b > 1:
#         # # temp = deque(str(a))
#         # # for i in range(len(temp)):
#         # #     a[i] = int(a[i])
#         #
#         # a = temp
#         ret_val = exp(karatsuba_mult(a, a), floor(b / 2))
#         if not (b % 2):
#             ret_val = karatsuba_mult(ret_val, a)
#
#     return ret_val


# test()
# main()
# begin part 2 code for exponentiation


def exp(a, b):

    if b == 0:
        ret_deque = deque()
        ret_deque.append(1)
        return ret_deque

    if b % 2 == 0:
        val = exp(a, b/2)
        return karatsuba_mult(val, val)
    else:
        val = exp(a, (b-1)/2)
        return karatsuba_mult(karatsuba_mult(val, val), a)


def mainAL():
    a = deque(input("Enter the value for the first integer: "))
    b = int(input("Enter the value for the second integer: "))

    for i in range(len(a)):
        a[i] = int(a[i])

    result = exp(a, b)
    while len(result) > 0 and result[0] == 0:
        result.popleft()
    print("The product is: ", "".join(map(str, result)))


def test2():
    print("Running Exponentiation")
    errorCount = 0
    for k in range(1, 1000, 1):
        a = deque(k)
        for j in range(1, 1000, 1):
            b = j

            for i in range(len(a)):
                a[i] = int(a[i])
            result = exp(a, b)
            while len(result) > 0 and result[0] == 0:
                result.popleft()
            if "".join(map(str, result)) != str(k**j):
                errorCount += 1
                print("Erroneous inputs found:\n", "a: ", a, "\n", "b: ", b, "\n", )

    print("Total erroneous inputs: ", errorCount)


test2()
