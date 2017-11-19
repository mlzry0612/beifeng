dict1 = {'a': 1, 'b': 2, 'c': [1, 2, 3, 4, 5]}
dict12 = dict1.copy()

print(dict1)
print(dict12)


dict12['b'] = 23
print(dict1)
print(dict12)

dict12['c'][1] = 23432
print(dict1)
print(dict12)

dict12['c'] = [22,33]
print(dict1)
print(dict12)

#copy 只 copy 每一层的  第二层不会影响

