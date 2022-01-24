#1.Increment Values by 2 in range and 
# what is step function in for loop
#step function
""" In a for loop, we can use range function(start,end,step) 
the step in the parameter is to incrementing step by step 
after every iteration. Below is the example to increment step by step """

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
for num in range(start, end,2):
    print(num)

#2. Infinite for loop

""" First method is we can create an infinite for loop by
adding iterables which will keep our 
loop going until we run out of memory """

#Example
""" iterables =['never','ending','loop']
for word in iterables:
    print(word)
    iterables.append(word) """

''' We can also use generators that always 
yields another number. The generator will include a 
while true loop'''

#3.How to add values to a tuple
'''Tuples are immutable but we can first convert tuple
 to list and then append the new value to the list then 
 create a new tuple by converting the list.  
'''
Tup = (10,20,30,40)
L1 = list(Tup)
L1.append(50)
New_tup = tuple(L1)
print(New_tup)

