import os
import os.path

dires= []
inp = open("test.txt", "w")
for currentDir, dirs, files in os.walk("."):
        for i in files:
                if i.endswith(".py"): 
                        dires.append(currentDir[2:]+"\n")
                        break
dires.sort()
for i in dires:
        inp.write(i)
inp.close()