
#unoptimzed solution

def cal_danger(heights, changes):
    total_danger = 0
    for height in heights:
        if height < 0:
            danger = -height
        elif height == 0:
            danger = 0
        else:
            danger = height
        total_danger += danger
 
    for x in changes:
        new_heights = [h + x for h in heights]
        new_danger = 0
        for height in new_heights:
            if height < 0:
                new_danger += -height
            elif height == 0:
                new_danger += 0
            else:
                new_danger += height
        print(new_danger)
        heights = new_heights
 
 
n = int(input())
heights = list(map(int, input().split()))
k = int(input())
changes = list(map(int, input().split()))
cal_danger(heights, changes)
