import datetime
def hours_input():
    recorded_hours = []
    add_another = True
    while add_another:
        date_entry = True
        hours_entry = False
        rate_entry = False
        while date_entry:
            try:
                date = datetime.datetime.strptime(input("Enter the date (dd/mm/yyyy): "), '%d/%m/%Y')
            except:
                print("Invalid date")
            else:
                date_entry = False
                hours_entry = True
        while hours_entry:
            try:
                hours = input("Enter the hours(hh:mm): ")
                minute = int(hours.split(':')[1])
                hour = int(hours.split(':')[0])
                total_minutes = (hour * 60) + minute
            except:
                print("Invalid hours")
            else:
                hours_entry = False
                rate_entry = True
        while rate_entry:
            try:
                rate = input("Enter the rate: ")
                pph = (float(rate)*100)
                ppm = pph / 60
            except:
                print("Invalid rate")
            else:
                rate_entry = False
                recorded_hours.append({
                    'date': date,
                    'minutes': total_minutes,
                    'pence_earned': total_minutes * ppm
                    })
                add_another = input("Would you like to add another? (y/n): ") == 'y'
    return recorded_hours


def hours_calculator():
    recorded_hours = hours_input()
    total_minutes = 0
    total_pay = 0
    for entry in recorded_hours:
        total_pay += entry['pence_earned']
        total_minutes += entry['minutes']
    verbose = input("Would you like to see a verbose breakdown? (y/n): ") == 'y'
    if verbose:
        for entry in recorded_hours:
            print(f'On {entry["date"]}, you worked {entry["minutes"]} minutes, earning £{str(round(entry["pence_earned"]/100, 2))}')
    print(f'You have worked {total_minutes} minutes, earning £{str(round(total_pay/100, 2))} in total')
    return total_minutes, total_pay

hours_calculator()
