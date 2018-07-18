


date = input('輸入日期:')
event = input('輸入事件:')
description = input('輸入心得:')

f = open('note.txt', 'w')
f.write("輸入日期"+date+"輸入事件"+event+"輸入心得"+description) #輸入的直接是字串
