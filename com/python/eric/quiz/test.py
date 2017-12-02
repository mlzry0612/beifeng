def calc(x):
    return (2 * x + 1)


if __name__ == '__main__':

    for i in range(6):
        if i == 0:
            y = calc(1)
        else:
            y = calc(y)
    print("总共有 %d 条士力架" % y)
