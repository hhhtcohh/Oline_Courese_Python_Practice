# dict1={"语文":109,"数学":97,"英语":120,"物理":87,"化学":87,"生物":79}
# print(dict1)
# print(type(dict1))
#
# dict1["语文"]=150
# print(dict1)
# yw=dict1["语文"]
# print(yw)
#
# ---------------------------------------- 字典 常见操作 ---------------------------------------
# dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
# print(dict1)
#
# # 添加 - key不存在就是添加
# dict1["涛哥"] = 550
# print(dict1)
#
# # 修改 - key存在就是修改
# dict1["涛哥"] = 620
# print(dict1)
#
# # 查询
# print(dict1["涛哥"]) # 根据key获取value
# print(dict1.get("涛哥")) # 根据key获取value
#
# print(dict1.keys()) # 获取所有的key
# print(dict1.values()) # 获取所有的value
# print(dict1.items()) # 获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("许立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
#
# # 遍历
# for k in dict1.keys():
#     print(f"{k} : {dict1[k]}")
#
# for item in dict1.items():
#     print(f"{item[0]} : {item[1]}")
#
# for k,v in dict1.items():
#     print(f"{k} : {v}")

"""
    案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。
    具体功能如下：
        1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
        5. 退出购物车

    结构: shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {...}}
"""
from random import choice
from unittest import case

# shopping_cart = {}
# menu="""
# ############ 系统菜单 ###########
# #          1.添加购物车         #
# #          2.修改购物车         #
# #          3.删除购物车         #
# #          4.查询购物车         #
# #          5.退出购物车         #
# ###############################
# """
#
#
# print("欢迎使用购物车管理系统~")
#
# while True:
#     print(menu)
#     choice = input("请输入(1-5):")
#     match choice:
#         case "1":
#             goods_name = input("请输入要添加商品名称:")
#             goods_price = float(input("请输入商品价格:"))
#             goods_num = int(input("请输入商品数量:"))
#             if goods_num in shopping_cart:
#                 print("该商品已存在，请重新输入新商品")
#             else:
#                 shopping_cart[goods_name] = {"goods_price": goods_price, "goods_num": goods_num}
#                 print("商品添加完毕！")
#             continue
#
#         case "2":
#             goods_name = input("请输入要修改的商品名称:")
#
#             if goods_num not in shopping_cart:
#                 print("该商品不存在，请重新选择商品")
#             else:
#                 goods_price = float(input("请输入商品最新价格:"))
#                 goods_num = int(input("请输入商品最新数量:"))
#                 shopping_cart[goods_name] = {"goods_price": goods_price, "goods_num": goods_num}
#                 print("商品修改完毕！")
#             continue
#
#         case "3":
#             goods_name = input("请输入要删除的商品名称:")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在，请重新选择商品")
#             else:
#                 del shopping_cart[goods_name]
#                 print("商品删除完毕！")
#             continue
#         case "4":
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(
#                     f"商品名称为:{goods_name},商品价格为:{goods_info["goods_price"]},商品数量为:{goods_info["goods_num"]}")
#             continue
#         case "5":
#             print("已退出系统")
#             break
#         case _:
#             print("操作非法")
#             continue

print("欢迎使用教务管理系统")
student_list={}
menu = """
###################################################\t系统菜单\t#####################################################
#\t1.添加学生信息\t2.修改学生信息\t3.删除学生信息\t4.查询学生信息\t5.列出所有学生\t6.统计班级成绩\t7.退出系统\t#
#################################################################################################################
"""
while True:
    print(menu)
    choice = input("请输入(1-7):")
    match choice:
        case "1":
            student_name = input("请输入添加的学生姓名:")
            if student_name in student_list:
                print("该学生已存在,请重新试!!")
            else:
                student_chinese = float(input("请输入语文成绩:"))
                student_math = float(input("请输入数学成绩:"))
                student_english = float(input("请输入英语成绩:"))
                student_list[student_name] = {"chinese": student_chinese, "math": student_math,
                                              "english": student_english}
                print(f"添加[{student_name}]成功!!!")
            print()
            continue

        case "2":
            student_name = input("请输入修改的学生姓名:")
            if student_name not in student_list:
                print("该学生不存在,请重新试!!")
            else:
                student_chinese = float(input("请输入语文成绩:"))
                student_math = float(input("请输入数学成绩:"))
                student_english = float(input("请输入英语成绩:"))
                student_list[student_name] = {"chinese": student_chinese, "math": student_math,
                                              "english": student_english}
                print(f"修改[{student_name}]成功!!!")
            print()
            continue

        case "3":
            student_name = input("请输入删除的学生姓名:")
            if student_name not in student_list:
                print("该学生不存在,请重新试!!")
            else:
                del student_list[student_name]
                print(f"删除[{student_name}]成功!!!")
            print()
            continue

        case "4":
            student_name = input("请输入被查询的学生姓名:")
            if student_name not in student_list:
                print("该学生不存在,请重新试!!")
            else:
                student_score=student_list[student_name]
                print(f"{student_name}同学,语文成绩:{student_score['chinese']},数学成绩:{student_score['math']},英语成绩:{student_score['english']}")
                print(f"查找[{student_name}]成功!!!")
            print()
            continue

        case "5":
            print("学生如下:")
            for student_name in student_list.keys():
                print(f"{student_name}")
            print()
            continue

        case "6":

            list_chinese=[]
            list_math=[]
            list_english=[]
            for student_name,score in student_list.items():
                list_chinese.append(score["chinese"])
                list_math.append( score["math"])
                list_english.append(score["english"])

            max_chinese=max(list_chinese)
            max_math=max(list_math)
            max_english=max(list_english)

            min_chinese=min(list_chinese)
            min_math=min(list_math)
            min_english=min(list_english)

            avg_chinese=sum(list_chinese)/len(student_list)
            avg_math=sum(list_math)/len(student_list)
            avg_english=sum(list_english)/len(student_list)

            max_chinese_student=[student_name for student_name,score in student_list.items() if score["chinese"]==max_chinese]
            max_math_student=[student_name for student_name,score in student_list.items() if score["math"]==max_math]
            max_english_student=[student_name for student_name,score in student_list.items() if score["english"]==max_english]

            min_chinese_student=[student_name for student_name,score in student_list.items() if score["chinese"]==min_chinese]
            min_math_student=[student_name for student_name,score in student_list.items() if score["math"]==min_math]
            min_english_student=[student_name for student_name,score in student_list.items() if score["english"]==min_english]

            print(f"语文最高分:{max_chinese},语文最低分{min_chinese}:,平均分:{avg_chinese:.2f}")
            print(f"语文最高分是:{max_chinese_student},语文最低分是{min_chinese_student}")

            print(f"数学最高分:{max_math}语文最低分{min_math}:,平均分:{avg_math:.2f}")
            print(f"数学最高分是:{max_math_student},数学最低分是{min_math_student}")

            print(f"英语最高分:{max_english}英语最低分{min_english}:,平均分:{avg_english:.2f}")
            print(f"英语最高分是:{max_english_student},英语最低分是{min_english_student}")
            print()
            continue

        case "7":
            print("学生管理系统已退出!!!")
            print()
            break

        case _:
            print("输入错误,操作非法!!!")
            print()
            continue



