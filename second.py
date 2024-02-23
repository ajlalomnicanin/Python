# Pozdravna poruka
print("Dobrodošli u svijet Pythona!")

# Računanje zbroja
broj1 = 10
broj2 = 5
zbroj = broj1 + broj2
print("Zbroj brojeva", broj1, "i", broj2, "je:", zbroj)

# Provjera parnosti broja
broj = 7
if broj % 2 == 0:
    print(broj, "je paran broj.")
else:
    print(broj, "je neparan broj.")

# Računanje faktorijela
def faktorijel(n):
    if n == 0:
        return 1
    else:
        return n * faktorijel(n-1)

n = 5
print("Faktorijel broja", n, "je:", faktorijel(n))
