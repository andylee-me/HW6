e = []
f = open("compitition.txt", "r")
line = f.readlines()
f.close()
import re
digitals = re.compile(r'\d+', re.I)
for i in line:
    a = re.findall(digitals, i)
    a.remove(max(a))
    a.remove(min(a))
    a = list(map(int, a))
    import statistics
    a = statistics.mean(a)
    e.append(str(a))
    winner = max(e)
line1 = list(line[0])
line2 = list(line[1])
line3 = list(line[2])
StrA = "".join(line1)
StrA = StrA.replace("\n","")
strb = "".join(line2)
strb = strb.replace("\n","")
Strc = "".join(line3)
for i in range(0,3):
    l = ["Mary","John","Amy"]
    if e[i] == winner:
        v = i
        winner = l[i]
print(StrA,"平均:",e[0],strb,"平均:",e[1],Strc,"平均:",e[2],"\n","winner:",winner)
