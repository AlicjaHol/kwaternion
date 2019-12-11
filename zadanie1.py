#Zadanie 1
#czy liczba jest parzysta?
def czy_parzysta1(x):
    if x % 2 == 0:
        print("parzysta")
    else:
        print("nieparzysta")
def czy_parzysta2(x):
    if x[-1] in ['2', '4', '6', '8', '0']:
        print("parzysta")
    else:
        print("nieparzysta")
def czy_parzysta3(x):
    while x>=1:
        x=x-2
    if x==0:
        print("parzysta")
    else:
        print("nieparzysta")
liczba = input("podaj liczbę całkowitą ")
czy_parzysta1(int(liczba))
czy_parzysta2(liczba)
czy_parzysta3(int(liczba))
