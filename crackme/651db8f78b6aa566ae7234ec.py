def check_2_1(x):
    if x <= 1:
        return 0
    for i in range(2, x//2):
        if not x % i:
            return 0
    return 1


def get_str(i):
    for i1 in range(ord('a'), ord('z')):
        for i2 in range(ord('a'), ord('z')):
            for i3 in range(ord('a'), ord('z')):
                for i4 in range(ord('a'), ord('z')):
                    if i1+i2+i3+i4 == i:
                        return f'{chr(i1)}{chr(i2)}{chr(i3)}{chr(i4)}'


key = []
for i in range(ord('a')*4, ord('z')*4):
    if check_2_1(i) == 1:
        k = get_str(i)
        if k is not None:
            key.append(k)
            if len(key) > 4:
                key = key[1:]
                print(f'{key[0]}-{key[1]}-{key[2]}-{key[3]}')
