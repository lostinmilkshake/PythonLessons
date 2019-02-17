
def search(inf, errors):
    if classDict.get(inf) != None:
        for j in range(len(classDict[inf])):
            if errors.count(classDict[inf][j]) > 0:
                answer = True
                return answer
            else:
                answer = search(classDict[inf][j], errors) 
                if answer:
                    return answer 
        answer = False
        return False

#TODO ДОДЕЛАТЬ, ДЕБИЛ
classDict = {}
amount = int(input())
for i in range(amount):
    name = list(input().split())
    if classDict.get(name[0]) != None:
        classDict[name[0]] += name[2:]
    else:
        classDict[name[0]] = name[2:]
#print(classDict)

errors = []
amount = int(input())
for i in range(amount):
    inf = input()
    errors.append(inf)
    answer = search(inf, errors)
    if answer:
        print(inf)

'''
# Правильное решение
n = int(input())
classes = {}
for i in range(n):
    line = input()
    parts = line.split(" : ")
    cls = parts[0]
    if len(parts) == 1:
        classes[cls] = []
    else:
        classes[cls] = parts[1].split(" ")


def check(src, dest):
    if src == dest:
        return True
    return any([check(child, dest) for child in classes[src]])


m = int(input())
used = []

for i in range(m):
    cls = input()
    if any([check(cls, used_one) for used_one in used]):
        print(cls)
    used.append(cls)
'''