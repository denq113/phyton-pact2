print("Введите 3 - значное число")
numbers = int(input())
f = numbers % 10
u = numbers / 10
t = u % 10
r = u / 10
o = r % 10
if (numbers > 99 and numbers < 1000):
  if (f > t):
     if (t>o):
        print("Цифры записаны последовательно")
  else:
    print("Цифры не записаны последовательно")
else:
    print("Введино не 3 - значное число")