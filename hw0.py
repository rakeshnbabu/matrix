# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [x for x in L if x%num != 0]



## Problem 2
def myLists(L): return [list(range(1,x+1)) for x in L]



## Problem 3
def myFunctionComposition(f, g): return {a:d for (a,b) in f.items() for (c,d) in g.items() if b==c}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = .001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    sum = 0
    for i in L:
        sum += i
    return sum

## Problem 7
def myProduct(L):
    sum = 1
    for i in L:
        sum *= i
    return sum

## Problem 8
def myMin(L):
    retMin = L.pop()
    for i in L:
        retMin = i if i < retMin else retMin
    return retMin

## Problem 9
def myConcat(L):
    retStr = ""
    for i in L:
        retStr += i
    return retStr


## Problem 10
def myUnion(L):
    retSet = set()
    for i in L:
        retSet = retSet.union(i)
    return retSet

