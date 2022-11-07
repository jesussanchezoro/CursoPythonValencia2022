from structure import solution, instance
import random

def construct(inst, alpha):
    sol = solution.createEmptySolution(inst)
    n = inst['n']
    u = random.randint(0,n-1)
    solution.addToSolution(sol, u)
    cl = createCandidateList(sol, u)
    alpha = alpha if alpha >= 0 else random.random()
    while not solution.isFeasible(sol):
        gmin, gmax = evalGminGmax(cl)
        th = gmax - alpha * (gmax - gmin)
        rcl = []
        for i in range(len(cl)):
            if cl[i][0] >= th:
                rcl.append(cl[i])
        selIdx = random.randint(0, len(rcl)-1)
        cSel = rcl[selIdx]
        solution.addToSolution(sol, cSel[1], cSel[0])
        cl.remove(cSel)
        updateCandidateList(sol, cl, cSel[1])
    return sol


def createCandidateList(sol, first):
    n = sol['instance']['n']
    cl = []
    for c in range(n):
        if c != first:
            d = solution.distanceToSolution(sol, c)
            cl.append([d,c])
    return cl


def evalGminGmax(cl):
    gmin = 0x3f3f3f3f # Num. muy grande
    gmax = 0
    for c in cl:
        gmin = min(gmin, c[0])
        gmax = max(gmax, c[0])
    return gmin, gmax


def updateCandidateList(sol, cl, added):
    for i in range(len(cl)):
        c = cl[i]
        c[0] += sol['instance']['d'][added][c[1]]