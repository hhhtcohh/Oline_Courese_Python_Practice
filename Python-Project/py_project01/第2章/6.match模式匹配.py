"""day = input("请输入星期(1-7):")
match day:
    case "1":
        print("星期一")
    case "2":
        print("星期二")
    case "3":
        print("星期三")
    case "4":
        print("星期四")
    case "5":
        print("星期五")
    case "6" | "7":
        print("周末休息")
    case _ :
        print("输入错误")
"""

#辣鸡计算器
"""num1=float(input("请输入数字A:"))
num2=float(input("请输入数字B:"))
tool = input("请输入运算符(+-*/)")
match tool:
    case "+":
        print(f"{num1} + {num2} = {num1+num2}" )
    case "-":
        print(f"{num1} - {num2} = {num1-num2}" )
    case "*":
        print(f"{num1} * {num2} = {num1*num2}" )
    case "/" if num2 !=0 :
        print(f"{num1} / {num2} = {num1/num2}" )
    case "/"\
        if num2 == 0:
            print("学过小学数学吗？")
    case _:
        print("error")
"""

key=input("请输入指令:")
match key:
    case "w" | "W":
        print("角色向上移动")
    case "a" | "A":
        print("角色向左移动")
    case "d" | "D":
        print("角色向右移动")
    case "s" | "S":
        print("角色向下移动")
    case " " :
        print("角色跳跃")
    case "j" | "J":
        print("角色发动攻击")
    case "esc" | "Esc" :
        print("退出")