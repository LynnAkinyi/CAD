st="No\t"*4
print(st)
S="South Africa"
for i in range(len(S)):
    print(i,end=",")

rt="Hello"
print(len(rt))

ST="Desktop"
print(ST[2:5:2])

RT="culture."
print(RT[::-1])

N=input("Enter a word\n")
if N== N[::-1]:
    print(N,"is a palandrome")
else:
    print(N,"is not a palandrome")
