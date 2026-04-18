# import random
#
# num_random=random.randint(1,100)
#
# while True:
#     num = int(input("请输入一个1-100内的数字:"))
#     if num_random < num:
#         print("您猜大了")
#     elif num_random > num:
#         print("您猜小了")
#     else :
#         print(f"您猜对了,该数为{num_random}")
#         break

total=0
for i in range(1001):
    if i%5==0:
        total+=i
print(f"1000以内所有5的倍数的和为:{total}")

str = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
count=0

for i in str:
    if i=="a" or i=="k":
        count+=1
print(f"字符串中有{count}个a和k")

