#Dictionary Methods

d1={"Mit": "Football","Nimish":"F1"}

#1.copy
d2 = d1.copy()
print(d2)

#2.clear
d2.clear()
print(d2)

#3.get
x= d1.get("Mit")
print(x)

#4.items
x= d1.items()
print(x)

#5. keys
x= d1.keys()
print(x)

#6. update
d1.update({"Aaditya":"Extrovert"})
print(d1)

#7.values
x= d1.values()
print(x)

#8.pop
d1.pop("Nimish")
print(d1)

#9. setdefault
x= d1.setdefault("Nimish","F1")
print(x)

#10.popitem
d1.popitem()
print(d1)

#11.fromkeys
x=('Mit','Nimish')
y=0

thisdict=dict.fromkeys(x,y)
print(thisdict)

