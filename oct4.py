import re
import datetime
import random
def bank_account():
    print('Thankyou for visiting banco Leasly')
while True:
    name=input("Don't use a multiple username.\nKindly enter a username:  ").strip()
    if not name.isalpha():
        print('Try again')
    elif len(name)<4:
        print('Username too short,try again !')
    elif len(name)>9:
        print('Username cannot be that long: ')
    else:
        break
import datetime
while True:
    try:
        birth_date=input('Kindly enter your date of birth in the format DD/MM/YY:')
        formated_date=datetime.datetime.strptime(birth_date,'%d/%m/%Y')
        age_now=datetime.datetime.today()
        eligibility=(age_now-formated_date).days/365.2425
        age_limit=int(eligibility)
        if age_limit>17:
            print('You have to be at most 17 years to have an account with us.')
        else:
            break
    except:
        print('Try again')
    else:
        print('Try again.')
    finally:
        print('')
while True:
    pin=input('Enter number of your choice.\nMost preffered is numbers in the range of (100-9999): ')
    if not pin.isdigit():
        print('Kindly try again as instructed ')
    elif len(pin[:3])!=3:
        print('Check on the length')
    else:
        break
otp=int(random.randrange(-9000,9000))
secret_pin=int(pin)-otp
print('Your one time password is ',abs(secret_pin))
print('    Choose one from the two ')
print('a','To withdraw')
print('b','To deposit')
balance=int(500)
while True:
    choice=input('Enter between the two options: ')
    if choice=='a':
        withdrawal=input('Enter an amount to withdraw: ')
        if not withdrawal.isdigit():
            print('Only digits are allowed.')
        elif int (withdrawal)>=balance:
            print('You cannot complete the transaction.')
        else:
            print('You have withdrawn',withdrawal)
            print('Your balance is',(balance-int(withdrawal)))
            break
    elif choice=='b':
        deposit=input('Enter an amount to deposit:')
        if not deposit.isdigit():
            print('Only numbers are allowed:')
        else:
            print('You have deposited',deposit)
            print('Your new balance is',(balance+int(deposit)))
            break
    else:
        print('Try again')
bank_account()
bye=input('Enter any key to quit: ')
quit()





