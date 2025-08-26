n1=int(input())
s1=set()
s2=set()
for i in range(n1):
    s1.add(int(input()))
n2=int(input())
for i in range(n2):
    s2.add(int(input()))
s3=s1.union(s2)
print(len(s3))
