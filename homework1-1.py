#homework1-1.py
import os
os.system("clear")
#回家試身手#1-1
print("-"*60)
print("Homework 1-1")
print("-"*60)
print("No1:試寫一程式 , 提示使用者輸入長&寬,計算此矩形的面積及周長")
x=input("請輸入長:")
y=input("請輸入寬:")
x=float(x)
y=float(y)
print("總面積為:",x*y)
print("總周長為:",(x*2)+(y*2))

print("-"*60)
print("No2:試寫一程式 ,  將此字串取代成不同的新字串")
text1="this is a book"
text1new=text1.replace("book","lion")
text2new=text1.replace("this","****").replace("is","!!")
text3new=text1.replace("a book","an apple")
print("原本字串:",text1)
print("新字串1:",text1new)
print("新字串2:",text2new)
print("新字串3:",text3new)

print("-"*60)
print("Homework 2-1")
print("-"*60)
print("""No3:
令 a=“Jeff” , b=“Leo” , c=“Jonny” , 並打印出
“Jeff is good , Leo is young , and Jonny is single…”
當 a 換成 “Steve” , c = “Dave” 時, 需打印出
“Steve is good , Leo is young , and Dave is single… """)

a="Steve"
b="Leo"
c="Dave"
if a=="Jeff" or a=="Steve":
    status1="good"
else:
    a="no user" 
    status1="no status"

if b=="Leo":
    status2="young"
else:
    a="no user" 
    status1="no status"
if c=="Johnny" or c=="Dave":
    status3="single"
else:
    a="no user" 
    status1="no status"

print(a,"is",status1,",",b,"is",status2,",",c,"is",status3,"....")

print("-"*60)
print("Homework 2-2")
print("-"*60)
print("""No4
試寫一程式 , 請使用者輸入一數字 , 並按規則顯示下列訊息 :
0 <= n < 30  :  young
30<= n < 60 :  strong 
n >= 60        :  old
n < 0            :  ‘n’ must be larger than 0
""")
number1=input("請輸入一個數值:")
number1=int(number1)
if number1<=0:
    print("數字必須大於0")
elif number1 >=0 and number1 <30:
    print(number1,"is young")
elif number1 >=30 and number1<60:
    print(number1,"is strong")
else:
    print(number1,"is old")
