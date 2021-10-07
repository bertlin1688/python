"""---
#20211005
a=50
if a<50:
    print("A=",a)
else:
    print("A=",a)


x=100
if x>100:
    print("X <100")
elif x==100:
    print("X=100")
else:
    print("No")

###########################################
# Input
today=input("請輸入日期:")
print("今天日期:",today)

age=input("請輸入您的年紀:")
print("你的年紀是:",age)
###########################################

#幫Age+3歲顯示
#新的Age轉換成數字
age=int(age)
age=age+3
print("你的年紀+3是:",age)

#type
name="Bert"
print(type(name))
print(type(123))
print(type("test"))

#資料型別轉換
age2=input("請輸入你的年紀:")
print("我是輸入後的資料",type(age2))
age2=int(age2)
print("我是轉換成數字",type(age2))

# 1.選取程式碼
# 2.打開註解Ｍac command+/ , Windows ctrl+/

#資料型別1
#int整數
print("-"*60)
a=12
b=30
print(a+b)
print(a*b)
print(a/b)

#float
print("-"*60)
c=36.145
d=59.4096
print(c*d)
print(c/d)

#complex
print("-"*60)
e=1+2j
f=3-4j
print(e+f)
print(e*f/2)

#bool
print("-"*60)
g=True
h=False
print(g and h)
print(g or h)

#空型別
print("-"*60)
i=None
print(type(i))
print(i)

print(type(a))
print(type(c))
print(type(e))
print(type(g))
print(type(i))

#資料型別2
#字串型別
name1="Bert"
name2='Lin'
print(name1,name2)
print(name1+""+name2)
print(name1, "and",name2)
message="Good evening~~~~"
print(name1,"says",message)

#index取直
print(name1[1]) #-->e
print(name2[2]) #--->n
print(name2[-1]) #--->n

#字串合併
group1=name1+name2
group2=name1+ "____"+name2
group3=name1+("-"*5)+name2+"hihihi"
print(group1)
print(group2)
print(group3)

name3="Bert"
message2="您好!!"
#透過print將三個元素顯示出來
print(name3,",",message2) 

#利用+合併三個元素變成一個大字串
bigmessage=name3+" , "+message2
print(bigmessage)

#字串常用功能
'''.format : 字符串模板 , 使用變數合成字串
[:]	    :  利用字串 index 取值
.split :  字串分割
.join  :  字串合併
.strip :  頭尾空白去除
.startswith :   是否以 … 為開頭
.replace :   以 … 替換子字串
.find :  找尋子字串的第一個 index 值
'''
"""
#字串常用功能
#.format , 字符串模板
name1="Bert"
message1="你好!!!"
name2="Lin"
message2="天氣真好"
print("{} says: {}".format(name1,message1))
print("{} says: {}".format(name2,message2))
print("{} says: {}".format("Bert","天氣真好"))

big_message2="{},{}"
print(big_message2.format("Alex","今天天氣如何?"))

#[]字串範圍取值
sentence1="五倍卷要發行了,準備領錢!!!"
print(sentence1[2])
print(sentence1[10])
print(sentence1[0:6]) #部分範圍取值
print(sentence1[:6])  #從頭開始取到第6個字
print(sentence1[9:])  #從第9個字取到底

#.split切割
print("split"+ "-"*60)
sentence2="五倍卷要發行了;快點預約;但是系統GG;等啊等!!"
print(sentence2.split(";")) #切割成四個字串 ['五倍卷要發行了', '快點預約', '但是系統GG', '等啊等!!']
print(sentence2.split("了"))

sentence3="a-b-c-ddd-e-f-g"
print(sentence3.split("-"))

#.join
print("join"+ "-"*60)
data1=["a","b","c","d"]     #--->list陣列
print("-".join(data1))
print(" ** ".join(data1))

data2=sentence2.split(";")
message3=",".join(data2)
print("舊:",sentence2)
print("新:",message3)

#.strip 去除首尾空白
print("strip"+ "-"*60)
message4="   你好   ,  今天天氣如何?  "
print("原本訊息:",message4)
print("新訊息:",message4.strip())

#.replace
print("replace" + "-"*60)
print(sentence2.replace("五","三"))
print(sentence2.replace("五","三").replace("GG","掛掉"))
print(sentence2.replace("五倍卷","___").replace("預約","___"))
print(sentence2.replace("!",""))

#算數運算子
print("-"*60)
print("運算子")
print("-"*60)
#專門給數值類 int / float / complex
a=100
b=125

print(a+b)
print(a*b)
print(a/b)

#指數 2的10次方
print("指數")
print(2**10)
print(6**3)

#整數除
print("除整數")
print(1944//49)

#取餘數
print("取餘數")
print(108%100)
print(27%4)
print(20%4)

#專門給str
message5="你好"+"!!"+"今天天氣很好"
print(message5)

message6= "-QQ-"*20
print(message6)

name5="Bert"
name6="Lin"

#單純使用print
print(name5,"和",name6 )

message7="{} 和 {}".format(name5,name6)
print(message7)
message8="和".join([name5,name6])
print(message8)

#關係運算子 > , < , == , !=
print("-"*60)
print("關係運算子")
print("-"*60)
a=30
b=80
c=90
print(a>b)
print(a<b)
print(a*3==c)
print(a*3!=c)

name8="alex"
print(name8=="Test")
print(name8!="Test")

#邏輯運算子 and , or ,not
print("-"*60)
print("邏輯運算子")
print("-"*60)
print(a>10 or b <60)
print(a>10 and b <60)
print(a%2 ==0)
print(a%2 ==0 or b%2==0)
