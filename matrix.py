

def transpose(M):
    if M == []: return M
    Mt = []
    for row in range(len(M[0])):
        Mt.append(list())
    for row in range(len(Mt)):
        for col in range(len(M)):
            Mt[row].append(M[col][row])
    return Mt


def powers(num_list, min, max):
    rM = []
    for idx, num in enumerate(num_list):
        rM.append(list())
        for power in range(min, max+1):
            rM[idx].append(num**power)
    return rM


def matmul(M1, M2):
    if M1 == [] and M2 == []: return []
    n1, m1 = len(M1), len(M1[0])
    n2, m2 = len(M2), len(M2[0])
    M2 = transpose(M2)
    Mm = []
    
    def vecmul(v1, v2):
        vsum = 0
        for e1, e2 in zip(v1,v2):
            vsum += e1*e2
        return vsum
    
    for n in range(n1):
        Mm.append(list())
        for m in range(m2):
            Mm[n].append(vecmul(M1[n],M2[m]))
    return Mm


def invert(M):
    a,b,c,d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a*d - b*c
    Mi = [[d/det, -b/det],
          [-c/det, a/det]]
    return Mi
    

def loadtxt(filename):
    with open(filename) as file:
        M = []
        data = file.readlines(1)[0].split()
        while data != None and data != []:
            M.append(data)
            data = file.readlines(1)
            if data != None and data != []:
                data = data[0].split()
            else: break
        
        for row in range(len(M)):
            for col in range(len(M[0])):
                M[row][col] = float(M[row][col])
        return M
