
def createEmptySolution(instance):
    solution = {}
    solution['sol'] = set()
    solution['of'] = 0
    solution['instance'] = instance
    return solution


def evaluate(sol):
    of = 0
    for s1 in sol['sol']:
        for s2 in sol['sol']:
            if s1 < s2:
                of += sol['instance']['d'][s1][s2]
    return of


def addToSolution(sol, u, ofVariation = -1):
    if ofVariation == -1:
        for s in sol['sol']:
            sol['of'] += sol['instance']['d'][u][s]
    else:
        sol['of'] += ofVariation
    sol['sol'].add(u)


def removeFromSolution(sol, u, ofVariation = -1):
    sol['sol'].remove(u)
    if ofVariation == -1:
        for s in sol['sol']:
            sol['of'] -= sol['instance']['d'][u][s]
    else:
        sol['of'] -= ofVariation


def contains(sol, u):
    return u in sol['sol']


def distanceToSolution(sol, u, without = -1):
    d = 0
    for s in sol['sol']:
        if s != without:
            d += sol['instance']['d'][s][u]
    return round(d, 2)

def isFeasible(sol):
    return len(sol['sol']) == sol['instance']['p']


def printSol(sol):
    print("SOL: "+str(sol['sol']))
    print("OF: "+str(round(sol['of'],2)))





