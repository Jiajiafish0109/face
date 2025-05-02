#讓電腦隨機產出一個介於1~100的整數後，讓使用者猜該數字。當猜的數字大於正確數字時，程式須回覆”太大了”；
#當猜的數字小於正確數字時，程式須回覆”太小了”；直到猜對正確數字時，程式回覆”恭喜，猜對了”。先不須對使用者所輸入的資料作檢查
#提醒：要產生亂數可以先匯入random模組，在經由呼叫random.randint(1, 100)來隨機產出一個介於1~100的整數

import random

def guess_number_game():
    target = random.randint(1, 100)  
    while True:
        guess = int(input("請輸入你的猜測(1~100): "))
        if guess > target:
            print("太大了")
        elif guess < target:
            print("太小了")
        else:
            print("恭喜，猜對了！")
            break

# 執行遊戲
guess_number_game()
