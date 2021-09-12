def get_name_initial(name, uppercase = False):
    if uppercase:
        initial = name[0: 1].upper()
    else:
        initial = name[0: 1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_name_initial(uppercase = True, name = first_name)

print(f'Your initial is: {first_name_initial}')