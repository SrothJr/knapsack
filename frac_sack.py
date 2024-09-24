def frac_sack(arr, w):
    ratio = {}
    p = 0
    for i in arr:
        ratio[i[0]/i[1]] = i

    for i in sorted(ratio, reverse=True):
        if w >= ratio[i][1]:
            w -= ratio[i][1]
            p += ratio[i][0]
        else:
            p += (ratio[i][0] * w)/ratio[i][1]
            w = 0
            break    

    return p

arr = [[40,10],[100, 20],[120, 30]]
w = 50
print(frac_sack(arr, w))
