#20211014
import os
def tutorialtitle(tutorial):
    print("-"*60)
    print(tutorial)
    print("-"*60)
os.system("clear")

#小試身手3-1
#1+2+3+.....+100 總和
tutorialtitle("小試身手3-1,1+2+3+.....+100 總和")
total=0
for i in range(1,101):
    total=total+i
    print("i = ",i,"目前總和:",total)



#小試身手3-1
# 有一變數 name=“Jack!” , 試撰寫一程式 , 列印出下列訊息
#         JJJJJ
#         aaaa
#         ccc
#         kk
#         !
tutorialtitle("小試身手3-1,有一變數 name=“Jack!” , 試撰寫一程式 , 列印出下列訊息")
name="Jack!"
count=len(name)
print("字串總長度:{}".format(count))
for i in name:
    print(i*count)
    #count=count-1  # ==> count -=1
    count -=1
#簡化寫法
# +=    每次+1
# -=    每次-1

a=12
a+=8
print(a)

msg="嗨嗨,"
msg=msg+"我是Jeff~~"
print(msg)

msg+="您好!!"
print(msg)

#亂數
import random
r=random.random() #產生0~1之間的隨機小數
print(r)

r2=random.randint(0,10) #產生1~9的隨機亂數
print(r2)


#小試身手3-2,大樂透 01~49 可重複地抽6號碼
tutorialtitle("小試身手3-2,大樂透 01~49 可重複地抽6號碼")
import random
for i in range(6):
    i=i+1
    print("number{} is:{}".format(i,random.randint(1,50)))

#小試身手3-2,大樂透 01~49 可重複地抽6號碼 -->老師解法
tutorialtitle("小試身手3-2,大樂透 01~49 可重複地抽6號碼 -->老師解法")
data=[]
for i in range(60):
    num=random.randint(1,49)
    if num not in data and len(data)<6:        #這四行判斷如果有重複就附加
        data.append(num)
    if len(data) ==6:               #如果取得6個數值提前結束迴圈 
        break                       #結束迴圈
  
print(data)

#while-loop
tutorialtitle("while-loop")
count=0
while count<5:
    print("第{}次執行".format(count))
    count=count+1

#小試身手3-2,大樂透 01~49 可重複地抽6號碼 -->while解法
tutorialtitle("小試身手3-2,大樂透 01~49 可重複地抽6號碼 -->while解法")
data=[]
while len(data) <6:
    num=random.randint(1,49)
    if num not in data :
        data.append(num)
        #print(data)
print(data)

#小試身手3-1
#1+2+3+.....+100 總和 while寫法
tutorialtitle("小試身手3-1,1+2+3+.....+100 總和while寫法")
i=1
total2=0
while i<=100:
    total2+=i
    i+=1
print("1+100總和:{}".format(total2))

#小試身手3-1 while解法
# 有一變數 name=“Jack!” , 試撰寫一程式 , 列印出下列訊息
#         JJJJJ
#         aaaa
#         ccc
#         kk
#         !
tutorialtitle("小試身手3-1,有一變數 name=“Jack!” , 試撰寫一程式 , 列印出下列訊息-while解法")
i=5
name="Jack!"

while i>0:
    #i=5 -->抓J, index=0
    #i=4 -->抓a, index=1
    #i=3 -->抓c, index=2
    w=name[5-i]
    print(w*i)
    i-=1
print("done")

#小試身手3-2,大樂透 01~49 不重複地抽6號碼 -->while解法
tutorialtitle("小試身手3-2,大樂透 01~49 可重複地抽6號碼 -->while解法")
import random
cnt=0
data2=[]
while len(data2) <5:
    cnt+=1
    num2=random.randint(1,49)
    if num2 not in data2:
        data2.append(num2)
print("總過做了{}次".format(cnt))
print(data2)

#雙重迴圈(曹狀迴圈)
tutorialtitle("雙重迴圈(曹狀迴圈)")
for i in range(10):
    print("{}開始!!".format(i))
    for j in ["a","b","c"]:
        print(i,j)
    print("{}結束!!".format(j))
    print("-"*60)

##9x9乘法表
#顯示
# 1X1=1 
# 1X2=2 
# ......
# 9X9=81
tutorialtitle("9x9乘法表")
x=1
y=1
for i in range(1,10):
    #print(i)
    for y in range(1,10):
        print("{}x{}={}".format(i,y,i*y))
    print("-"*8)

# 進階教學
#sorted-->排序
a=[4,3,8,5,8,10,38,15]
print(sorted(a))
print(sorted(a,reverse=True))
tutorialtitle("進階教學,sorted-->排序")

# 函式 function,也稱為函數
tutorialtitle("函式1")
def calculate(x,y):
    return(x+y,x-y,x*y,x/y)

r1=calculate(34,57)
r2=calculate(64,96)
print(r1)
print(r2)

print("-"*60)
def say_hello(name):
    print("韓式執行 hello")
    print("嗨嗨 , 我是{}".format(name))

say_hello("bert")

tutorialtitle("函式2")
def test_func(name,age,remark="嗨嗨"):
    print(name)
    print("Age : {}".format(age))
    print("Remark : {}".format(remark))
    return "Done."

test_func("Bert",18)
test_func("Bert Lin",20,"強大")

r4=test_func("Bert",18)
r5=test_func("Bert Lin",20,"強大")

print("函式執行結束")
print("R4 is:",r4)
print("R5 is:",r5)

#函式練習
tutorialtitle("未使用函式寫法,太多重複性code")
math=[87,100,81,99,94]
eng=[88,86,79,93,97]
chinese=[84,98,92,99,98]

#Math
print("Math sum : {}".format(sum(math)))
print("Math avg : {}".format(sum(math)/len(math)))
print("Math Max : {}".format(sorted(math,reverse=True)[0]))
#Eng
print("eng sum : {}".format(sum(eng)))
print("eng avg : {}".format(sum(eng)/len(eng)))
print("eng Max : {}".format(sorted(eng,reverse=True)[0]))
#Chinese
print("Chinese sum : {}".format(sum(chinese)))
print("Chinese avg : {}".format(sum(chinese)/len(chinese)))
print("Chinese Max : {}".format(sorted(chinese,reverse=True)[0]))

# tutorialtitle("使用函式寫法,減少重複性code")
tutorialtitle("使用函式寫法,減少重複性code")
def get_scores_info(name,classid):
    #print("-"*60)
    print("{} sum : {}".format(name,sum(classid)))
    print("{} avg : {}".format(name,sum(classid)/len(classid)))
    print("{} Max : {}".format(name,sorted(classid,reverse=True)[0]))
    r_max=sorted(classid,reverse=True)[0]
    print("-"*20)
    return(r_max)
 
get_scores_info("Math",math)   
get_scores_info("Eng",eng)
get_scores_info("Chinese",chinese)
result_max=get_scores_info("Chinese",chinese)
print(result_max)


#function-4
print("-"*60)
def say_hello(name):
    print("嗨嗨,我是:{}".format(name))

def say_hello_with_return(name):
    print("嗨嗨,我是:{}".format(name))
    return "今天是星期四"

teacher="Jeff"
say_hello(teacher)
say_hello_with_return(teacher)

print("*"*60)
a=say_hello_with_return(teacher)
print(a)
print("-"*60)
b=say_hello(teacher)
print(b)