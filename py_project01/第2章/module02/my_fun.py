__all__=["separate1","separate4","NAME","PI"]

PI=3.1415926535
NAME="Ghost"

def separate1() :
    print("- " *10)

def separate2() :
    print("* " *10)

def separate3() :
    print("> " *10)

def separate4() :
    print("# " *10)
if __name__ == "__main__":#如果在当前文件运行则为__main__,但如果在跟其他文件中调用这个文件则显示为__文件名__
    separate1()


