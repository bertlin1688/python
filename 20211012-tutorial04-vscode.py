#20211012
import os
def tutorialtitle(tutorial):
    print("-"*60)
    print(tutorial)
    print("-"*60)

os.system("clear")
#關係運算子
tutorialtitle("關係運算子")
print("list")
students=["AA","Bert","chen","Wang","TT"]
print("Bert" in students)
print("BB" in students)

print("-"*60)
print("dict")
student2={
    "Bert":99,
    "LL":24,
    "CK":89,
}

print("Leo" in students)
print("Bert"in students)

print("-"*60)
print("str")
message3="This is a book."
print("is" in message3)
print("abc" in message3)
print("oo" in message3)

#小試身手2-1
tutorialtitle("小試身手2-1")
#a
names=["Jeff","Leo","Keven","Lisa","Matty"]
#b
scores=[97,93,68,85,100]
#c
print("嗨嗨,我是{}成績為{}".format(names[2],scores[2]))
#d
print("該梯次平均為:{}".format(sum(scores)/len(scores)))
#e
scores[3]=72
print("修改{}號同學成績為{}".format(4,scores[3]))

#f
print("該梯次平均為:{}".format(sum(scores)/len(scores)))

message4={
    "Jeff":97,
    "Leo":93,
    "Keven":68,
    "Lisa":85,
    "Matty":100,
}

#小試身手2-2
tutorialtitle("小試身手2-2")
#a
data2={
    "name":"Jeff",
    "height":170,
    "weight":65,
    "age":26,
    "class":"A-",
    "interest":["喝酒,爬山,寫程式"]
}
print(data2)
#b
print("我是{name},階級為{class1}".format(name=data2["name"],class1=data2["class"]))
#c
data2["height"]=180
print("修改{name} 的身高為 {new_height}".format(name=data2["name"],new_height=(data2["height"])))

#d
print(data2["interest"])
data2["interest"].append("彈吉他")
print(data2["interest"])


#dist in list 
tutorialtitle("dist in list")
data3=[
    {"name":"Jeff","no":1,"math":100,"eng":87},
    {"name":"Leo","no":2,"math":97,"eng":89},
    {"name":"Keven","no":3,"math":87,"eng":88},
    {"name":"Jenny","no":4,"math":82,"eng":95},
    {"name":"Holy","no":5,"math":91,"eng":98},
]

print("-"*60)
no1=data3[0]["no"]
name1=data3[0]["name"]
math1=data3[0]["math"]
eng1=data3[0]["eng"]
print("No: {} , Name:{} , Math: {} , Eng: {}".format(no1,name1,math1,eng1))

print("-"*60)
no2=data3[1]["no"]
name2=data3[1]["name"]
math2=data3[1]["math"]
eng2=data3[1]["eng"]
print("No: {} , Name:{} , Math: {} , Eng: {}".format(no2,name2,math2,eng2))

#迴圈Loop
tutorialtitle("迴圈Loop")
for element in data3:
    no=element["no"]
    name=element["name"]
    math=element["math"]
    eng=element["eng"]
    print("No: {} , Name:{} , Math: {} , Eng: {}".format(no,name,math,eng))

print("-"*60)
#ragne(1,10) -->產生1~10的數字,為[1,2,3,4,5,6,7,8,9,]
for i in range(1,10):
    print(i)
    a=i*i
    print("number: {}".format(a))

###list
#迭代：一個接著一個依序操作
# "Jeff"放入name變數裡--> "Bert"放入到變數裡--> "Keven"放入到變數裡-->David"放入到變數裡
for name in ["Jeff","Bert","Keven","David"]:
    print("您好,我是:{}".format(name))

for i in range(3,7):
    print("嗨嗨",i)
print("-"*60)
for i in [3,4,5,6]:
    print("嗨嗨",i)

print("-"*60)
dict5={"name":"Jeff","age":18,"message":"你好"}

for key in dict5:
    print(key)
    print(dict5[key])

##Str
print("-"*60)
message5="嗨嗨,最近好累~~"
for w in message5:
    print(w)

## dict in list:
print("-"*60)
data6=[
    {"name":"Bert","age":18},
    {"name":"David","age":20},
    {"name":"Jeff","age":38},    
]

for ty in data6:
    print(ty["name"],ty["age"])


#小試身手3-1
#1+2+3+.....+100 總和
tutorialtitle("小試身手3-1,1+2+3+.....+100 總和")
total=0
for i in range(1,11):
    total=total+i
    print("i = ",i,"目前總和:",total)


#小試身手3-1
#產生圖形,*遞減
# ******
# *****
# ****
# ***
# **
# *
tutorialtitle("小試身手3-1,*列印")

print("-"*60)
for i in range(6,0,-1):
    #print(i)
    print(i,"*"*i)


print("-"*60)
x=7
for i in range(1,7):
    #print(i)
    y=x-i
    print("*"*y)

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
    count=count-1

#小試身手3-2,大樂透 01~49 可重複地抽6號碼
tutorialtitle("小試身手3-2,大樂透 01~49 可重複地抽6號碼")
import random
for i in range(6):
    i=i+1
    print("number{} is:{}".format(i,random.randint(1,50)))
   