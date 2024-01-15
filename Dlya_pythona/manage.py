# list1 = []
# for i in range(1, 11):
#     list1.append(i)
# print(list1)

# lisst1 = [i for i in range(1, 11)]
# print(lisst1)

# liast1 = [str(i) for i in range(1,11)]
# print(liast1)

# list2 = [int(i) for i in input().split()]
# print(list2)

# laist3 = [i for i in range(1, 101) if i % 2 == 0]
# print(laist3)

# listr = [i * j for i in range(1, 10) for j in [1, 2, 3]]
# print(listr)

# tuple1 = tuple([i for i in range(1, 10) if i % 2 != 0])
# print(tuple1)
# print(type(tuple1)) 

# dict = {x: x**2 + 1 for x in range(5)}
# print(dict)

# dict1 = {x: y for x in 'ABC' for y in 'XYZ'}
# print(dict1)

# dict2 = {x: 'Z' for x in 'ABC'}
# print(dict2)

# dict3 = {}.fromkeys('ABC', 'z')
# print(dict3)

# dict4 = {x: y for x, y in [('A',0),('B',1),('C',2)]}
# print(dict4)

# dict5 = {x: [y for y in range(x,x+3)]for x in range(4)}
# print(dict5)
 
# dict6 = {x: [y %2 for y in range (10)] for x in 'ABC'}
# print(dict6)

# dict7 = {'ABCDE'[i]:[i % 2]*5 for i in range(5)}
# print(dict7)

# dict8 = {x: {0 for y in 'XYZ'} for x in 'ABC'}
# print(dict8)

dict9 = {x: {y: x for y in 'XYZ'} for x in 'ABC'}
print(dict9)