# Largest sum of the substring - optimized

nums = [1, 2, 3, -4, 5]
sum = 0
high = float('-inf')
for num in nums:
  sum += num
  if sum > high:
    high = sum
  if sum < 0:
    sum = 0
print(high)
