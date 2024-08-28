#Declare list and print
'''
num = [1,2,3,4]
print("num ia :",num)
num.append(4)
print(num)
x = num.pop()
print(num[0])
for x in num:
    print(x)
print("Done")
'''

#Declare Tuple
'''
num = 1,2,3,4
print(num)

sal = {"A":1,"B":2,"c":3}
print(sal)
for item in sal.keys():
    print(item)
for item in sal.values():
    print(item)
for key,val in sal.items():
    print(key,val)
print("A" in sal)
# Sets
s = {1,2,3}
print(type(s))
'''
#Comprehnsion
'''
l = []
for x in range(0,10):
    l.append(x)
    print(l)
'''
#######
l = [x for x in range(0,10)]
print(l)
t = tuple(x for x in range(0,10))
print(t)
s = {x for x in range(0,10)}
print(s)
d = {x:x*x for x in range(0,10)}
print(d)





