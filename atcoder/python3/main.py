s = input()

index = 0
d = {}

def range_char(start, stop):
    return (chr(n) for n in range(ord(start), ord(stop) + 1))

for c in range_char('a', 'z'):
    d[c] = 0

def is_number(c):
    return c >= '0' and c <= '9'

def is_opening(c):
    return c == '('

def is_closing(c):
    return c == ')'

def process_number(s):
    global index
    num = ''
    while is_number(s[index]):
        num += s[index]
        index += 1
    return int(num)

def insert_char(c, val):
    d[c] += val

def process(prefix_number):
    global index
    local_prefix = prefix_number
    while index < len(s):
        if is_number(s[index]):
            local_prefix *= process_number(s)
        elif is_opening(s[index]):
            index += 1
            process(local_prefix)
            local_prefix = prefix_number
        elif is_closing(s[index]):
            index += 1
            break
        else:
            insert_char(s[index], local_prefix)
            local_prefix = prefix_number
            index += 1

def main():
    process(1)
    for (k, v) in d.items():
        print('{0} {1}'.format(k, v))

main()
