#Zadanie 3
import math
def suma_cyfr(x):
    suma = 0
    while x>0:
        suma += x%10
        x //= 10
    return suma

def czy_pierwsza(x):
    i = 2
    while i <= math.sqrt(x):
        if x%i == 0:
            return False
        i+=1
    return True

liczba = int(input("podaj liczbę całkowitą "))
if czy_pierwsza(liczba) and czy_pierwsza(suma_cyfr(liczba)):
    print("liczba jest super-pierwsza")
elif czy_pierwsza(liczba) and not czy_pierwsza(suma_cyfr(liczba)):
    print("liczba jest pierwsza, ale nie jest super-pierwsza")
elif not czy_pierwsza(liczba):
    print("liczba nie jest pierwsza")

