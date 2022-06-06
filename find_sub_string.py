t = 'данные'

S = set()  # unique symbols
M = len(t)  # number of symbols in word
d = {}  # dictionary to save shifts

for i in range(M - 2, -1, -1):  # iteration from second last
    if t[i] not in S:  # if the symbol not in set already
        d[t[i]] = M - i - 1
        S.add(t[i])

if t[M - 1] not in S:
    d[t[M - 1]] = M

d['*'] = M  # shift for else symbols

print(d)


test = 'етeоданные'

length = len(test)

if length >= M:
    i = M - 1   # counter for the checking element in string

    while i < length:
        k = 0
        flBreak = False
        for j in range(M - 1, -1, -1):
            if test[i - k] != t[j]:  # if our elements don't match
                if j == M - 1:  # shift if first element don't match
                    off = d[test[i]] if d.get(test[i], False) else d['*']
                else:  # shift if it not the last symbol
                    off = d[t[j]]

                i += off  # shift the counter of the string
                flBreak = True  # if symbols doesn't match, flBreak = True
                break  # terminate current process, next will start with a new values

            k += 1  # shift for comparing remaining elements

        if not flBreak:  # if we came to the end of substring, all letters matches
            print(f'Found the substring with index: {i - k + 1}')
            break
    else:
        print("The substring wasn't found in string")
else:
    print("The substring wasn't found in string")
