

for i in range(5):
    username = input("请输入您的账号:")
    password = input("请输入您的密码:")
    if username=="" or password=="":
        print("账号密码不能为空")
        print(f"还剩{4 - i}次机会，请重新尝试")
        if i==4:
            print("登录失败")
        continue
    elif username=="1" and password=="123456789":
        print("欢迎登陆91平台~")
        break
    else:
        print("密码错误，请重新输入账号密码访问神秘世界")
        print(f"还剩{4 - i}次机会，请重新尝试")
        if i==4:
            print("登录失败")