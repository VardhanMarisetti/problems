# Happy number

Number = input("Enter a number: ")
Print = Number
Red = set ()
while Number != "1":
  Next = 0
  for i in range(len(Number)):
    Next += int(Number[i]) ** 2
  Number = str(Next)
  if Number in Red:
    break
  else:
    Red.add(Number)
if int(Number) == 1:
  print(f"{Print} is a happy number")
else:
  print(f"{Print} is not a happy number")
