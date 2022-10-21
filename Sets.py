S1 = set()
S2 = set()
N1 = eval(input("Enter the number of elements in the first set\n"))
N2 = eval(input("Enter the number of elemnts in the second set\n"))

for i in range(N1):
    x = int(input("Enter elemnt at"+str(i)+"first set\n"))
    S1.add(x)
    

for i in range(N2):
    y = int(input("Enter elements at"+str(i)+"second set\n"))
    S2.add(y)
    
print("Elements in the first set\n",S1.difference(S2))
print("Elements in the second set\n",S2.difference(S1))
print("Common elements",S1.intersection(S2))
print("Elements on both sets\n",S1,S2)

