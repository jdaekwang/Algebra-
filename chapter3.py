from chapter2 import *
from inspect import signature

def is_commutative(f_binary,domain):
    i = 0
    while i < len(domain):
        j = 0
        while j < len(domain):
            try1=f_binary(domain[i],domain[j])
            try2= f_binary(domain[j],domain[i])
            if try1 != try2:
                return False
            j = j + 1
        i = i + 1
    return True

def is_associative(f_binary,domain):
    i= 0 
    while i < len(domain):
        j = 0 
        while j < len(domain):
            k = 0
            while k < len(domain):
                try1 = f_binary(domain[i],f_binary(domain[j],domain[k]))

def is_binary(f):
    
