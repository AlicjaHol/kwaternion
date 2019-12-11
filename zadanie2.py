#Zadanie 2
#czy liczba jest pierwsza?
if __name__ == "__main__":
    def czy_pierwsza(x):
        dzielniki = 0
        for i in range(1, x + 1):
            if x % i == 0:
                dzielniki = dzielniki + 1
        if dzielniki == 2:
            print("pierwsza")
        else:
            print("nie jest pierwsza")

    liczba = int(input("podaj liczbę całkowitą "))
    czy_pierwsza(liczba)
