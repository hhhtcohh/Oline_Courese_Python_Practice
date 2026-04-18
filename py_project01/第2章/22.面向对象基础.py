# #定义类
# class Car:
#     pass
#
# #创建对象
# c1=Car()
#
# #动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BWM"
# c1.name = "X5"
# c1.price = 500000
# print(c1.__dict__)#将属性以键值对的字典输出
# print(c1.color)
# print(c1.brand)
# print(c1.name)

#定义类
class Car:
    wheel=4
    tax_rate=0.51

# __init__ 方法是初始化的方法, 会在对象创建时自动调用,
# 可以在该方法中为对象设置对应的属性 ;
# self: 是第一个参数, 表示当前所创建出来的实例对象
    def __init__(self,c_color,c_brand,c_name,c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕,对象属性添加完毕!")
    def running(self):
        print(f"{self.name} {self.brand}正在高速行驶!!")
    def total_cost(self,discount,rate):
        """
        计算总费用
        :param discount:折扣(小数)
        :param rate: 税率
        :return:提车的总费用
        """
        total_cost = (discount + rate) * self.price
        return total_cost
    def __str__(self):
        return (f"{self.color} "
                f"{self.brand} "
                f"{self.name} "
                f"{self.price}")
    def __eq__(self,other):
        return (self.color == other.color
                and self.brand == other.brand
                and self.name == other.name
                and self.price == other.price)
    def __lt__(self,other):
        return self.price <= other.price


# #创建对象
# c1=Car("红色","X7","BWM",800000)
# print(c1.__dict__)
#
# c2=Car("白色","C4","奔驰",450000)
# print(c2.__dict__)
#
# c1.running()
# total=c1.total_cost(discount=0.9,rate=0.1)
# print("提车的总费用为:",total)\

#创建对象
c1=Car("白色","汉","BYD",9000)
# print(c1)
# c2=Car("白色","汉","BYD",9000)
# print(c2)
# print(c1 == c2)
# print(c1 < c2)
print(c1.brand)
print(Car.wheel)
print(c1.wheel)