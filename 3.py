import math
print("Введите число")
Number = int(input())
x = [int(a) for a in str(Number)]
if(Number%3 == 0):
  print("Число делится на 3 и сумма чисел равняется= ", sum(x))
elif(Number%3!= 0):
  print("Число не делится на 3 и произведение чисел равняется= ", math.prod(x))
