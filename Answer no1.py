size=int(input("Enter the number of elements: "))
lst1=[]
for i in range(size):
    num= input("Enter the element: ")
    lst1.append(num)

print(lst1)
res = sorted(lst1, key = lambda sub : sub[-2])

print("Sorted List : " + str(res))



