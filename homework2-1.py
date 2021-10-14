import os
os.system("clear")
#回家試身手#2-1
print("-"*60)
print("Homework 2-1")
print("-"*60)
print("""No1:試撰寫一程式 , 列印出以下圖形
         ******
         *****
         ****
         ***
         **
         *
         **
         ***
         ****
         *****
         ******
""")

for i in range(6,1,-1):
    print("*"*i)
for i in range(1,6):
    print("*"*i)


#回家試身手#2-2
print("-"*60)
print("Homework 2-1")
print("-"*60)
print("""有一變數 data , 其值為
     [ “a”, “b”, “c”, “c”, “c”, “a”, “d”, “b”, “b”, “a”, “c”]
     試統計各字母出現次數 , 並以 dict  型式表達
     hint :   
     。最終答案範例格式如下
            {  a”: 3 , “b”: 5 , “c”:  3  , ... }

     。當 data 新增元素時 ( ex: 新增字母 “j”)
         dict 必須能自動新增統計結果 -> “j”:  1  
         依此類推""")
