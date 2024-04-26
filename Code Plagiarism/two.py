def check_string(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i += 2
    return i == len(s) and j == len(t)
 
 
def check_string2(s, t):
    i = 0
    for c in t:
        if i >= len(s):
            return False
        while s[i] != c:
            i += 2
            if i >= len(s):
                return False
        i += 1
    return True
 
 
s = input().strip()
t = input().strip()
 
if check_string2(s, t):
    print('YES')
else:
    print('NO')
