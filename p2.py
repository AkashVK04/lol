def decorator1(a):
    def wrapper1():
        print("This is my decorator1 funaction")
        a()
        print("This is end of program1")
    return wrapper1

def decorator2(a):
    def wrapper2():
        print("This is my decorator2 funaction")
        a()
        print("This is end of program2")
    return wrapper2

@decorator1
@decorator2
def add():
    print("This is add function")
add()

#function=decorator1(decorator2(add))
#function()