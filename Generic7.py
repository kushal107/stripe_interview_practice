"""def printlist(*mylist01):
    t = 2
    #mylist01.append(t)
    for x in mylist01:
        print (x**2)
    print(mylist01)

#mylist = [44,55,77]
printlist(2,5,7,8)
#print(mylist)"""

def printdict(**dict01):
    for x,y in dict01.items():
        print(f"{x} = {y}")

mydict = {'k1':1, 'k2':2}
#printdict(mydict)
printdict(a=1,b=2)