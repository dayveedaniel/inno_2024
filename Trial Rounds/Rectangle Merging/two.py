#not accurate

def merge_rectangles(tup, merged):
    if not merged:
        merged.append(tup)
        return merged
 
    count = 0
    for a, b in merged:
        canA = tup[0] == a
        #print(f'canA {tup[0]} = {a} {canA}')
        canB = tup[1] == b
        #print(f'canb {tup[1]} = {b} {canB}')
        if canA and canB:
            merged[count] = (a, b + tup[1])
            merged.append((a + tup[0], b))
        elif canA:
            merged[count] = (a, b + tup[1])
        elif canB:
            merged[count] = (a + tup[0], b)
 
        count += 1
    return merged
 
 
def main():
    n = int(input())
    rectangles = []
    merged = []
 
    for _ in range(n):
        a, b = map(int, input().split())
        rectangles.append((a, b))
 
    for tup in rectangles:
        merged = merge_rectangles(tup, merged)
 
    if len(merged) == 1 and rectangles[0] == merged[0]: merged.clear()
 
    k = len(merged)
    print(k)
    for a, b in merged:
        print(a, b)
 
 
main()
