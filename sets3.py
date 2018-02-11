#main is the main program
#treats lists as multisets, you can use remove_repeats to get rid of repeating elements
#the empty list "[]" is an element of every list
#[[[]]] is treated as [[]], same is true for [[[[]]]],[[[[[[]]]]]],...

compute = "subset"

def flatten(l):
    new_list = []
    for i in l:
        if i == []:
            new_list = new_list + [[]]
        elif type(i) == list:
            new_list = new_list + flatten(i)
        else:
            new_list = new_list + [i]
    return new_list

def main(l1,l2):
    if type(l1) and type(l2) != list:
        print("arguments are not lists")
    else:
        a = flatten(l1)
        b = flatten(l2)
        if compute == "subset":
            result = subset(substract_elements(a,b))
        elif compute == "union":
            result = l1 + l2
            print("the union is: ",result)
        elif compute == "intersection":
            result = substract_elements(a,b)[0]
            print("the intersection is: ")
        elif compute == "complement":
            result = substract_elements(a,b)[1]
        return result


def substract_elements(x,y):
    if len(x) <= len(y):
        big = y
        small = x
    elif len(x) > len(y):
        big = x
        small = y
    else:
        print("substract element error")
    i = 0
    big_len = len(big)
    small_len = len(small)
    common_elements = []
    copy_small = small[:]
    copy_big = big[:]
    while i < big_len:
        a = big[i]
        j = 0
        while j < small_len:
            b = small[j]
            if a == b:
                common_elements = common_elements + [copy_small[j]]
                del copy_small[j]
                del copy_big[i]
                small_len = small_len - 1
                big_len = big_len - 1
            elif a != b:
                j = j + 1
        i = i + 1
    return [common_elements,copy_big, copy_small, big, small]

def subset(l3):
    print(l3)
    if l3[0] == [] and l3[4] != []:
        print("the sets are disjoint")
        return True
    elif len(l3[0]) == len(l3[4]):
        if len(l3[3]) == len(l3[4]):
            print("the sets are equal")
        elif len(l3[4]) < len(l3[3]):
            print(l3[4],"is a proper subset")

def remove_repeats(l4):
    i = 0
    new_list = []
    len_list = len(l4)
    while i < len_list:
        if l4[i] not in new_list:
            new_list = new_list + [l4[i]]
        i = i + 1
    return new_list

#Tests

a = [1,2,3]
b = [1,2,3]
c = [2,2,3]
d = [0,4,5,7]
e = [[],[]]
f = [[]]
g = []
h = [1,2,3,5,9]
i = [4,5,6]
j = [[[],[]],[]]
k = [[[[]]]]
l = [[[1]],[2,[3]],[]]

main(a,d)
main(a,b)
main(a,h)
main(e,f)
main(g,f)
main(f,g)
main(a,i)
main(e,j)
main(a,g)
main(k,g)
main(k,f)
main(a,l)
