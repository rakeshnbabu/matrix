from orthogonalization import orthogonalize
from orthogonalization import aug_orthogonalize
import matutil as mu
from math import sqrt

def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    orthoL = orthogonalize(L)
    normL = [sqrt(li*li) for li in orthoL]
    return [li/ni for li,ni in zip(orthoL, normL)]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    orthoL,retR = aug_orthogonalize(L)
    normL = [sqrt(li*li) for li in orthoL]
    orthoL = [li/ni for li,ni in zip(orthoL, normL)]
    for i in range(len(normL)):
        for iVec in retR:
            iVec[i] = normL[i]*iVec[i]
    return (orthoL, retR)
