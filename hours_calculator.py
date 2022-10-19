import datetime
import math
def hours_input():
    recorded_hours = []
    add_another = True
    previous_date = False
    previous_hours = False
    previous_rate = False
    while add_another:
        date_entry = True
        hours_entry = False
        rate_entry = False
        while date_entry:
            try:
                date = input("Enter the date (dd/mm/yyyy): ")
                if date == '' and previous_date:
                    date = previous_date
                else:
                    date = datetime.datetime.strptime(date, '%d/%m/%Y')
            except:
                print("Invalid date")
            else:
                date_entry = False
                hours_entry = True
                previous_date = date
        while hours_entry:
            try:
                hours = input("Enter the hours(hh:mm): ")
                if hours == '' and previous_hours:
                    hours = previous_hours
                else:
                    if ':' in hours:
                        minute = int(hours.split(':')[1])
                        hour = int(hours.split(':')[0])
                        total_minutes = (hour * 60) + minute
                    else:
                        total_minutes = int(hours) * 60
            except:
                print("Invalid hours")
            else:
                hours_entry = False
                rate_entry = True
                previous_hours = hours
        while rate_entry:
            try:
                rate = input("Enter the rate: ")
                if rate == '' and previous_rate:
                    rate = previous_rate
                else:
                    pph = (float(rate)*100)
                    ppm = pph / 60
            except:
                print("Invalid rate")
            else:
                rate_entry = False
                previous_rate = rate
                recorded_hours.append({
                    'date': date,
                    'minutes': total_minutes,
                    'pence_earned': total_minutes * ppm
                    })
                add_another = input("Would you like to add another? (y/n): ") != 'n'
    return recorded_hours

def pence_to_pounds_string(pence):
    return (f'£{pence/100:.2f}')

def minutes_to_hours_string(minutes):
    return f'{math.floor(minutes/60)}:{str(minutes % 60) if minutes % 60 > 9 else "0" + str(minutes % 60)}'

def date_to_string(date):
    return date.strftime("%d/%m/%Y")

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
            print(f'On {date_to_string(entry["date"])}, you worked {minutes_to_hours_string(entry["minutes"])} hours, earning {pence_to_pounds_string(entry["pence_earned"])}')
    print(f'You have worked {minutes_to_hours_string(total_minutes)} hours, earning {pence_to_pounds_string(total_pay)} in total')
    if input("Would you like to save this breakdown? (y/n): ") == 'y':
        with open('hours_export.txt', 'a') as file:
            file.write(f'New entry saved on {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
            file.write('\n')
            for entry in recorded_hours:
                file.write(f'On {date_to_string(entry["date"])}, you worked {minutes_to_hours_string(entry["minutes"])} hours, earning {pence_to_pounds_string(entry["pence_earned"])}')
                file.write('\n')
            file.write(f'You have worked {minutes_to_hours_string(total_minutes)} hours, earning {pence_to_pounds_string(total_pay)} in total')
            file.write('\n')
    return total_minutes, total_pay

hours_calculator()
