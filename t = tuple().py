t = tuple()
N = int(input("Enter population size:\n"))
for i in range(N):
    x = eval(input("Enter a score at:"+str(i)+"\n"))
    t = t+(x,)
    print("Total score=",sum(t))
    print("Population size=",len(t))
    print("Highest=",max(t),"lowest=",min(t))
    print("Average=",sum(t)/(len(t)))
    
z = 0
u =  sum(t)/len(t)
for i in range(len(t)):
    z = z+(t[i]-u)*(t[i]-u)
var = z/N
print("var",var)
sd =(var)**(1/2)
print("sd",sd)
