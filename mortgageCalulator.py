def calculate_mortgage_payments():
    calculate = True
    while calculate:
        interest_rate = float(input("Enter the interest rate: "))
        loan_amount = float(input("Enter the loan amount: "))
        loan_term = int(input("Enter the loan term in years: "))
        monthly_payment = loan_amount * (interest_rate / 1200) / (1 - (1 + interest_rate / 1200) ** (-loan_term * 12))
        format_monthly_payment = "{:.2f}".format(monthly_payment)
        format_total_payment = "{:.2f}".format(monthly_payment * loan_term * 12)
        print(f'Your monthly payment is £{format_monthly_payment}')
        print(f'Your total payment is £{format_total_payment}')
        return_dict = {
            'interest_rate': interest_rate,
            'loan_amount': loan_amount,
            'loan_term': loan_term,
            'monthly_payment': monthly_payment,
            'format_monthly_payment': format_monthly_payment,
            'format_total_payment': format_total_payment
        }
        calculate = input("Would you like to calculate another mortgage? (y/n): ") == 'y'
    return return_dict

calculate_mortgage_payments()
