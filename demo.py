'''
print("你好，大头")
print(1487)
print(1.487)
print(True,False)
print(None)
print(())
print([])
print({})

# a = 2 
# print(a)

a = float(input("请输入数字："))
b = float(input("请输入数字："))
print("和:",a+b)

# print(type("A"))

name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
job = input("请输入你的工作：")
print("大家好，我叫{mz},我{nl}岁,我的工作是{rjcs}。虽然我才{nl}岁，但是我在{rjcs}这一行干了很多年，所以{nl}岁不是问题，{rjcs}让我积极热情，这就是我{mz}的态度。".format(mz=name,nl=age,rjcs=job))

print(1==2)

a = "大家好，我叫付小胖,我18岁,我的工作是软件测试。虽然我才18岁，但是我在软件测试这一行干了很多年，所以18岁不是问题，软件测试让我积极热情，这就是我付小胖的态度。"
print(len(a))




print('\n'.join([''.join([('LoveSongxiaolong'[(x-y)%8]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)]))




xx = (4,5,'哈哈',6,7,'啦啦','A','B')
print(xx.count('哈哈'))
print(xx.index('啦啦'))

yy = (7,8,9,xx)
print(yy)

print(len(xx)+len(yy))

print(len(xx))

print(len(yy))

zz = ['波波肠',123,'火锅',456,'炸鸡',789,'麻辣烫',741,'冰激凌']
print(zz.index('火锅'))
print(zz.count('炸鸡'))

zz.append(852)
zz.insert(3,'可乐')
zz.remove('冰激凌')

c = zz.pop(4)
zz.append(c)
zz[1] = '可乐'
print(zz)
'''

'''
通过input分别输入多段字符串，然后获取他们的长度，
并且把长度的值分别存放到数组中，并从小到大的排序。

aa = input("请输入:")
bb = input("请输入:")
cc = input("请输入:")
dd = input("请输入:")
xx = []
a = len(aa)
b = len(bb)
c = len(cc)
d = len(dd)
xx.append(a)
xx.append(b)
xx.append(c)
xx.append(d)
xx.sort()
print(xx)


aa = input("请输入:")
bb = input("请输入:")
cc = input("请输入:")
dd = input("请输入:")
xx = [len(aa), len(bb), len(cc), len(dd)]
xx.sort()
print(xx)

a = [1,2,3,4,5,6,7,8,9,10]
b = []
for i in a:
    if i % 2 != 0:
        b.append(i)
        
print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [i for i in a if i % 2 != 0]
print(b)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.clear()
print(a)
'''

# A = {"name":"付大头"}
# # print(A['name'])
# # print(A.get('name'))

# A['age'] = 17
# # print(A)

# A.pop('name')
# print(A)


a = {'name':"付大头",'age':'18','sex':'女','aihao':{'jia':'吃饭','pian':'喝玩','real':'学习'}}
# b = a['aihao']
# print(b)

# print(list(a.keys()))
# print(list(a.values()))

# a.pop('name')
# print(a.get('name'))
# print(a['name'])
'''
import demo1

demo1.jiafa(111,222)


# from demo1 import jiafa

# jiafa(444,555)


data = [{"ID":1,"Name":"张三","status":0},{"ID":2,"Name":"李四","status":1}]
list = []
for i in data:
    list.append(i["ID"])
    list.append(i["Name"])
print(list)




# d = dict()

# dd = {k:v for k,v in d.items()}
# print(dd)



# dict = {'Name': 'Runoob', 'Age': 7}
# for i,j in dict.items():
#     print(i,j)


def calculation_loan_quota(money, all_loan_quota):
    """计算公积金贷款额度
    :param money: 每个月公积金
    :param all_loan_quota: 总贷款额度
    :return:多少个月
    """
    # 计算12个月的贷款额度
    all_money = (money * (1 + 12) * 6) / 12 * 15
    print(all_money)
    if all_money == all_loan_quota:
        print('第12个月可以贷款{}'.format(all_loan_quota))
        return 12
    # 不足12月
    elif all_money > all_loan_quota:
        for month in range(1, 13):
            if all_loan_quota <= (money * (1 + month) * month / 2) / 12 * 15:
                print('第{}个月可以贷款{}'.format(month, all_loan_quota))
                return month
    # 12个月贷款不够总额度
    else:
        for month in range(12, 100):
            if all_loan_quota <= (month + (month - 12) * 2) * 6 * money / 12 * 15:
                print('第{}个月可以贷款{}'.format(month, all_loan_quota))
                return month
        print('第99个月也不够，你注定无法贷款')
        return 100


calculation_loan_quota(1000, 500000)




name = input("请输入你的姓名：")
age = input("请输入你的年龄：")
job = input("请输入你的工作：")
print("大家好，我叫{mz},我{nl}岁,我的工作是{rjcs}。虽然我才{nl}岁，但是我在{rjcs}这一行干了很多年，所以{nl}岁不是问题，{rjcs}让我积极热情，这就是我{mz}的态度。".format(mz=name,nl=age,rjcs=job))

name = "付大头"
age = 18
weight = 45.5
stu_id = "00001"

# 我今年18岁了。
print("我今年%d岁" % age)
# 我的名字是付大头。
print("我的名字是%s" % name)
# 我的体重是45.5KG。
print("我的体重是%.2f" % weight)
# 我的学号是00001
print("我的学号是%05d" % stu_id)
# 我的名字是付大头，今年18岁了。
print("我的名字是%s,今年%d岁了" % (name,age))
print("我的名字是%s,明年%d岁了" % (name,age+1))
# 我的名字是付大头，今年18岁了，体重45KG，学好是00001
print("我的名字是%s,今年%d岁了，体重是%.2fKG,学号是%05d" %(name,age,weight,stu_id))
print("我的名字是%s,今年%s岁了，体重是%sKG,学号是%05d" %(name,age,weight,stu_id))

# 方法1
print(f"我的名字是{name},今年{age}岁了")
# 方法2
print(f"我的名字是{name}，今年{age}岁了，体重{weight}KG，学号是{stu_id}".format(name,age,weight,stu_id))
# 方法3
print("我的名字是{mingzi}，今年{nianling}岁了，体重{tizhong}KG，学号是{xuehao}".format(mingzi=name,nianling=age,tizhong=weight,xuehao=stu_id))
'''
# print("hello world",end="---")
# print("hello world",end="\n'")


print("hello\nworld")
print("hello\tworld")
print("\nhello world")
print("\thello world")
