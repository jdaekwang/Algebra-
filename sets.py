def check_equal(x,y):
    if len(x) != len(y):
        print("the lists are not equal")
        return False
    elif x == y:
        print("the ordering and contents of both lists are the same")
        return True
    elif type(x) and type(y) != list:
        print("both or one of the objects are not lists")
    else:
        i = 0
        copy_x = x
        copy_y = y
        while i < len(x):
            a = x[i]
            j = 0
            while j < len(y): 
                b = y[j]
                if a == b:
                    copy_x = copy_x[(i+1):]
                    copy_y = copy_y[0:j]+copy_y[(j+1):]
                j = j + 1
            i = i + 1
        print(copy_x,copy_y)
        if copy_x == [] and copy_y == []:
            print("the contents of both lists are the same")
            return True
