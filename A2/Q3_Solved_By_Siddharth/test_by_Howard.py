global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# TypeError: process_numbers() got an unexpected keyword argument 'numbers'
def process_numbers(numbers): # Added a variable here to address the TypeError
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]
    while local_variable > 0:
        if local_variable % 2 == 0:
            numbers.remove(local_variable)
        local_variable -= 1
    return numbers

my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set)

# TypeError: modify_dict() takes 0 positional arguments but 1 was given
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict() # Removed the parameter to address the TypeError

def upbate_global():
    global global_variable
    global_variable += 10

for i in range(5):
    print(i)
    i += 1

# KeyError: 'ke14'
if my_set is not None and my_dict['key4'] == 10: # CHanged `ke14` to `key4` to address KeyError
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)
print(my_dict)
print(my_set)