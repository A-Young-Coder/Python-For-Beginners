def get_name_initial(name):
    initial = name[0: 1].upper()
    return initial

first_name = input('Your first name: ')
first_name_initial = get_name_initial(name = first_name)
last_name = input('Your last name')
last_name_initial = get_name_initial(name = last_name)

print(f'{first_name_initial}{last_name_initial}')