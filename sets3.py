#main is the main program
#treats lists as multisets, you can use remove_repeats to get rid of repeating elements
#the empty list "[]" is considered as the empty set and it is the subset of all lists
#input must be a list
#elements of the list must be able to be comparable, i.e. <, > must make sense

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

def sort(l):
    new_list = []
    new_list_2 = []
    for i in l:
        if type(i) == list:
            new_list = [sort(i)]
        elif type(i) != list:
            new_list_2 = new_list_2 + [i]
    ordered_list = merge_sort(new_list_2) + new_list
    return ordered_list

def merge_sort(l):
    if len(l) > 1:
        first_half = l[:(len(l)//2)]
        second_half = l[(len(l)//2):]
        return merge(first_half, second_half)
    elif len(l) <= 1:
        return l

def merge(l1,l2):
    if len(l1) == 0:
        return l2
    elif len(l2) == 0:
        return l1
    elif l1[0] > l2[0]:
        sorted_list = [l2[0]] + merge(l2[1:],l1)
    else:
        sorted_list = [l1[0]] + merge(l1[1:],l2)
    return sorted_list
        

def main(l1,l2):
    if type(l1) and type(l2) != list:
        print("arguments are not lists")
    else:
        a = sort(l1)
        b = sort(l2)
        if compute == "subset":
            result = subset(substract_elements(a,b))
        elif compute == "union":
            result = l1 + l2
            print("the union is: ",result)
        elif compute == "intersection":
            result = substract_elements(a,b)[0]
            print("the intersection is: ",result)
        elif compute == "complement":
            result = substract_elements(a,b)[1]
            #result = substract_elements(a,b)[2]
            print("the complement is: ", result)
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
    print([common_elements,copy_big,copy_small,big,small])
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
    elif l3[0] != []:
        print("the sets have the elements in common, but they are neither is a subset of each other")

def remove_repeats(l4):
    i = 0
    new_list = []
    len_list = len(l4)
    while i < len_list:
        if l4[i] not in new_list:
            new_list = new_list + [l4[i]]
        i = i + 1
    return new_list

def make_powerset(l5):
    power_set = []
    pick = 1
    number_of_elements = len(l5)
    while pick < number_of_elements:
        array_of_indices = pick * [0]
        if array_of_indices[0] and array_of_indices[-1] == number_of_elements:
            for i in array_of_indices:
                if i < number_of_elements:
                    i = i + 1
                else:
                    print("else condition of make_powerset")
        pick = pick + 1
    print(power_set)

#Create an array, with length elements.

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
main(a,c)
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
