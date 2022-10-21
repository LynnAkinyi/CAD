k = list()
v = list()
d = dict()
N = eval(input("Enter Number of student\n"))

for i in range(0,N):
    x =  input("Enter a key at"+str(i)+"\n")
    k.append(x)

for i in range(0,N):
    y =  input("Enter a value at"+str(i)+"\n")
    v.append(y)

d = dict(zip(k,v))
print("student number",d.keys)
print("student name",d.values)
print("RegNo\t Full Name")

for k,v in d.items():
    print(k,"\t",y)
