values = {
    'tax_free_allowance': 12500,
    'basic_rate_allowance': 50270,
    'higher_rate_allowance': 150000,
    'basic_rate': 20,
    'higher_rate': 40,
    'additional_rate': 45,
    'net': 0,
    'income': 0
}

def print_values():
    print(f'Personal allowance:        £0 to £{values["tax_free_allowance"]} 0%')
    print(f'Basic rate allowance:      £{values["tax_free_allowance"] +1} to £{values["basic_rate_allowance"]} {values["basic_rate"]}%')
    print(f'Higher rate allowance:     £{values["basic_rate_allowance"] +1} to £{values["higher_rate_allowance"]} {values["higher_rate"]}%')
    print(f'Additional rate allowance: £{values["higher_rate_allowance"] + 1} and above {values["additional_rate"]}%')

def to_percentage(value):
    return (100-value) / 100

def calculate_net_income():
    print("Default values:")
    print_values()
    change_rate = input("Would you like to change the default values? (y/n): ")
    while change_rate == 'y':
        values["tax_free_allowance"] = int(input(f'Enter your personal allowance: (currently set to £{values["tax_free_allowance"]}) '))
        values["basic_rate_allowance"] = int(input(f'Enter your basic rate allowance: (currently set to £{values["basic_rate_allowance"]} '))
        values["higher_rate_allowance"] = int(input(f'Enter your higher rate allowance: (currently set to £{values["higher_rate_allowance"]} '))
        values["basic_rate"] = int(input(f'Enter your basic rate: (currently {values["basic_rate"]}% '))
        values["higher_rate"] = int(input(f'Enter your higher rate: (currently {values["higher_rate"]}% '))
        values["additional_rate"] = int(input(f'Enter your additional rate: (currently {values["additional_rate"]}% '))
        print("New values:")
        print_values()
        change_rate = input("Would you like to change these values? (y/n): ")
    values["income"] = int(input("Enter the annual income: £"))
    
    if values["income"] <= values["tax_free_allowance"]:
        values["net"] = values["income"]
    elif values["income"] > values["tax_free_allowance"] and values["income"] <= values["basic_rate_allowance"]:
        values["net"] = values["tax_free_allowance"] + ((values["income"] - values["tax_free_allowance"]) * to_percentage(values["basic_rate"]))
    elif values["income"] > values["basic_rate_allowance"] and values["income"] <= values["higher_rate_allowance"]:
        values["net"] = values["tax_free_allowance"] + ((values["basic_rate_allowance"] - values["tax_free_allowance"]) * to_percentage(values["basic_rate"])) + ((values["income"] - values["basic_rate_allowance"] - values["tax_free_allowance"]) * to_percentage(values["higher_rate"]))
    elif values["income"] > values["higher_rate_allowance"]:
        values["net"] = values["tax_free_allowance"] + ((values["basic_rate_allowance"] - values["tax_free_allowance"]) * to_percentage(values["basic_rate"])) + ((values["higher_rate_allowance"] - values["basic_rate_allowance"] - values["tax_free_allowance"]) * to_percentage(values["higher_rate"])) + ((values["income"] - values["higher_rate_allowance"]  - values["basic_rate_allowance"] - values["tax_free_allowance"]) * to_percentage(values["additional_rate"]))

    print(f'Your net incomeis £{"{:.2f}".format(values["net"])}')
    print(f'Your monthly income is £{"{:.2f}".format(values["net"] / 12)}')
    print(f'Your tax is £{"{:.2f}".format(values["income"] - values["net"])}')
    print(f'Your tax rate is {"{:.2f}".format(((values["income"] - values["net"])/values["income"])*100)}%')
    return values
# calculate_net_income()