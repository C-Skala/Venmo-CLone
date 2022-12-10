from time import sleep

user_one = {
'Full_name': 'Geralt Riverierre',
'username': 'witcher',
'password': 'yennifer',
'account_balance': 10000,
'connected_banks': 'yes',
'Banks':[
    ('Vivaldi Bank', {'balance': 5000}),
    ('Celadon Bank', {'balance': 5000}),
    #('Vivaldi Bank',  5000),
    #('Celadon Bank', 5000),
],
}

user_two = {
'Full_name': 'ash ketchum',
'username': 'pokeMAN',
'password': 'misty',
'account_balance': 8000,
'connected_banks': 'yes',
'Banks':[
    ('Vivaldi Bank', {'balance': 4000}),
    ('Celadon Bank', {'balance': 4000}),
    #('Vivaldi Bank', 4000),
    #('Celadon Bank', 4000),
],
}

def user_check():
    username_verified = False
    password_verified = False
    
    username_check = input("please enter your username   ")
    print(" ")
    while username_verified == False:
        if username_check == user_one['username']:
            username_verified = True
            #sleep(1)
            password_check = input('please enter your password   ')
            print(" ")
        elif username_verified == False:
            print('no user found by that name (please remember we are CaSe SeNsItIvE)')
            print(" ")
            #sleep(1)
            username_check = input("please enter your username   ")
            print(" ")
    
    while password_verified == False:
        if password_check == user_one['password']:
            password_verified = True
            print(user_one['Full_name'])
            print(" ")
            #sleep(1)
            print(user_one['account_balance'])
            print(" ")
            #sleep(1)
            print(user_one['Banks'][0][0]," : ",user_one['Banks'][0][1])
            print(" ")
            #sleep(1)
            print(user_one['Banks'][1][0]," : " ,user_one['Banks'][1][1])
            print(" ")
        elif password_verified == False:
            print('that answer was bad and you should feel bad')
            print(" ")
            #sleep(1)
            password_check = input('please enter your password   ')
            print(" ")

def balance_txfr():
    give_money = False
    while give_money == False:
        xfer_inq = input('would you like to transfer money to ' + user_two['Full_name']+'?')
        if xfer_inq == "y":
            give_money = True
            txfer_done = False
            while txfer_done == False:
                ammnt_to_txfr = int(input('how much would you like to give? '))
                if ammnt_to_txfr > user_one['account_balance']:
                    print('sorry you dont have that much coin yet')
                    #ammnt_to_txfr = input('how much would you like to give? ')
                elif ammnt_to_txfr <= user_one['account_balance']:
                    user_one['account_balance'] -= ammnt_to_txfr
                    user_two['account_balance'] += ammnt_to_txfr
                    txfer_done = True
        elif xfer_inq == 'n':
            print('ok keep your coin')
            return
        else:
            print('please type y or n')

def balance_txfr_again():
    give_money = False
    while give_money == False:
        xfer_inq = input('do you want to transfer any more money to ' + user_two['Full_name']+'?')
        if xfer_inq == "y":
            give_money = True
            txfer_done = False
            while txfer_done == False:
                ammnt_to_txfr = int(input('how much would you like to give? '))
                if ammnt_to_txfr > user_one['account_balance']:
                    print('sorry you dont have that much coin yet')
                    #ammnt_to_txfr = input('how much would you like to give? ')
                elif ammnt_to_txfr <= user_one['account_balance']:
                    user_one['account_balance'] -= ammnt_to_txfr
                    user_two['account_balance'] += ammnt_to_txfr
                    txfer_done = True
        elif xfer_inq == 'n':
            print('ok keep your coin')
            return
        else:
            print('please type y or n')


user_check()
balance_txfr()
balance_txfr_again()

