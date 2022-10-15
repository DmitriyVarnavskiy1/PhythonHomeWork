# Map

def Stepen(x,y):
    return x ** y

lst = [1 , 4 , 8 , 10, 9]
lst1 = [1 , 2 , 3 , 3]
L = map(Stepen , lst , lst1)
print(list(L))      

                                         
                                         
                                


def mapfunktionlist(function,lst1,lst2):  
    lst = []
    if len(lst1) >= len(lst2):
        length = len(lst2)
    else:
        length = len(lst1)
    for id in range(length):
        lst.append(function(lst1[id],lst2[id]))
    return lst

        

print(mapfunktionlist(Stepen,lst,lst1))