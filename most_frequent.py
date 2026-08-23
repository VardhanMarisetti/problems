# Most frequent number - Dictionary - optimized

nums = [1, 5, 7, 7, 7, 7, 7, 4, 9, 5, 3, 3, 3, 3, 5, 8, 9, 9, 5, 9, 9]
freq = {}
for num in nums:
  if num in freq:
    freq[num] += 1
  elif num not in freq:
    freq[num] = 1
high = 0
for value in freq.values():
  if value > high:
    high = value
for num in freq:
  if freq[num] == high:
    print(num, end = " ")
