for letter in 'Python':  # 第一个实例
    print('当前字母 :', letter)

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print('当前水果 :', fruit)

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print
            '%d 等于 %d * %d' % (num, i, j)
            break  # 跳出当前循环
    else:  # 循环的 else 部分, 只要不是 break 的都进else
        print(num, '是一个质数')

sequence = [12, 34, 34, 23, 45, 76, 89]
# 使用内置 enumerate 函数进行遍历:
for index, item in enumerate(sequence):
    print("index is %s, the value is %s" % (index, item))

s = 'qazxswedcvfr'
for i in range(0, len(s), 2):
    print(s[i])

# 冒泡排序# 定义列表 list
arays = [1, 8, 2, 6, 3, 9, 4]
number = 0
for i in range(len(arays)):
    for j in range(i + 1):
        print("i is %s, j is %s" %(i, j))
        number += 1
        if arays[i] < arays[j]:
            arays[i], arays[j] = arays[j], arays[i]
            print(arays)
print("Total number is %s" % number)


nums = [1, 8, 2, 6, 3, 9, 4]
number = 0
for i in range(len(nums) - 1):    # 这个循环负责设置冒泡排序进行的次数, len为7，
    for j in range(len(nums)-i-1):  # ｊ为列表下标  -1防止下标越界
        number += 1
        print("i is %s, j is %s" % (i, j))
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            print(nums)
print("Total number is %s" % number)

