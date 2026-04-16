# # s1={13,14,54,39,71,11,13,14}
# # print(s1)
# # print(type(s1))
# #
# # s2=set()
# # print(s2)
# # print(type(s2))
#
# s1={100,200,300,400,500}
# print(s1)
#
# s1.add(700)
# print(s1)
#
# s1.remove(200)
# print(s1)
#
# e=s1.pop()
# print(e)
# print(s1)
#
# s1.clear()
# print(s1)
#
# s2={"A","B","C"}
#
# s3={"A","C","E","F"}
#
# print(s2.difference(s3))
# print(s3.difference(s2))
# print(s2.union(s3))
# print(s2.intersection(s3))

# 选修足球学生名单
football_set = {"王林", "曾牛", "徐立国", "遁天", "天运子", "韩立", "厉飞雨", "乌丑", "紫灵"}
# 选修篮球学生名单
basketball_set = {"张铁", "墨居仁","王林", "姜老道", "曾牛", "王蝉", "韩立", "天运子", "李化元", "厉飞雨", "云露"}
# 选修法语学生名单
french_set = {"许木", "王卓", "十三", "虎咆", "姜老道", "天运子",  "红蝶", "厉飞雨", "韩立", "曾牛"}
# 选修艺术学生名单
art_set = { "遁天", "天运子", "韩立", "虎咆", "姜老道", "紫灵"}

print(french_set.intersection(art_set))
print(french_set & art_set)

print(french_set.intersection(art_set.intersection(football_set.intersection(basketball_set))))
print(french_set&art_set&football_set&basketball_set)


print(football_set.difference(basketball_set))
print(football_set-basketball_set)
s1={s for s in football_set if s not in basketball_set}
print(s1)

s_name=football_set|basketball_set|art_set|french_set
s_all=[*football_set,*basketball_set,*art_set,*french_set]
for s in s_name:
    print(f"{s} \t: {s_all.count(s)}")
