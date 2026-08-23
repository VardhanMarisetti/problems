# Nth highest integer without sort()

num = [-748, -12, -637, -32, -445, -7894, -9020]
order = []
n = int(input("Nth number: "))
for j in range(n):
  high = num[0]
  for i in num:
    if i > high:
      high = i
  num.remove(high)
print(high)
