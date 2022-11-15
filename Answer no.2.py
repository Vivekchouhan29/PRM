#Taking sides for tringle
side1 = int(input("Enter the Side1 Value  of Tringele : ")) 
side2 = int(input("Enter the Side2 Value  of Tringele : "))
side3 = int(input("Enter the Side3 Value  of Tringele : "))
#Taking sides for rectangle
num1 = int(input("Enter the Side1 Value  of Rectangle : "))
num2 = int(input("Enter the Side1 Value  of Rectangle : "))
num3 = int(input("Enter the Side1 Value  of Rectangle : "))
num4 = int(input("Enter the Side1 Value  of Rectangle : "))


def checkingvalidation(side1,side2,side3,num1,num2,num3,num4):
    if (side1 + side2 > side3) and (side3 + side2 > side1) and (side1 + side3 > side2) :
        print("Valid Triangle")
    else:
        print("Invalid Triangle")
    
    if (num1 == num3) and (num2 == num4):
        print("Valid Rectangle")
    else:
        print("Invalid Rectangle")

checkingvalidation(side1,side2,side3,num1,num2,num3,num4)