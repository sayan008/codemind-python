x=int(input())
for i in range(x):
    n=int(input())
    l=list(map(int,input().split()))
    k=sorted(l)
    if l ==k:
        print("0")
    else:
        print(k[-1]-k[0])