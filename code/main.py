import os
import random

from structure import solution, instance
from constructives import greedy, cgrasp
from localsearch import lsfirstimprove
from algorithms import grasp
import datetime

def executeInstance():
    random.seed(1309)
    path = "instances/preliminar/MDG-a_1_100_m10.txt"
    inst = instance.readInstance(path)
    sol = grasp.execute(inst, 100, -1)
    solution.printSol(sol)

def executeDir():
    dir = "instances/preliminar"
    with os.scandir(dir) as files:
        ficheros = [file.name for file in files if file.is_file() and file.name.endswith(".txt")]
    with open("resultados.csv", "w") as results:
        for f in ficheros:
            path = dir+"/"+f
            print("Solving "+f+": ", end="")
            inst = instance.readInstance(path)
            results.write(f+"\t"+str(inst['n'])+"\t")
            start = datetime.datetime.now()
            sol = grasp.execute(inst, 100, -1)
            elapsed = datetime.datetime.now() - start
            secs = round(elapsed.total_seconds(),2)
            print(str(sol['of'])+"\t"+str(secs))
            results.write(str(round(sol['of'],2))+"\t" + str(secs) + "\n")


if __name__ == '__main__':
    #executeInstance()
    executeDir()