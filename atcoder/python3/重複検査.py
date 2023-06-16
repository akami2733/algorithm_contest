N = int(input())
s = set([i for i in range(1, N + 1)])
for n in range(N):
    v = int(input())
    if v in s:
        s.remove(v)
    else:
        ans = v
if 'ans' in locals():
    print('{0} {1}'.format(ans, s.pop()))
else:
    print('Correct')