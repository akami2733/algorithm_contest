n, q = map(int, input().split())
users = [['N' for _ in range(n)] for _ in range(n)]

def process(opt, u1, *u2):
    u1 -= 1
    if opt == 1:
        u2 = u2[0] - 1
        users[u1][u2] = 'Y'
    elif opt == 2:
        for i in range(n):
            if users[i][u1] == 'Y':
                users[u1][i] = 'Y'
    elif opt == 3:
        tmp = []
        for i in range(n):
            if i != u1 and users[u1][i] == 'Y':
                tmp += [i]
        for i in tmp:
            for j in range(n):
                if j != u1 and users[i][j] == 'Y':
                    users[u1][j] = 'Y'

for i in range(q):
    process(*map(int, input().split()))

for i in range(len(users)):
    print(''.join(users[i]))