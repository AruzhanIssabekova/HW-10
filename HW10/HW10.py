# n=list(map(int,input().split()))
# d={i:i**3 for i in n}
# print(d)

# n=list(map(int,input().split()))
# d=[]
# for i in n:
#     if i not in d:
#         d.append(i)
# print(d)

# d=[i for i in range(0, 100, 10)]
# print(d)

# def das(m):
#     for t in m:
#         if t % 7 == 0:
#             yield t
# n=int(input())
# m=[i for i in range(1,n)]
# das(m)
# for i in das(m):
#     print(i, end=' ')

from itertools import permutations
s=list(input())
d=[]
for i in s:
    if i.isalpha():
        d.append(i)
print(d)
for j in range(len(d)+1):
    for i in permutations(d,j):
        print(''.join(i))