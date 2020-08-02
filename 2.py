n=int(input())
a = input()
ele = list(map(int,a.split()))
ele.sort()
for i in range(n-1,-1,-1):
    if ele[n-1]==ele[i]:
        continue
    elif ele[n-1]!=ele[i]:
        print(int(ele[i]))
        break
