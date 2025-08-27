n = int(input())
s = set(map(int, input().split()))
n1=int(input())
s1=[input().split() for _ in range(n1)]

for cmd in s1:
    if cmd[0]=='pop':
        s.pop()
    elif cmd[0]=='discard':
        s.discard(int(cmd[1]))
    elif cmd[0]=='remove':
        s.remove(int(cmd[1]))
print(s)
print(sum(s))