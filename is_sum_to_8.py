a = [1, 2, 3, 4, 5]

def is_sum_to_8(IN):
    Temp = []
    for n in IN:
        comp = 8 - n
        if comp in Temp:
            print(comp)
            return True
        else:
            Temp.append(n)
return False

print(is_sum_to_8(a))
