taxes = 0


def tax(income):
    if income <= 300_000:
        taxes = 0
        print('Income is 300 000 or less')

    elif 300000 < income <= 700_000:
        taxes = (income - 300_000) * 0.2
        print('Income is between 300 000 and 700 000')

    else:
        taxes = 80000 + 0.35 * (income - 700_000)
        print('Income is more than 700 000')

    return taxes


taxes = tax(300_001)
print(f'Tax: {taxes}')

import numpy as np

#create 13 candidate income levelse for testing
incomes = np.linspace(0, 1_200_000, 13)
print(f"Incomes: {incomes}")

taxes_loop = []

for income incomes:
    # Compute taxes for current income level
    taxes = tax(income)
    # Append to list
    taxes_loop.append(taxes)
# income after tax
    net_income = income - taxes

    print(f"Gross income: {income:10.0f}, Net income: {net_income:10.0f}")