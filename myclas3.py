from myclass2 import Mobile as M
import random
ic = M()
ic.var1 = 22
ic.var2 = 44
ic.showvar()

x = random.randint(1001,1011)
print(f"the random number is {x}")

mylist = ['hello', 'how', 'are', 'you','?']
print(f"the random text is {random.choice(mylist)}")