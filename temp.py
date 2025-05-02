# -*- coding: utf-8 -*-
s = input("請輸入攝氏溫度:")
if s.count('.') > 1:
    print('只能有一個小數點')
# 修改第8行以正確判斷數字格式並允許前後空白
elif s.strip().replace('.', '', 1).replace('-', '', 1).isdigit():
    if s[0] == '-' or s[0].isdigit() or s[0] == ' ' or s[-1] == ' ':
        temp = float(s.strip())  # 去除前後空白，避免轉換錯誤
        print(f'攝氏{temp}度等於華氏{(temp * 9 / 5) + 32:+5.1f}度')
        print(f'華氏{temp}度等於攝氏{(temp - 32) * 5 / 9:+5.1f}度')
    else:
        print("只能以數字或負號開頭")
else:
    print("輸入的溫度無法轉換!")



