import random

from structure import solution

def improve(sol):
    improve = True
    while improve:
        improve = tryImprove(sol)


def tryImprove(sol):
    selected, unselected = createSelectedUnselected(sol)
    random.shuffle(selected)
    random.shuffle(unselected)
    for s in selected:
        ds = solution.distanceToSolution(sol, s)
        for u in unselected:
            du = solution.distanceToSolution(sol, u, s)
            if du > ds:
                solution.removeFromSolution(sol, s)
                solution.addToSolution(sol, u)
                return True
    return False


def createSelectedUnselected(sol):
    selected = []
    unselected = []
    n = sol['instance']['n']
    for v in range(n):
        if solution.contains(sol, v):
            selected.append(v)
        else:
            unselected.append(v)
    return selected, unselected

