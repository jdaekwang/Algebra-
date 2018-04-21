#main is the main program:
#treats lists as multisets, you can use remove_repeats to get rid of repeating elements
#the empty list "[]" is considered as the empty set and it is the subset of all lists
#input must be a list
#elements of the list must be able to be comparable, i.e. <, > must make sense


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
        

def main(l1,l2, compute):
    if type(l1) and type(l2) != list:
        print("arguments are not lists")
    else:
        a = sort(l1)
        b = sort(l2)
        if compute == "subset":
            result = is_subset(a,b)
        elif compute == "union":
            result = l1 + l2
        elif compute == "intersection":
            result = find_common(l1,l2)
        elif compute == "complement":
            result = complement(l1,l2)
        return result


def larger_or_equal(l1,l2):
    if len(l1) > len(l2):
        return l1
    elif len(l2) > len(l1):
        return l2
    elif len(l2) == len(l1):
        return "equal"
    else:
        print("Error")

def find_common(l1,l2):
    common_elements1 = []
    common_elements2 = []
    i = 0
    j = 0
    while i < len(l1):
        if l1[i] in l2:
            common_elements1 = common_elements1 + [l1[i]]
        i = i + 1
    while j < len(l2):
        if l2[j] in l1:
            common_elements2 = common_elements2 + [l2[j]]
        j = j + 1
    if len(common_elements1) < len(common_elements2):
        return common_elements1
    else:
        return common_elements2

def complement(l1,l2):
    i = 0
    l1_minus_l2 = l1[:]
    l2_minus_l1 = l2[:]
    while i < len(l1_minus_l2):
        j = 0
        while j < len(l2_minus_l1):
            if l1_minus_l2[i] == l2_minus_l1[j]:
                l1_minus_l2[i] = "deleted"
                l2_minus_l1[j] = "deleted"
            j = j + 1
        i = i + 1
    l1_minus_l2_final = []
    l2_minus_l1_final = []
    for i in l1_minus_l2:
        if i != "deleted":
            l1_minus_l2_final = l1_minus_l2_final + [i]
    for j in l2_minus_l1:
        if j != "deleted":
            l2_minus_l1_final = l2_minus_l1_final + [j]
    return [l1_minus_l2_final, l2_minus_l1_final]


def is_subset(l1,l2):
    common = find_common(l1,l2)
    print(common)
    if common == l1 and common == l2: 
        return "equal"
    elif common == l1:
        return l1
    elif common == l2:
        return l2
    elif common == []:
        return "disjoint"
    else:
        return "common elements"

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

compute = "subset"

main(a,d, compute)
main(a,b, compute)
main(a,c, compute)
main(a,h, compute)
main(e,f, compute)
main(g,f, compute)
main(f,g, compute)
main(a,i, compute)
main(e,j, compute)
main(a,g, compute)
main(k,g, compute)
main(k,f, compute)
main(a,l, compute)
