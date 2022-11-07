from structure import solution, instance
from constructives import cgrasp
from localsearch import lsfirstimprove, lsbestimprove


def execute(inst, iters, alpha):
    best = None
    for i in range(iters):
        print("IT " + str(i + 1))
        sol = cgrasp.construct(inst, alpha)
        print("\tC: "+str(sol['of']))
        # lsfirstimprove.improve(sol)
        lsbestimprove.improve(sol)
        print("\tLS: " + str(sol['of']))
        if best is None or best['of'] < sol['of']:
            best = sol
        print("\tB: " + str(best['of']))
    return best