a = 'aabcccccaaa'

def count_compression(S):
    l = len(S)
    S += ' '
    S1 = ''
    count = 0
    for i in range(l):
        if i < l:
            c = S[i]
            c2 = S[i+1]
            if c == c2:
                count += 1
            else:
                count += 1
                S1 += c
                S1 += str(count)
                count = 0
    return S1


print(count_compression(a))
