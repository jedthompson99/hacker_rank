if __name__ == '__main__':
    N = int(input())
L = []
for _ in range(N):
    line = input().split()
    if line[0] == 'print':
        print(L)
    else:
        getattr(L, line[0])(*map(int, line[1:]))


# insert
# print
# remove
# append
# sort
# pop
# reverse

# N = int(input())
# b = []
# for i in range(0, N):
#     a = input().split()
#     if(a[0] == 'insert'):
#         b.insert(int(a[1]), int(a[2]))
#     elif(a[0] == 'remove'):
#         b.remove(int(a[1]))
#     elif(a[0] == 'pop'):
#         b.pop()
#     elif(a[0] == 'print'):
#         print(b)
#     elif(a[0] == 'reverse'):
#         b.reverse()
#     elif(a[0] == 'append'):
#         b.append(int(a[1]))
#     elif(a[0] == 'sort'):
#         b.sort()
