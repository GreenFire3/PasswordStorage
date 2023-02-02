import random, requests, os, re
from cryptography.fernet import Fernet

def delete_all():
    delete = input('Вы действительно хотите удалить все данные? + или -')
    if delete == '+':
        f = open("users.txt", "r+")
        f.seek(0)
        f.truncate()
        menu()
    if delete == '-':
        os.system('cls')
        menu()

def create_pass():
    simv = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(1):
        pass_ = ''
        for ii in range(25):
            pass_ = pass_ + random.choice(simv)
        print(pass_)
        os.system('cls')
        menu()

def create_text():
    logn = input('Введите логин: ')
    nard = input('Введите пароль: ')
    fileW = open('users.txt', 'a', encoding='utf-8')
    key = b'p9TVboilU2dg6oOGjBYO8-b_5awnWpwAwG5cAYRInhM='
    fernet = Fernet(key)
    encText = fernet.encrypt(nard.encode())
    encText = encText.decode()
    fileW.write(logn + ':' +encText + '\n')
    fileW.close()
    os.system('cls')
    menu()

def read_text_list():
    with open('users.txt', encoding='utf-8') as fileR:
        line = fileR.readline()
        while line:
            text = line
            text_without = re.sub(r'\w+\:', '', text)
            line321 = str.encode(text_without)
            key = b'p9TVboilU2dg6oOGjBYO8-b_5awnWpwAwG5cAYRInhM='
            fernet = Fernet(key)
            decMessage = fernet.decrypt(line321).decode()
            head, sep, tail = line.partition(':')
            print(head+':' + decMessage)
            line = fileR.readline()
    fileR.close()
    os.system('cls')
    menu()

def get_password():
    login = input('Введите логин ')
    word = login
    fileR = open('users.txt', encoding='utf-8').readlines()
    for i in fileR:
        if word in i:

            text_without = re.sub(r'\w+\:', '', i)
            line321 = str.encode(text_without)
            key = b'p9TVboilU2dg6oOGjBYO8-b_5awnWpwAwG5cAYRInhM='
            fernet = Fernet(key)
            decMessage = fernet.decrypt(line321).decode()
            head, sep, tail = i.partition(':')
            print(head+':' + decMessage)
    os.system('cls')
    menu()

def menu():
    os.system('cls')
    print('''
1 - Сгенерировать пароль
2 - Создать новую запись
3 - Просчесть список учетных записей
4 - Получить пароль от записи
5 - Удалить все записи
''')
    user = input('')
    if user == str(1):
        os.system('cls')
        print('Новый сгенерированый пароль:')
        create_pass()
    elif user == str(2):
        os.system('cls')
        create_text()
    elif user == str(3):
        os.system('cls')
        read_text_list()
    elif user == str(4):
        os.system('cls')
        get_password()
    elif user == str(5):
        os.system('cls')
        delete_all()
    else:
        menu()

def start():
    pass_ = random.randint(1111, 9999)
    code = pass_

    r=requests.get('https://api.telegram.org/bot6049003105:AAGeU88MQ5No7SM65esvQXk5nembE9wjUpY/sendmessage?chat_id=748935455&text=' + str(pass_))

    code_user = input('Введите код: ')

    if int(code_user) == int(code):
        os.system('cls')
        print('Все ок')
        menu()

    else:
        print('Код неверный')
        start()
start()