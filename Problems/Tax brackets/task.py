income = int(input())
tax = 0
percent = 0
if income <= 15527:
    print(f'The tax for {income} is {percent}%. That is {tax} dollars!')
elif (income <= 42707) and (income > 15527):
    percent = 15
    tax = round(income * (percent / 100))
    print(f'The tax for {income} is {percent}%. That is {tax} dollars!')
elif (income <= 132406) and (income > 42707):
    percent = 25
    tax = round(income * (percent / 100))
    print(f'The tax for {income} is {percent}%. That is {tax} dollars!')
elif income > 132406:
    percent = 28
    tax = round(income * (percent / 100))
    print(f'The tax for {income} is {percent}%. That is {tax} dollars!')
