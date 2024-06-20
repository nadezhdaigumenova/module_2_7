def print_params(a=1, b='str', c=True):
    print(a, b, c)

print_params()
print_params(2)
print_params(5,8)
print_params(5, 8, 3)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [9, 'dog', False]
values_dict = {'a': 4, 'b': 'urban', 'c': 2}

print_params(*values_list)
print_params(**values_dict)

values_list2 = [54.32, 'str']
print_params(*values_list2, 42)
