#list methods

L1=[1,2,3,12,9]
#1. append
L1.append(23)
print(L1)

#2.sort
L1.sort()
print(L1)

#3.reverse
L1.reverse()
print(L1)

#4.pop
L1.pop()
print(L1)

#5.remove
L1.remove(2)
print(L1)

#6.index
x = L1.index(9)
print(x)

#7.insert
L1.insert(3,129)
print(L1)

#8.extends
L2 = ['numbers','numericals','integer']
L2.extend(L1)
print(L2)

#9.count
x = L1.count(12)
print(x)

#10.copy
L3 = L1.copy()
print(L3)

#11.clear
L1.clear()
print(L1)