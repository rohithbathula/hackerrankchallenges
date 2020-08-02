sum=0
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
l=student_marks[query_name]
for i in range(len(l)):
    sum=sum+l[i]
avg=sum/3
final_avg= "{:.2f}".format(avg)
print(final_avg)
