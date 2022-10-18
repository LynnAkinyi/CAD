P1 = []
P2 = []
P3 = []
result = []
P4 = []

N = eval(input("Enter the number of elements you need\n"))
for i in range(N):
    x = eval(input("Enter an element at:"+str(i)+"\n"))
    P1.append(x)
    P2.append((P1[i]*P1[i]))
    print("List: ",P1)
    print("Square elements: ",P2)
    if P1[i]%5==0:
        P3.append(P1[i])
    else:
        pass
print("List: ",P1)
print("List: ",P2)
print("Divisible by 5",P3)
 
for i in P1: 
    if i not in result: 
        result.append(i) 


print ("The list after removing duplicates : " + str(result))
if P1[i]%2==0:
        P4.append(P1[i])
else:
        pass
print("Divisible by 2",P4)
