B1 = set()
B2 = set()
N1 = eval(input("Enter the number of animals in the first gamepark\n"))
N2 = eval(input("Enter the number of animals in the second gamepark\n"))

for i in range(N1):
    x = str(input("Enter animal3 at"+str(i)+"first gamepark\n"))
    B1.add(x.lower())
    

for i in range(N2):
    y = str(input("Enter elements at"+str(i)+"second gamepark\n"))
    B2.add(y.lower())
    
print("Observation in first gamepark\n",B1.difference(B2))
print("Observation in second gameparkO\n",B2.difference(B1))
print("Common observation",B1.intersection(B2))
print("Observation in both gameparks\n",B1.unio(B2))

