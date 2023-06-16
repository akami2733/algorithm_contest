N = int(input())
p_v = int(input())
for n in range(N - 1):
    v = int(input())
    if v == p_v:
        print('stay')
    else:
        print('{0} {1}'.format('up' if v > p_v else 'down', abs(v - p_v)))
    p_v = v
