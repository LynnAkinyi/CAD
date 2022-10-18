L1 = list()
L2 = list()
for i in range(8):
    x = eval(input("Enter a number at:"+str(i)+"\n"))
    L1.append(x)
    print("The total is: ",sum(L1))
    print("The length is: ",len(L1))
    print("The lowest score is:", min(L1))
    print("The highest score is: ", max(L1))
    print("The average score is: ", sum(L1)/len(L1))
    avg = sum(L1)/len(L1)
    
for j in range(len(L1)):      
    if L1[j]>=0 and L1[j]<=39:
        L2.append("D")
    elif L1[j]>=40 and L1[j]<=49:
        L2.append("D")
    elif L1[j]>=40 and L1[j]<=49:
        L2.append("C")
    elif L1[j]>=40 and L1[j]<=49:
        L2.append("B")
    elif L1[j]>=40 and L1[j]<=49:
        L2.append("A")

    else:
        print("Invalid!")
print("score\t grade")
for k in range(len(L1)):
    print(L1[k],"\t",L2[k])
   
