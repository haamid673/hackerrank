if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
a=set(arr)
first=max(a)
a.remove(first)
print(max(a))