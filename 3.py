k=[]
for _ in range(int(input())):
    l=[]
    name = input()
    l.append(name)
    score = float(input())
    l.append(score)
    k.append(l)
m=[]
for i in range(len(k)):
    value=k[i][1]
    m.append(value)
m.sort()
for j in range(len(m)-1):
    if m[j]==m[j+1]:
        continue
    elif m[j]!=m[j+1]:
         store=m[j+1]
         break
z=[]
for _ in range(len(k)):
    if k[_][1]==store:
        z.append(k[_][0])
z.sort()
for y in range(len(z)):
    print(z[y])
   
