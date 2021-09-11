state = 'Maharastra'
country = 'India'
if country.lower() == 'india':
    if state == 'Maharastra':
        tax = 0.15
    elif state == 'Madhya Pradesh':
        tax = 0.10
    else:
        tax = 0.14
else:
    tax = 0.0
print(f'Your tax is {tax}')