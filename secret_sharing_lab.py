# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec
from independence import is_independent
from vec import Vec
from itertools import combinations


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    uFound = False
    u = list2vec([0,0,0,0,0,0])
    while not uFound:
        u = list2vec([randGF2() for i in range(6)])
        if a0*u == s and b0*u == t:
            uFound = True
    return u


## Problem 2
# Give each vector as a Vec instance
secret_a0 = a0
secret_b0 = b0
secret_a1 = Vec(a0.D, {})
secret_b1 = Vec(a0.D, {})
secret_a2 = Vec(a0.D, {}) 
secret_b2 = Vec(a0.D, {}) 
secret_a3 = Vec(a0.D, {}) 
secret_b3 = Vec(a0.D, {}) 
secret_a4 = Vec(a0.D, {}) 
secret_b4 = Vec(a0.D, {}) 

vecList = [(secret_a1, secret_b1), (secret_a2, secret_b2), (secret_a3, secret_b3), (secret_a4, secret_b4)] 
imVecs = [(secret_a0, secret_b0)]
notFound = True
while notFound:
    for vecPair in vecList:
        for vec in vecPair:
            for i in range(6):
                vec[i] = randGF2()
    if all(is_independent(list(sum(x,()))) for x in combinations(vecList +imVecs,3)):
        notFound = False
