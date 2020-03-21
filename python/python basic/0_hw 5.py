from cmath import inf

def procedureF(k, A):
    """Given n numbers a1; :::; an s.t. 0  ai < 2K for all i. There must exist a number
        X s.t. max1in (ai  X) is minimum, where  is bitwise XOR operation."""

    t = 2**(k-1)
    B = []
    C = []

    for i in A:
        if i & t > 0 :      B.append(i)
        else:               C.append(i)

    if k == 1:
        if B == None or C == None:  return 0
        else:                       return 1

    if B is not None:   AnsB = procedureF(k-1, B)
    else:               AnsB = float(inf)
    # print(AnsB)

    if C is not None:   AnsC = procedureF(k-1, C)
    else:               AnsC = float(inf)
    # print(AnsC)

    if B is None or C is None:  return min(AnsB, AnsC)
    else: return t + min(AnsB, AnsC)


k = 3
A = [5, 2, 1, 1]
print(procedureF(k, A))