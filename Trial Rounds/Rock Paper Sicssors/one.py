#doesnt pass all cases

r1, s1, p1 = map(int, input().split())
r2, s2, p2 = map(int, input().split())
 
lossCount = min(r1, s2) + min(s1, p2) + min(p1, r2)
 
print(lossCount)
