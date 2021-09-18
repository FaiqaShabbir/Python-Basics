def fun():
    print("First Function!")

    def fun1():
        print("First child function1!")

    def fun2():
        print("Second child function!")

    fun1()
    fun2()


fun()
