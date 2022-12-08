def fun1():
    print("To jest fun1")

    def fun2():
        print("To jest fun2")

    return fun2


xFun1 = fun1()
print(type(xFun1))
xFun1()