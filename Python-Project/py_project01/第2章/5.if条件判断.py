
"""score = int(input("请输入你的成绩："))
if 90 <= score  :
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
elif score >= 0:
    print("fall")
else:
    print("error")


year = int(input("请输入需要判定的年份："))
if (year % 4 == 0 and year % 100 != 0)or(year % 400 == 0):
    print(f"{year}是闰年")
else :
    print(f"{year}是平年")
"""
"""
a = int(input("a="))
b = int(input("b="))
c = int(input("c="))


if a + b > c and a + c > b and c + b > a :
    if a == b == c:
        print("1")
    elif a == b or b == c or c == a:
        print("2")
    else:
        print("3")
else :
        print("4")
"""

first_price=0.4883
second_price=0.5383
third_price=0.7883
first_max=2880
second_max=4800

elect_usage=float(input("请输入电量："))
elect_cost=float()
if 0 <= elect_usage <= first_max:
    elect_cost =elect_usage*first_price
elif first_max <= elect_usage <= second_max:
    elect_cost =(elect_usage-first_max)*second_price+first_max*first_price
elif second_max <= elect_usage:
    elect_cost =(elect_usage-second_max)*third_price+(second_max-first_max)*second_price+first_max*first_price
else :
    print("error")
print(f"您的电费为:{elect_cost}元")