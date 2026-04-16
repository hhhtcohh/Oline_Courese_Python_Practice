# try:
#     print("========================================")
#     print(my_name)
#     print("========================================")
# except NameError as e:
#     print("程序出错,请联系管理员",e)
try:
    print("========================================")
    print(my_name)
    print(1/0)
    print("========================================")
except Exception as e:
    print("程序出错,请联系管理员",e)
finally:
    print("资源释放")