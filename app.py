from mortgage_calculator import *
from tax_calculator import *
from extra_outgoings import *

if __name__ == "__main__":
    calculate_mortgage = True
    calculate_tax = True
    calculate_extra_outgoings = True
    while calculate_mortgage == True:
        mortgage = calculate_mortgage_payments()
        # breakpoint()
        calculate_mortgage = input("Would you like to calculate another mortgage? (y/n): ") == 'y'
    while calculate_tax == True:
        tax = calculate_net_income()
        # breakpoint()
        calculate_tax = input("Would you like to calculate another tax? (y/n): ") == 'y'
    # print(tax)
    # print(mortgage)
    while calculate_extra_outgoings == True:
        extra_outgoings = extra_outgoings_calculator()
        # breakpoint()
        calculate_extra_outgoings = input("Would you like to calculate another extra outgoings? (y/n): ") == 'y'
    print('')
    print("***   Spending Summary:   ***")
    print(f'Monthly net income: £{"{:.2f}".format(tax["net"] / 12)}')
    print(f'Monthly mortgage payments: £{"{:.2f}".format(mortgage["monthly_payment"])}')
    for key, value in extra_outgoings.items():
        print(f'{key}: £{value}')
    print(f'Monthly savings: £{"{:.2f}".format((tax["net"] / 12) - mortgage["monthly_payment"] - extra_outgoings["Monthly extra outgoings"])}')