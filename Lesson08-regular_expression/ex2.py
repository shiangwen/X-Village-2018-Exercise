'''
請利用 re 模組，寫一個簡單的使用者驗證系統，使用者提供帳號，密碼，程式判段是否為合法的帳號密碼。

帳號格式：

總長度為 3
且第一個英文字母為大寫
其餘為小寫
密碼格式:

總長度為 9
前 3 個字為英文小寫
後六個數字為數字 0-9
但第一個數字必須為 0
'''
import re

username=input("Please input username:")

username_pattern=r'[A-Z][a-z][a-z]'
password_pattern=r'[a-z][a-z][a-z]0[0-9][0-9][0-9][0-9][0-9]'

username_pattern_length=r'...'
password_pattern_length=r'.........'

result1 = re.search(username_pattern,username)
result1_2 = re.search(username_pattern_length,username)



if result1 is not None :
    pass
elif result1_2 is not None :
    print("Username format error!","your username is:",username)
else:
    print("Username legnth error!","your username is:",username)

password=input("Please input password:")
result2 = re.search(password_pattern,password)
result2_2 = re.search(password_pattern_length,password)

if result2 is not None :
    print('welcome',username)
elif result2_2 is not None :
    print("Password format error!","your password is:",password)
else:
    print("Password legnth error!","your password is:",password)

