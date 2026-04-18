#读文件
#1.打开文件
f=open("./resources/罗曼罗兰.txt","r",encoding="utf-8")

#2.读取文件内容
# content=f.read()
content =f.readlines()
for line in content:
    print(line.strip())
#3.关闭文件
f.close()

# #写文件
# #1.打开文件
# f=open("./resources/静夜思.txt","w",encoding="utf-8")
# #2.写入文件内容
# f.write("静夜思(李白)\n\n")
# f.write("床前明月光,\n")
# f.write("疑是地上霜.\n")
# f.write("举头望明月,\n")
# f.write("低头思故乡.\n")
# #3.关闭文件
# f.close()

#-------------------------------------------

# #写文件,方式1
# #1.打开文件
# f=open("./resources/静夜思.txt","w",encoding="utf-8")
# #2.写入文件内容
# try:
#     f.write("静夜思(李白)\n\n")
#     f.write("床前明月光,\n")
#     f.write("疑是地上霜.\n")
#     f.write("举头望明月,\n")
#     f.write("低头思故乡.\n")
# except Exception as e:
#     print("error",e)
# #3.关闭文件
# finally:
#     f.close()

#-------------------------------------------

#写文件,方式2
with open("./resources/静夜思.txt","w",encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光,\n")
    f.write("疑是地上霜.\n")
    f.write("举头望明月,\n")
    f.write("低头思故乡.\n")
