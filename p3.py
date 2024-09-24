def function(a):
    def wrapper(b):
        print("This is starting of program")
        result=a(b)+10
        return result
    return wrapper

#@function

def add(a):
    return a

print(add(20))

fun=function(a)
fun()
