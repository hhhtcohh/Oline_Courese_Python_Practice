import json

# #写入json数据文件
# user = {
#     "name": "小予",
#     "age":20,
#     "gender":"男",
#     "hobbies":["跑步","羽毛球"]
# }
# with open("./resources/user.json","w",encoding="utf-8") as f:
#     json.dump(user,f,ensure_ascii=False,indent=4)#ensure_ascii=False:非ASCII码不转义,保留原样输出 #indent:在键值对前缩进

#读取json数据文件
with open("./resources/user.json","r",encoding="utf-8") as f:
    user = json.load(f)
    print(user)
    print(type(user))