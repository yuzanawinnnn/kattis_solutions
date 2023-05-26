n = int(input())

for i in range(n):
    b, p = input().split(" ")
    b = int(b)
    p = float(p)
    
    bpm = 60*b / p
    variance = 60 / p
    
    min_bpm = bpm - variance
    max_bpm = bpm + variance
    
    print("{:.4f}".format(min_bpm), "{:.4f}".format(bpm), "{:.4f}".format(max_bpm))
