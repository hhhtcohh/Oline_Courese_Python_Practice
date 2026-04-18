"""
msg = input("请输入你要遍历的字符串：")
for i in msg:
    print(i)
else :
    print("遍历结束")
"""

"""
total=0
for i in range(1,101):
    if i%2==1:
        total=total+i
print(f"1-100的奇数和为{total}")

total=0
for i in range(1,101,2):
    total=total+i
print(f"1-100的奇数和为{total}")
"""

# total=0
# for i in range(100,501):
#     if i%3==0:
#         total=total+i
# print(total)

# m=int(input("m="))
# n=int(input("n="))
# for j in range(1,n+1):
#     for i in range(1,m+1):
#         if i<m:
#             print("*",end="    ")
#         else:
#             print("*",end="\n")


"""
m=int(input("m="))
n=int(input("n="))
for j in range(1,n+1):
    for i in range(1,m+1):
        print("*",end="    ")
    print()
"""

for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}",end="\t")
    print()