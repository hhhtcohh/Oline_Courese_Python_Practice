from itertools import count

# t1=(1314,520,114514,3.14,8848,2333)
# print(t1)
# print(type(t1))
#
# print(t1[0])
# print(t1[-1])
#
# print(t1[0:5:1])
#
# print(t1.count(114514))
# print(t1.index(114514))
#
# t2=()
# print(t2)
# print(type(t2))
#
# t3=(100,)
# print(t3)
# print(type(t3))
#
# a,b,c,d,e,f=t1
# print(f" {a} | {b} | {c} | {d} | {e} | {f} ")
#
# g,*h = t1
# print(f"{g} | {h}")
#
# *i,j,k =t1
# print(f"{i} | {j} | {k}")

# a=13
# b=45
# a,b=b,a
# #左解包，右组包
# print(a,b)
#
# a=100
# b=200
# c=300
# c,a,b=a,b,c
# print(a,b,c)



# 根据如下提供的学生成绩单，完成如下需求：
# 1. 计算每个学生的总分、各科平均分，然后一并输出出来。
# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
# 3. 查找成绩优秀（平均分大于90）的学生，并输出。

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}")
print()
Chinese_scores=[s[2] for s in students]
Math_scores=[s[3] for s in students]
English_scores=[s[4] for s in students]
print(f"语文最低分:{min(Chinese_scores)},最高分:{max(Chinese_scores)}")
print(f"数学最低分:{min(Math_scores)},最高分:{max(Math_scores)}")
print(f"英语最低分:{min(English_scores)},最高分:{max(English_scores)}")
print()
print("本次考试优秀的学生有:")
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    if avg > 90:
        print(f"{s[1]} \t平均分为:{avg:.1f}")
