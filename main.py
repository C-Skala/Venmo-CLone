from time import sleep

user_one = {
'Full_name': 'Geralt Riverierre',
'username': 'witcher',
'password': 'yennifer',
'account_balance': '10000',
'connected_banks': 'yes',
'Banks':[
    #('Vivaldi Bank', {'balance': 5000}),
    #('Celadon Bank', {'balance': 5000}),
    ('Vivaldi Bank',  5000),
    ('Celadon Bank', 5000),
],
}

user_two = {
'Full_name': 'ash ketchum',
'username': 'pokeMAN',
'password': 'misty',
'account_balance': '8000',
'connected_banks': 'yes',
'Banks':[
    #('Vivaldi Bank', {'balance': 4000}),
    #('Celadon Bank', {'balance': 4000}),
    ('Vivaldi Bank', 4000),
    ('Celadon Bank', 4000),
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


user_check()
