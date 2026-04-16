# def triangle_area(b,h):
#     area = (b*h)/2
#     return area
# print(triangle_area(3,4))
#
# def count_aeiou(s) :
#     count = 0
#     for w in s:
#         if w.lower() in "aeiouAEIOU":
#             count += 1
#     return count
# print(count_aeiou("hello"))
#
# def calc_score(score_list):
#     max_score = max(score_list)
#     min_score = min(score_list)
#     avg_score = round(sum(score_list) / len(score_list),2)
#     return max_score, min_score, avg_score
# s_list=[600,504,546,549,579,691]
# max_score, min_score, avg_score = calc_score(s_list)
# print(max_score, min_score, avg_score)

def rank(a):
    if a >= 90 and a <= 100:
        return "A"
    elif a >= 75 and a < 90:
        return "B"
    elif a >= 60 and a < 75:
        return "C"
    elif a >= 0 and a < 60:
        return "D"
    else:
        return "error"
print(rank(98))
print(rank(76))
print(rank(69))
print(rank(51))
print(rank(101))

# def palindrome(str) :
#     if str[::1] == str[::-1]:
#         return True
#     else:
#         return False
# print(palindrome("黄山落叶松叶落山黄"))
# print(palindrome("天青色等烟雨"))
def palindrome(str) :
    return str == str[::-1]
print(palindrome("黄山落叶松叶落山黄"))
print(palindrome("天青色等烟雨"))

def time_converter(time) :
    h=time//3600
    m=time%3600//60
    s=time%60
    return str(h)+":"+str(m)+":"+str(s)
print(time_converter(62960))

def tell_triangle(a,b,c) :
    if a+b>c and a+c>b and b+c>a:
        if a==b==c :
            return "等边三角形"
        elif a==b or a==c or b==c :
            return "等腰三角形"
        else :
            return  "普通三角形"
    else:
        return "不能构成三角形"

print(tell_triangle(3, 4, 5))
print(tell_triangle(3, 3, 5))
print(tell_triangle(3, 4, 6))
print(tell_triangle(3, 5, 6))
print(tell_triangle(3, 4, 7))
print(tell_triangle(8, 8, 8))