# Assignment Q1. Comparison and Assignment operators

#Assignment operators
print("Set1")
x=5
print(x)
x+=3
print(x)
x-=2
print(x)
x*=4
print(x)
x/=2
print(x)
x%=3
print(x)

print("--------------------------------")
print("Set2")
x=10
print(x)
x+=6
print(x)
x-=4
print(x)
x*=8
print(x)
x/=4
print(x)
x%=6
print(x)

print("--------------------------------")
print("Set3")
x=15
print(x)
x+=9
print(x)
x-=6
print(x)
x*=12
print(x)
x/=6
print(x)
x%=9
print(x)

print("--------------------------------")
print("Set4")
x=12
print(x)
x+=9
print(x)
x-=9
print(x)
x*=12
print(x)
x/=9
print(x)
x%=12
print(x)

#Comparison operators
print("--------------------------------")
print("Set1")
x=5
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print("--------------------------------")
print("Set2")
x=12
y=9
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print("--------------------------------")
print("Set3")
x=14
y=20
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print("--------------------------------")
print("Set4")
x=10
y=25
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)


#Assignment Q2. If else

#First statement: If it snows I will go out else i will not
print("--------------------------------")
snows = 0

if snows == 1:
    print("I will go out.")
else:
    print("I will not go out.")

print("--------------------------------")
snows = 1
if snows == 1:
    print("I will go out.")
else:
    print("I will not go out.")

#Second statement:If it rains frogs will dance
print("--------------------------------")
rains =0
if rains == 1:
    print("Frogs will dance.")
#It will not print anything because no else is present and the condition is not satisfied for if
print("--------------------------------")
rains =1
if rains == 1:
    print("Frogs will dance.")
