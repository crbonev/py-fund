di = {}
words = input().split()
for w in words:
    w = w.lower()
    if w not in di:
        di[w] = 1
    else:
        di[w] += 1
for w in di:
    if di[w] % 2 != 0:
        print(w, end=' ')