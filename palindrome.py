a = 'abc'
b = 'cba'

def reverse(string):
    return string[::-1]

def is_palindrom(s,s1):
    s1 = reverse(s1)
    if s == s1:
        return True
    else:
        return False

results = is_pail(a, b)

print(results)
