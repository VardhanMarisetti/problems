# 2nd highest integer - optimized

num = [748, 12, 637, 32, 445, 7894, 9020]
high = float('-inf')
s_high = float('-inf')
for i in num:
  if i > high:
    s_high = high
    high = i
  elif i > s_high and i != high:
    s_high = i
print(high)
print(s_high)
