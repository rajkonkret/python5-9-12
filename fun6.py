def fun1():
    print("To jest fun1")

    def fun2(text):
        print("To jest fun2")
        print(text)

    return fun2

    def fun3():
        print("To jest funkcja 3")

    return fun3


xFun1 = fun1()
print(type(xFun1))
xFun1("radek")
