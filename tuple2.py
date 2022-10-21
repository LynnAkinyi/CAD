L = list()
t2 = tuple()
t1 = tuple()
N = int(input("Enter population size\n"))
for i in range(N):
    x = eval(input("Enter a score at"+str(i)+"\n"))
    L.append(x)
    t1 = tuple(L)
    t2 = t2+(L[i]**2) 

print("Value sorted",sorted(t1))
print("Value squared",t2)
print("The third value",t1[2])
print("Average",sum(t1)/len(t1))

t3 = tuple()
for i in range(len(t1)):
    if t1[i] not in t3:
        t3 = t3+(t1[i],)
print("Tuple without duplicates",t3)


















     
