my_dict = {}
my_dict['k2'] = 1
my_dict['k1'] = 2

print(my_dict)
for x in my_dict.values():
    print(x)

my_dict2 = dict(sorted(my_dict.items()))
print(my_dict2)
print(my_dict)