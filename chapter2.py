from chapter1 import *

def cartesian_product(a,b):
    i = 0
    product = []
    while i < len(a):
        j = 0
        while j < len(b):
            add = [a[i], b[j]]
            j = j + 1
            product = product + [add]
        i = i + 1
    return product

def is_mapping(domain_codomain_pair):
    i = 0
    while i < len(f):
        stored_domain = domain_codomain_pair[i][0]
        stored_codomain = domain_codomain_pair[i][1]
        j = 1
        while j < len(f) - 1:
            stored_domain2 = domain_codomain_pair[j][0]
            stored_codomain2 = domain_codomain_pair[j][1]
            j = j + 1
            if stored_domain == stored_domain2 and stored_codomain != stored_codomain2:
                return False
        i = i + 1
    return True

def map_function(function, domain):
    mapped = []
    i = 0
    while i < len(domain):
        mapped = mapped + [function(domain[i])]
        i = i + 1
    return mapped

def is_surjective(function, domain, codomain):
    mapped = map_function(function,domain)
    result = main(mapped,codomain, "subset")
    if result == domain or result == "equal":
        return True
    else:
        return False

def is_injective(function, domain):
    domain_without_repeats = remove_repeats(domain)
    mapped = remove_repeats(map_function(function,domain))
    if len(mapped) != len(domain_without_repeats):
        return False
    else: 
        return True

def f(x):
    return x*x

def is_bijective(function, domain, codomain):
    condition1 = is_injective(function,domain)
    condition2 = is_surjective(function,domain,codomain)
    if condition1 == True and condition == True:
        return True
    else:
        return False

def is_image(function,domain,codomain):
    return is_surjective(function,domain,codomain)

def is_inverse(function,domain,codomain):
    return is_surjective(function,codomain,domain)


