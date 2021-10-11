#def hello ():
#    print('Hello World!')
#
#hello ()

#x = int(input("Enter 1 number: "))
#y = int(input("Enter 2 number: "))

#def sum(a,b):
#    return a+b
#print(sum(x,y))
#z = sum(x,y)
#print(z)


#x = int(input("Enter 1 number: "))
#def f(a):
#    return 2*a-2
#print(f(x))

def f(a=5):
    return 2*a-2
#print(f())

a = 45
b = 5
def f():
    global a
    a = a + 2
    print(a)
f()
print(a)
