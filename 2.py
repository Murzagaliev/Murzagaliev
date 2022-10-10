print("Введите 3 числа")

a = int(input())
b = int(input())
c = int(input())

Discriminant = int( (b*b)-(4*a*c))

if (Discriminant == 0) or (Discriminant > 0):
    print("Да")
  
elif(Discriminant < 0):
    print("Нет")
