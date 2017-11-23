import math

if __name__ == '__main__':
    for i in range(100000):
        x = int(math.sqrt(i + 100))
        y = int(math.sqrt(i + 268))

        if x**2 == i+100 and y**2 == i+268:
            print(i)


