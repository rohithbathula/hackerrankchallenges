from collections import namedtuple
Student= namedtuple('Students',' ID MARKS CLASS NAME')
n=int(input())
data=input().split()
for i in range(n):
    if data[i]=='MARKS':
        x=i
        break
sum=0
for j in range(n):
    var=input().split()
    sum=sum+int(var[x])
avg=sum/n
final_avg= "{:.2f}".format(avg)
print(final_avg)
