import random

from structure import solution

def improve(sol):
    improve = True
    while improve:
        improve = tryImprove(sol)


def tryImprove(sol):
    sel, ofVarSel, unSel, ofVarUnsel = selectInterchange(sol)
    if ofVarSel < ofVarUnsel:
        solution.removeFromSolution(sol, sel, ofVarSel)
        solution.addToSolution(sol, unSel, ofVarUnsel)
        return True
    return False


def selectInterchange(sol):
    n = sol['instance']['n']
    sel = -1
    bestSel = 0x3f3f3f3f
    unsel = -1
    bestUnsel = 0
    for v in sol['sol']:
        d = solution.distanceToSolution(sol, v)
        if d < bestSel:
            bestSel = d
            sel = v
    for v in range(n):
        if not solution.contains(sol, v):
            d = solution.distanceToSolution(sol, v, without=sel)
            if d > bestUnsel:
                bestUnsel = d
                unsel = v
    return sel, bestSel, unsel, bestUnsel

