def sum_even(n):
    sum = 0
    for i in range(2, n, 2):
        sum += 1/i
    print("input n is %d, sum is%s" %(n, sum))


def sum_odd(n):
    sum = 0
    for i in range(1, n, 2):
        sum += 1/i
    print("input n is %d, sum is%s" %(n, sum))


if __name__ == '__main__':
    n = int(input("Please entire the number"))
    if n%2 == 0:
        sum_even(n)
    else:
        sum_odd(n)



