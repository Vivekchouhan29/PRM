list1=[1,2,3,4,5,6]
def find_len(list1):
    lst = []
    length = len(list1)    
    lst.append(list1[length-1])
    lst.append(list1[0])
    lst.append(list1[length-2])
    lst.append(list1[1])                                
    lst.append(list1[length-3])
    lst.append(list1[2])
    
    print(lst)
 
Largest = find_len(list1)