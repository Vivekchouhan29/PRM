num = int(input("enter a nth o. of fibonacci :"))

def fibonacci(num):
    a = 0
    b = 1
    if num < 0:
        print("Incorrect input")
    elif num == 0:
        print("Incorrect input")
    elif num == 1:
        return b
    else:
        for i in range(2,num+1):
            c = a + b
            a = b
            b = c
        return b
 
print(fibonacci(num))