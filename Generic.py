for x in range(1,6,2):
    print(x)
    
print("\n-----Second loop-----")

mylist = ['my', 'name', 'abhishek']
for x in mylist:
    print(x)

#convert range to list
num = list(range(1,6,2))
print(num)

mylist=[]
for x in range(1,11):
    num = x**2
    mylist.append(num)

print(mylist)

print(f"Max={max(mylist)}")
print(f"Min={min(mylist)}")
print(f"Sum={sum(mylist)}")