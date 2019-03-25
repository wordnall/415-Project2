from collections import deque
from math import floor
from itertools import islice

def main():
    print("Running Karatsubas large interger multiplication")
    a = int(input("Enter the value for the first integer: "))
    b = int(input("Enter the value for the second integer: "))

    print("The product is: ", karatsuba_mult(a, b))


def list_add(a, b, neg_b):
    ret_list = {}

    carry = 0
    for i in range(len(a - 1)):
        if neg_b:
            curr_b = int(-1 * b[i])
        else:
            curr_b = int(b[i])

        carry = string(int(a[i]) + curr_b + carry)
        str_carry = string(carry)
        if carry < 0:
            comp_len = 2
            str_carry = str_carry[1:]
            sign = "-"
        else:
            comp_len = 1
            sign = ""

        if len(str_carry) > comp_len:
            ret_list.prepend(int(str_carry[1]))
            carry = sign + str_carry[0]
        else:
            ret_list.append(abs(carry))
            carry = "0"

    if int(carry) > 0:
        ret_list.prepend(int(carry))

    return ret_list

def karatsuba_mult(a, b):
    deque_a = deque(map(int, str(a)))
    deque_b = deque(map(int, str(b)))

    while len(deque_a) > len(deque_b):
        deque_b.appendleft(0)
    while len(deque_b) > len(deque_a):
        deque_a.appendleft(0)

    len_a = len(deque_a)
    len_b = len(deque_b)
    if len_a == 1 and len_b == 1:
        return int(a) * int(b)


    #A*B = A1*B1*10^2k+(C1)*10^k+A0*B0, A1 = K+1, A0 = k, K = floor(n/2)
    k = floor(len_a/2)
    if k % 2:
        a1 = list(islice(deque_a, 0, k))
        b1 = list(islice(deque_b, 0, k))
    else:
        a1 = list(islice(deque_a, 0, k+1))
        b1 = list(islice(deque_b, 0, k + 1))

    a0 = list(islice(deque_a, k, len_a))
    b0 = list(islice(deque_a, k, len_b))

    c2 = karatsuba_mult(a1, b1)
    c0 = karatsuba_mult(a0, b0)
    c1 = karatsuba_mult(list_add(a1, a0), list_add(list_add(b1, b0), list_add(c2 + c0)), true)
    
    return c2 * 10**(2*k) + c1 * 10**k + c0;

main()
