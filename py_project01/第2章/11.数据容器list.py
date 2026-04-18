# """"""
# s=[22,2,19,5,33,8,27,10]
# print(s)
# print(s[0])
# print(s[-8])
# s[4]=23
# print(s)
# print(s[1:6:2])
# print(s[0:6:1])
# print(s[:6])
#
#
# #list工具
# s.append(10086)
# print(s)
#
# s.insert(1,10)
# print(s)
#
# s.remove(10)
# print(s)
#
# e=s.pop()
# print(s)
# print(e)
#
# s.pop(7)
# print(s)
#
# s.reverse()
# print(s)
#
# s.sort()
# print(s)
# #
# # s=[]
# # total=0
# # ave1=0
# # ave2=0
# # for i in range(5):
# #     num=int(input("请输入一个数字:"))
# #     s.append(num)
# # print(s)
# # s.sort()
# # print(s)
# # print(s[0],s[-1])
# # for j in s:
# #     total+=j
# # ave1=total/5
# # ave2=sum(s)/len(s)
# # print(ave1,ave2)
# """
#
# s1=[22,12,4,19,5]
# s2=[12,4,3,9]
# s3=[*s1,*s2]
# s4=s1+s2
# for i in s2:
#     s1.append(i)
# print(s1)
#
# #简化版s3,s4
# print(s3)
# print(s4)
#
# new_s=[]
# for i in s1:
#     if i not in new_s:
#         new_s.append(i)
# print(new_s)
#
#
#
#
# list=[]
# for i in range (1,21):
#     list.append(i**2)
# print(list)
#
# list2=[i**2 for i in range(1,21)]
# print(list2)
#
# a=[2,4,4,6,5,7,9]
# b=[i**2 for i in a if i%2==0]
# print(b)"""


list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']
list0 = list1 + list2 + list3
new_list = []
for i in list0:
    if i not in new_list:
        new_list.append(i)
print(new_list)
new_list.sort()
print(new_list)



list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
newlist=[i**2 for i in list4 if i%3==0 or i%5==0]
print(newlist)


list5 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
newList=[i for i in list5 if i>0 ]
print(newList)

