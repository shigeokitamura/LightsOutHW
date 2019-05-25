import sys
import numpy as np

H, W = map(int, input().split())

s = np.zeros((H + 2, W + 2))
#print(s)

for h in range(H):
    line = input().split()
    
    for w in range(W):
        if line[w] == 'O':
            s[h + 1][w + 1] = 1
        elif line[w] == '.':
            s[h + 1][w + 1] = -1
#print(s)

# H < W なら，計算量を減らすために転置
if H < W:
    ns = np.zeros((W + 2, H + 2))
    for h in range(H):
        for w in range(W):
            ns[w + 1][h + 1] = s[h + 1][w + 1]
    tmp = H
    H = W
    W = tmp
    s = ns

def sim(_s, _i):
    count = 0
    for h in range(1, H + 1):
        #print(count)
        # 上段の消し方を全通り試す
        for w in range(1, W + 1):
            if (h == 1 and ((_i >> (w - 1)) & 1) == 1) or (h > 1 and _s[h - 1][w] == 1):
                _s[h - 1][w] = -_s[h - 1][w]
                _s[h + 1][w] = -_s[h + 1][w]
                _s[h][w - 1] = -_s[h][w - 1]
                _s[h][w + 1] = -_s[h][w + 1]
                _s[h][w]     = -_s[h][w]
                count += 1
    #print(_s)
    for w in range(1, W + 1):
        if _s[H][w] == 1:
            return sys.maxsize
    #print(count)
    return count

ret = sys.maxsize

for i in range(1 << W):
    now = np.zeros((H + 2, W + 2))
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            now[h][w] = s[h][w]
    ret = min(ret, sim(now, i))
    #print(ret)
print(ret)

