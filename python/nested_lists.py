n=int(input())
records=[]
for i in range(n):
    name=input()
    score=float(input())
    records.append([name,score])
scorelist=[]
for item in records:
    scorelist.append(item[1])

secondlow=sorted(set(scorelist))[1]


names=[]
  
for i in records:
    if i[1]==secondlow:
        names.append(i[0])
        
names.sort()

for name in names:
    print(name)