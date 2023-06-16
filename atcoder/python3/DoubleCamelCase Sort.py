S = input()
wl = []
word = ''
for c in S:
    word += c
    if c.isupper():
        if len(word) > 1:
            wl += [word]
            word = ''
wl = sorted(wl, key=str.lower)
print(''.join(wl))