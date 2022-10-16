def extra_outgoings_calculator():
    extra_outgoings = {
        "Monthly extra outgoings": 0,
    }
    for _ in range(int(input("How many extra outgoings do you want to calculate? "))):
        name = input("Enter the name of the extra outgoings: ")
        amount = int(input("Enter the amount of the extra outgoings: £"))
        print(f'{name}: £{amount}')
        extra_outgoings.update({name: amount})
    print('Extra Outgoings Summary:')
    for key, value in extra_outgoings.items():
        print(f'{key}: £{value}')
        extra_outgoings["Monthly extra outgoings"] += value
    return extra_outgoings

