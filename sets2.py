#the main function is check_subset, it checks whether two zero-depth list are subsets of each other
#the empty list is a subset of all lists, it does not check if the empty list is contained multiple times

def flatten(List):
    for i in List:
        if type(i) == list:
            flatten(i)
        else:
           


def verdict(subset, result):
    if result == True:
        if subset != None:
            print(subset, "is the proper subset")
        elif subset == None:
            print("the sets are equal")
        return True
    elif result == False:
        print(subset, "the sets are not equal nor are they subsets of each other")
        return False

def check_subset(x,y):
    if type(x) and type(y) != list:
        print("arguments are not lists")
    elif len(x) < len(y):
        subset = x
        result = substract_elements(y,x)
    elif len(y) < len(x):
        subset = y
        result = substract_elements(x,y)
    elif len(y) == len(x):
        subset = None
        result = substract_elements(x,y)
    else:
        print("something went wrong")
    verdict(subset,result)

def substract_elements(x,y):
    copy_y = y[:]
    i = 0
    length_x=len(x)
    length_y=len(y)
    while i < length_x:
        a = x[i]
        j = 0
        print("i: ", i)
        print("j: ", j)
        while j != length_y:
            b = copy_y[j]
            if a == b:
                del copy_y[j]
                length_y = length_y - 1
            elif a != b:
                j = j + 1
        i = i + 1
    if copy_y == []:
        print("True")
        return True
    else:
        print("False")
        return False


#Tests

a = [1,2,3]
b = [2,2,3]
c = [0,9,5,4]
d = []
e = [1,2,3,4,1,5,6,3,5,6,1,2]
f = [1,2,3]
g = [[],[]]

check_subset(e,a)
check_subset(a,d)
check_subset(a,f)
check_subset(d,g)
