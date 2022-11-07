from structure import solution


def construct(inst):
    sol = solution.createEmptySolution(inst)
    u, v = findLargestDistance(inst)
    solution.addToSolution(sol, u)
    solution.addToSolution(sol, v)
    cl, pos = createCandidateList(sol)
    while not solution.isFeasible(sol):
        c = cl[pos][0]
        d = cl[pos][1]
        solution.addToSolution(sol, c, d)
        del cl[pos]
        pos = updateCandidateList(sol, cl, c)
    return sol


def findLargestDistance(inst):
    n = inst['n']
    best1 = -1
    best2 = -1
    largest = 0
    for i in range(n):
        for j in range(i+1, n):
            if inst['d'][i][j] > largest:
                best1 = i
                best2 = j
                largest = inst['d'][i][j]
    return best1, best2


def createCandidateList(sol):
    n = sol['instance']['n']
    cl = []
    largest = 0
    bestIndex = 0
    for c in range(n):
        if not solution.contains(sol, c):
            d = solution.distanceToSolution(sol, c)
            cl.append([c, d])
            if d > largest:
                largest = d
                bestIndex = len(cl)-1
    return cl, bestIndex

def updateCandidateList(sol, cl, added):
    bestIndex = 0
    largest = 0
    for i in range(len(cl)):
        c = cl[i]
        c[1] += sol['instance']['d'][added][c[0]]
        if c[1] > largest:
            bestIndex = i
            largest = c[1]
    return bestIndex