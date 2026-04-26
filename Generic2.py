mylist = [x**2 for x in range(1,11)]
print(mylist)

print(mylist[1:5:2])
yourlist = []
yourlist = mylist[:]
print(f"yourlist is this{yourlist}")

print("\n******************")
mylist.append(92)
yourlist.append(72)
print(f"My{mylist}")
print(f"your{yourlist}")

print("\n******************\n")

mytuple = 3,4,88
for x in mytuple:
    print(x)

mytuple = 55,99,101
print(mytuple)

print("\n**************************\n")

mycars = ['audi', 'bmw', 'volkswagen', 'toyota']
for car in mycars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

x = 'abc'
y = x.upper()

print(x,y)

if 'Audi' not in mycars:
    print('got the value')
else:
    print('value not found')

print("\n**************************\n")
a = 3
if a == 2:
    print('1st')
elif a == 4:
    print('2nd')
elif a == 3:
    print('3rd')

mylist2 = []
print(len(mylist2))


print("\n*****My dictionaries*******\n")
my_dict = {'balien1':'A1', 
           'alien2':5, 
           'ka':33,
           'mw':33}
my_dict['alien5'] = 'this is the fifth alien'

print(my_dict['balien1'])
#print(my_dict[2])
print(my_dict)

my_val = my_dict.get('alien2','no such alien exists')
print(my_val)

for x,y in my_dict.items():
    print(x,y)

if 18 in my_dict:
    print('yes its there')

print("MY DICT")
my_dict5 = dict(sorted(my_dict.items()))
print(my_dict5)

for x in set(my_dict.values()):
    print(x)

my_set = {1, 2, 4, 1, 5}
print(my_set)

print("/n***********NESTING*********/n")

my_list = []
d1 = {'a1': 1, 'a2': 2}

for x in range(10):
    my_list.append(d1)

for x in my_list:
    if x['a1'] == 1:
        print('its done')


my_dict = {
        'x1' : [1,2,3],
        'y1' : [4,5,6]
        }

for k1, v1 in my_dict.items():
    print(k1,v1)