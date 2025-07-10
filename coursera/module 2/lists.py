# lists can store multiple values that can be changed later on in the code
# to make a list do this variable_name = [value1, value2, value3]
    # a list can hold an infinite amount of values
    # the values can be any data type
# to get the length of the list do len(list_name)
# to get items in the list do list_name[indexnumber]
    # for getting the lists, always remember that the index starts from 0 instead of 1. So it goes 0, 1, 2, etc.
# if you try to access an index that isnt present in the list, python will return an error

# you can add items to a list using .append(), this adds the value to the list
# .pop() removes the last item in the list
    # if you specify the index number the the brackets, it removes the value at that index
        # for example, list_name.pop(1) removes the 2nd item in the list
# to check if there is an item in the list do: value in list_name, this will return a true or false value

mylist = [1, 'dog', 1203, '#', 'washington', 'bugatti']
print(mylist)
print(len(mylist))
print("3rd Value In List:", mylist[2])

print("\n")

mylist.append("pagani")
print(mylist)
mylist.pop(4)
print(mylist)
print('washington' in mylist)
print(1203 in mylist)