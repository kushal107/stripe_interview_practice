def create_inc_list(orig_list,incremented_list):
    while(orig_list):
        current_number = orig_list.pop()
        incremented_list.append(current_number+1)

def display_inc_list(mylist):
    print(mylist)

o_list = [4,5,6]
i_list = []

create_inc_list(o_list[:],i_list)
display_inc_list(i_list)
print(o_list)

my_sentence = "this is sparta"
print(my_sentence.title())