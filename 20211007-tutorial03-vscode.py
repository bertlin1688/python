#20211007
def tutorialtitle(tutorial):
    print("-"*60)
    print(tutorial)
    print("-"*60)

# #IF判斷式
# tutorialtitle("IF判斷式")
# a=10
# b=20
# if a>b:
#     print("Ａ>B")
#     print("A比較大")
# else:
#     print("B>A")
#     print("B比較大")

# if-elif-else
# x=20
# if x>0:
#     print("X是正數")
# elif x==0:
#     print("X是0")
# else:
#     print("X是負數")

# #如果A是偶數分配到A組,如果是奇數分配到B組
# tutorialtitle("如果A是偶數分配到A組,如果是奇數分配到B組")
# a=20
# print("A is:",a)
# if a%2==0:
#     print(a,"是偶數")
#     print("A組")
# else:
#     print(a, "是奇數")
#     print("B組")

# #請使用者輸入數字存到變數B,如果B是偶數分配到A,基數分配到B組
# tutorialtitle("請使用者輸入數字存到變數B,如果B是偶數分配到A,基數分配到B組")
# b=input("請輸入B:")
# print(type(b))
# print("B is:",b)
# b=int(b)
# print(type(b))
# if b%2==0:
#     print(b,"是偶數")
#     print("A組")
# else:
#     print(b, "是奇數")
#     print("B組")


# #小試身手1-1
# tutorialtitle("小試身手1-1")
# number=input("請輸入數字:")
# number=int(number)
# type_name=""
# if number>=100:
#     print("number is:",number)
#     type_name="丁組"
# elif number <100 and number >=50:
#     print("number is:",number)
#     type_name="丙組"
# elif number <50 and number >=0:
#     print("number is:",number)
#     type_name="乙組"
# else:
#     print("number is:",number)
#     type_name="甲組"
# print("您的組別是:",type_name)

# #小試身手1-2 ,曹狀if-else
# tutorialtitle("小試身手1-2,曹狀if-else")
# age=28
# gender="F"
# if gender=="F":
#     print("您的消費金額是500")
# else:
#     if age>=30:
#         print("你的消費金額是:1000")
#     else:
#         print("你的消費金額是700")


#求總和 &平均,若s不斷增加每次都要改成是太麻煩,可以改用串列
tutorialtitle("求總和 &平均")
s1=50
s2=32
s3=93

scores_sum=s1+s2+s3
scores_avg=scores_sum/3
print("總和:",scores_sum)
print("平均:",scores_avg)

#串列
tutorialtitle("串列") 
scores=[55,19,75,34,65,88,94,100]
print(type(scores))
scores_sum=sum(scores)
scores_avg=sum(scores)/len(scores)
print("個數:",len(scores))
print("總和:",scores_sum)
print("平均:",scores_avg)

data1=[1,2,3,4,5]
print(data1)

data2=["a","b","c","d"]
print(data2)

data3=["你好",123,True]
print(data3)

##list常用方法
#取值與修改數值
#取值-->透過index索引值)
data4=["a","b","c","d","e"]
print(data4[2])
print(data4[4])  #取單一值
print(data4[1:4]) #抓1-3
print(data4[1:]) #從1抓到結尾
print(data4[:3]) #從頭抓到3

#修改值-->透過index
data4[0]="aaa"
data4[4]="kkk"
print(data4)

print("-*60")
data5="this is a book ~~~~"
print(data5[:4])

#.append 附加元素
data6=["Bert","Lin","Chris","John"]
print(data6)
data6.append("David")
data6.append("chen")
data6.append(1000)
print(data6)

#.pop 拔除元素
data6.pop(3)
print(data6)
name=data6.pop(2)
print(name)
print(data6)

print("學生成績:",scores)
print("學生總和:",sum(scores))
print("學生平均:",sum(scores)/len(scores))

##字典(dict) or object
scores2={
    #key   ,Value
    "Bert":99, # Key-Value pair , 鍵值對
    "Jerry":77,
    "Chen":89,
    "Terry":92,
    "Chung":93
}
print("學生總和:",sum(scores2.values()))
print("學生平均:",sum(scores2.values())/len(scores2))

data7={
    "name":"Bert",
    "age": 20,
    "message": "Hello"
}
print(data7)
print(type(data7))

#Dist常用方法
#取數值
print("-"*60)
print("dist取數值")
print(data7["name"])
print(data7["age"])

#修改數值
print("-"*60)
print("修改值")
data7["name"]="Jerry"
print(data7)
print(data7["name"])

#新增數值
print("-"*60)
print("新增數值")
data7["interest"]=["聽音樂","看電視","吃東西"]
print(data7)

#刪除數值
print("-"*60)
print("刪除數值")
del data7["name"]
#del data7["age"]
#del data7["message"]
print(data7)

print("-"*60)
print(".keys and .values")
#.keys()
keys=list(data7.keys())
print(keys)
print(keys[0])
print(keys[1])


#.values()
print("*"*60)
values=list(data7.values())
print(values)
print(values[0])
print(values[1])

#和list比較
print("-"*60)
data8=["Bert",18,"您好~~"]
print(data8[1])
print(data8[2])

data8[1]=20
data8[2]="大家好啊"
print(data8)