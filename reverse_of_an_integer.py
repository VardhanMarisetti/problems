# Reverse of an integer - optimized

X = int(input())
RNum = 0
if X < 0:
  X = X * -1
  Sign = -1
else:
  Sign = 1
while X != 0:
  RNum = RNum * 10 + int(X % 10)
  X = int(X/10)
print(RNum * Sign)
