# """
# 采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
#     1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
#         1.1 输入学生姓名、语文成绩、数学成绩、英语成绩
#         1.2 检查学生姓名是否已存在, 如果学生不存在, 再添加 (存在则, 不添加)
#         1.3 验证成绩范围（0-100分）
#         1.4 创建学生对象并添加到系统
#     2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
#         2.1 输入要修改的学生姓名
#         2.2 根据姓名查找该学生, 显示该生当前成绩信息
#         2.3 输入新的语文、数学、英语成绩
#         2.4 更新学生成绩数据
#     3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
#     4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
#         4.1 输出格式为: "姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
#     5. 展示全部学生成绩：展示出系统中所有学生的成绩
# """
#
# class Student:
#     def __init__(self,name,chinese,math,english)    :
#         self.name=name
#         self.chinese=chinese
#         self.math=math
#         self.english=english
#     #"姓名：张三 | 语文：85 | 数学：90 | 英语：88 | 总分：263"
#     def __str__(self):
#         return f"姓名:{self.name} | 语文:{self.chinese} | 数学:{self.math} | 英语:{self.english} | 总分:{self.english+self.math+self.chinese}"
#     #修改学生成绩
#     def update(self,chinese=None,math=None,english=None):
#         if chinese is not None :
#             self.chinese=chinese
#         if math is not None :
#             self.math=math
#         if english is not None :
#             self.english=english
# #教务管理系统
# class EduManagement:
#     system_version="1.0"
#     system_name="教务管理系统"
#     def __init__(self):
#         self.student_list=[]
#     #增
#     def add_student(self):
#         name=input("请输入学生姓名:")
#         for s in self.student_list:
#             if s.name==name:
#                 print("该学生已存在,添加失败!")
#                 return
#
#         chinese=int(input("请输入学生语文成绩:"))
#         math=int(input("请输入学生数学成绩:"))
#         english=int(input("请输入学生英语成绩:"))
#         if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
#             stu=Student(name,chinese,math,english)
#             self.student_list.append(stu)
#             print("学生信息添加成功~")
#         else :
#             print("各科成绩必须在0-100之间")
#
#     #改
#     def update_student(self):
#         name=input("请输入学生姓名:")
#         for s in self.student_list:
#             if s.name!=name:
#                 print("该学生未存在,添加失败!")
#                 return
#             else:
#                 print(f"当前成绩:{s}")
#                 chinese = int(input("请输入修改后的学生语文成绩:"))
#                 math = int(input("请输入修改后的学生数学成绩:"))
#                 english = int(input("请输入修改后的学生英语成绩:"))
#                 if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
#                     s.update(chinese,math,english)
#                     print("学生信息修改成功~")
#                     print(f"修改后的成绩:{s}")
#                     return
#                 else:
#                     print("各科成绩必须在0-100之间")
#                     return
#
#     #删
#     def delete_student(self):
#         name=input("请输入要删除的学生姓名:")
#         for s in self.student_list:
#             if s.name!=name:
#                 print("该学生未存在,删除失败!")
#                 return
#             else:
#                 self.student_list.remove(s)
#                 print("学生信息删除成功~")
#                 return
#
#     #查
#     def query_student(self):
#         name = input("请输入要查找的学生姓名:")
#         for s in self.student_list:
#             if s.name != name:
#                 print("该学生未存在,查找失败!")
#                 return
#             else:
#                 print(f"学生信息:{s}")
#                 return
#     #展示
#     def show_student(self):
#         for s in self.student_list:
#             print(f"学生信息:{s}")
#         return
#     # 运行系统
#     def run(self):
#         print(f"欢迎使用教务管理系统 V{EduManagement.system_version}")
#         while True:
#             print()
#             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
#             print("# 1.添加学生  2.修改学生  3.删除学生  4.查找学生  5.展示所有学生  6.退出系统 #")
#             print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
#             print()
#             choice =input("请输入当前要执行的操作(1-6):")
#             match choice :
#                 case "1":
#                     self.add_student()
#                 case "2":
#                     self.update_student()
#                 case "3":
#                     self.delete_student()
#                 case "4":
#                     self.query_student()
#                 case "5":
#                     self.show_student()
#                 case "6":
#                     print("系统成功退出")
#                     break
#                 case _:
#                     print("非法操作,请重试")
#
# # 测试
# if __name__=="__main__":
#     edu_management=EduManagement()
#     edu_management.run()
#
#
#
#购物车管理系统制作
"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。
具体功能如下：
    1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称: xxx, 商品价格: xxx, 商品数量: xxx"。
    5. 退出购物车
"""
#制做商品类
class Goods:
    def __init__(self,goods_name,goods_price,goods_num):
        self.name=goods_name
        self.price=goods_price
        self.num=goods_num
    def __str__(self):
        return f"商品名称:{self.name} | 商品价格:{self.price} | 商品数量:{self.num}"
    def update_price(self,goods_name=None,goods_price=None,goods_num=None):
        if goods_name is not None:
            self.name=goods_name
        if goods_price is not None:
            self.price=goods_price
        if goods_num is not None:
            self.num=goods_num

#制作购物车系统
class CartSystem:
    version="1.0.0"
    name="购物车商品管理系统"

    def __init__(self):
        self.goods_list=[]

    #增
    def add_goods(self):
        goods_name=input("请输入要添加的商品名称:")
        for l in self.goods_list:
            if l.name == goods_name:
                print("该商品已存在,请重试~")
                return
        goods_price = float(input("请输入该商品价格:"))
        if goods_price < 0:
            print("输入异常")
            return
        goods_num = int(input("请输入该商品数量:"))
        if goods_num < 0 and type(goods_num) is not int:
            print("输入异常")
            return
        goods_info =Goods(goods_name,goods_price,goods_num)
        self.goods_list.append(goods_info)
        print("商品添加成功")
        return


    #改
    def update_goods(self):
        goods_name=input("请输入要修改的商品名称:")
        for l in self.goods_list:
            if l.name == goods_name:
                print(f"{l}")

                goods_price = float(input("请输入该商品修改后的价格:"))
                if goods_price < 0:
                    print("输入异常")
                    return
                goods_num = int(input("请输入该商品修改后的数量:"))
                if goods_num < 0 :
                    print("输入异常")
                    return
                l.update_price(goods_name,goods_price,goods_num)
                print("商品修改成功")
                return
        print("该商品不存在,请重试~")

    # 删
    def delete_goods(self):
        goods_name = input("请输入要删除的商品名称:")
        for l in self.goods_list:
            if l.name == goods_name:
                self.goods_list.remove(l)
                print("商品删除成功")
                return
        print("该商品不存在,请重试~")

    #查
    def query_goods(self):
        if not self.goods_list:
            print("购物车为空!")
            return
        for l in self.goods_list:
            print(f"查找到该商品,商品信息:{l}")

#运行程序(方法)
    def run(self):
        print()
        print(f"欢迎使用购物车管理系统 V{CartSystem.version}")
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加商品  2.修改商品  3.删除商品  4.查询购物车  5退出系统  #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()
            choice =input("请输入当前要执行的操作(1-5):")
            try :
                match choice :
                    case "1":
                        self.add_goods()
                    case "2":
                        self.update_goods()
                    case "3":
                        self.delete_goods()
                    case "4":
                        self.query_goods()
                    case "5":
                        print("系统成功退出")
                        break
                    case _:
                        print("非法操作,请重试")
            except ValueError:
                print("输入的数据有问题,请重新输入!!!")
            except Exception:
                print("输入的数据有问题,请在1-6中重新选择!!!")
if __name__ == "__main__":
    Cart_system=CartSystem()
    Cart_system.run()