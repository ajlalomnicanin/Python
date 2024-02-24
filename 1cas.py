import math

print("Hello Word")
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# promenljive u pythonu imaju type, name i value
#  count = 5
# count - name of variable
# 5 - value

x = 3
print(x)

x = "Tesla"
print(x)

# promenljive cuvaju neki tip podataka;
# broj,slovo,tekst,datum,slike...

# tipovi podataka u Pythonu;
# int - integer: 1, 2, 3, 4...
# float - floating-point number: 0.5, 3.56...
# str - text(string): "hello"...

x = 4
y = 3.14
h = "Tesla"

# Ulaz teksta...:
name = input("Unesite ime:")
print(name)

broj = int(input())
print(broj/4.2)

data = input()
num = float(data)

# Operacije - sabiranje mnozenje deljenje oduzimanje

broj = int(input())
print(broj*4.2)

#
name = "Ajla"
print("Hello" + name + "!")

# Zadaci
# Povrsina pravougaonika :
duzina = int(input())
sirina = int(input())

povrsina = duzina * sirina
print(povrsina)

# Pretvori ince u cm
inc = float(input("Unesite decimalni broj: "))
centimetar = inc * 2.54

print(centimetar)

# arithmetic operators *, /, //, %
a = 5
b = 6
product = a * b

a = 25
b = a / 4   # 6.25
c = a // 4  # 6
j = a % 4   # 25

# Interpolation - "f"

first_name = input()
last_name = input()
age = int(input())
town = input()
print(f"You are {first_name} {last_name}, a {age} -"
      f" years old person from {town}. ")

# Python uzima celu liniju koda, dok kod jave cita do prvog razmaka ako ne kazemo....

x = float(input())

print(math.sqrt(x))

print(math.sin(math.pi/6))


# stepenovanje

print(x ** 0.5)

# Zadatak

ime = input()
broj_gradilista = int(input())
broj_sati = broj_gradilista * 3

#
cat = int(input())
dog = int(input())

price = cat * 4 + dog * 2.5

print(f"{price} USD.")