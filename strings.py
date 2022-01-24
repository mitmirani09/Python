
# String methods 
# 1. capitalize
string = "hey, python is amazing."
new_string =string.capitalize()
print(new_string)
#2. Case fold
txt = "HEY, PYTHON IS AMAZING."
new_txt = txt.casefold()
print(new_txt)
#3.center
txt = "Fruits"
new_txt = txt.center(30)
print(new_txt)
#4.count 
txt = "fruits are healthy and fruits are tasty"
new_txt = txt.count("fruits")
print(new_txt)
#5.encode
txt = "eåsy to understånd."
new_txt = txt.encode()
print(new_txt)
#6. endswith
new_txt = txt.endswith(".")
print(new_txt)
#7. expandtabs
txt = "H\tE\tY"
new_txt = txt.expandtabs(3)
print(new_txt)
#8. find
txt = "hello, this is python world."
new_txt = txt.find("python")
print(new_txt)
#9. format
txt = "My name is {name},I am {age}".format(name = "Mit",age=19)
print(txt)
#10.index
txt = "hello, this is python world."
new_txt = txt.index("python")
print(new_txt)
#11.isalnum
txt = "#Iris1209"
new_txt = txt.isalnum()
print(new_txt)
#12.isalpha
new_txt = txt.isalpha()
print(new_txt)
#13.isdecimal
new_txt = txt.isdecimal()
print(new_txt)
#14.isdigit
new_txt = txt.isdigit()
print(new_txt)
#15.isidentifier
new_txt = txt.isidentifier()
print(new_txt)
#16. islower
new_txt = txt.islower()
print(new_txt)
#17.isnumeric
new_txt = txt.isnumeric()
print(new_txt)
#18.isprintable
new_txt = txt.isprintable()
print(new_txt)
#19.isspace
new_txt = txt.isspace()
print(new_txt)
#20 istitle
new_txt = txt.istitle()
print(new_txt)
#21.isupper
new_txt = txt.isupper()
print(new_txt)

#22.lower
txt = "Paris is my favourite place."
new_txt = txt.lower()
print(new_txt)
#23.upper
new_txt = txt.upper()
print(new_txt)
#24.ljust
new_txt = txt.ljust(5)
print(new_txt,"It is a very awesome place to visit.")
#25.lstrip
sample = "    Paris     "
new_sample = sample.lstrip()
print("of all places",new_sample,"is my fav.")
new_sample = sample.rstrip()
print("of all places",new_sample,"is my fav.")
#26.join
tup = ("My","Fav","Place","is","Paris")
x = " ".join(tup)
print(x)
#27.maketrans
x= "ris"
y= "cela"
mytable = txt.maketrans(x,y)
print(txt.translate(mytable))
#28.partition
x = txt.partition("my")
print(x)
#29.replace
x= txt.replace("Paris","New York")
print(x)
#30.rfind
x= txt.rfind("favourite")
print(x)
#31.rindex
x= txt.rindex("favourite")
print(x)
#32.rpartition
x= txt.rpartition("my")
print(x)
#33.rsplit
x= txt.rsplit("my")
print(x)
#34.split
x= txt.split("my")
print(x)
#35.startswith
x= txt.startswith("Paris")
print(x)
#36.swapcases
x= txt.swapcases()
print(x)
#37.title
x= txt.title()
print(x)
#38.zfill
y= "10"
x = txt.zfill(10)
print(x)
#39.split lines
y="Paris is amazing \n Also my fav place"
x = txt.splitlines()
print(x)


