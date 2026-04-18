# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def power(a,b):
#     return a**b
# def calculate(a,b,oper):
#     return oper(a,b)
# print(calculate(31,2,div))


# outline = lambda :print("-------------------------------------------")
# outline()
#
# def add(a,b):
#     return a+b
# add1=lambda a,b:a+b
# print(add1(1,2))
#
# game_list1=["PUBG","Counter Strike 2","Terraria","No Man's Sky","Black Myth Wukong"]
# game_list1.sort()
# print(game_list1)
#
# game_list2=["PUBG","Counter Strike 2","Terraria","No Man's Sky","Black Myth Wukong"]
# game_list2.sort(key=lambda s : len(s))
# print(game_list2)
#
# def factorial (n):
#     if n <= 0:
#         return "error"
#     else :
#         if n == 1:
#             return 1
#         else:
#             return n * factorial(n-1)
# print(factorial(9))

"""
案例2: 定义一个用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额的函数。
具体规则如下：
    1. 优惠券需要商品金额满5000才可以使用，且优惠券金额不能超过商品总价。
    2. 积分抵扣需要商品总金额满5000才可以使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
"""
def calc_order_cost(*args, coupon=0, score=0, express=0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量） ----> 如: ("鼠标", 188, 2) ("键盘", 388, 1)
    :param coupon: 优惠券
    :param score: 积分
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单的总金额 = 商品总金额 - 优惠券 - 积分抵扣 + 运费
    #1.获取商品总金额
    total_list= [s[1] *s[2] for s in args]
    total_cost = sum(total_list)
    #2.优惠券
    if total_cost>=5000 and coupon<=total_cost:
        total_cost -= coupon
    else:
        print("未达优惠券使用条件")
    #3.积分
    if total_cost >= 5000 and score//100<=total_cost :
        total_cost -= score//100
    else:
        print("未达积分使用条件")
    #4.运费
    total_cost +=express
    if total_cost<0:
        total_cost = 0
    return total_cost
cost=calc_order_cost(("Terraria",36,100),("No Man's Sky",42,100),("Black myth Wukong",198,2),coupon=100,score=10960,express=3.0)
print(cost)