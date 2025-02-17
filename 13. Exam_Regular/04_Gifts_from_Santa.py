N = int(input())
M = int(input())
S = int(input())
flag = False

for address in range(M, N - 1, -1):
    if address % 2 == 0 and address % 3 == 0:
        if address == S:
            flag = True
            break
        if flag:
            print(' ', end='')
        print(address, end='')
        flag = True
