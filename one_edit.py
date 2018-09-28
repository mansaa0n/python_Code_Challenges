a = 'pl'
b = 'pal'

def is_one_edit(S1, S2):
    one_ed = 0
    l1 = len(S1)
    l2 = len(S2)
    if l1 == l2 or l1 -1 == l2 or l1 == l2 -1:
        for c in S1:
            if c in S2:
                c1 = S1.find(c)
                c2 = S2.find(c)
                if c1 != c2:
                    one_ed += 1
            else:
                one_ed += 1
        if one_ed > 1:
            return False
        else:
            return True
    else:
        return False

cc = is_one_edit(a, b)
print(cc)
