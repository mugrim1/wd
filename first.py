
imiee = 'adam'

print(imiee)

def dluga_nazwa_funkcji():
    """parametry: ... """ # tzw. docstring

def main():
    print("Hello World")

# łańcuch znakow

# ctrl + / komentuj/odkomentuj
# shift+alt+strzalka w dol powiela kod
# """costam """ - lancuch wielowierszowy

#imie = """Ala"""
imie = str("Ala") #poprzez konstruktor
print(imie)
print (type(imie))
print (type(5))
print (type(5.6))
print (type(True))
print (type(False))
print("Ala" + "ma kota")
print("Ala"  + "ma" + str(5) + "kotów")
print(5)
ilosc_kotow = 5
print("Ala"  + "ma  {}  kotów".format(ilosc_kotow))
print("Ala"  + f"ma  {ilosc_kotow}  kotów")
print("Ala"  + "ma  {1}{0}{2}  kotów".format(4,5,7))
liczba = 6.123567
print(f"liczba{liczba:.2f}")
print(imie[0])

imie = imie.lower()
print(imie)

#liiiiiiiiiiiiiiiiiiczbyyyyyy
liczba = 1
liczbaf = 4.5 
suma = liczba + liczbaf 
print(1 + 2)
print(1 - 2)
print(1 / 2)
print(1 // 2) # dzielenie bez reszty 
print(1 * 2)
print(1 ** 2) # potegowanie
print(1 % 2 ) #modulo

print(0.1 + 0.2 == 0.3)

# listy

lista = []
lista2 = [1, 2, 3]
lista3 = [1, "Ala", 3.4, True, None]
final_list = lista + lista2 + lista3
lista2[2] #wartość 3,indeks 2

lista4 = [
[1, 2, 3]
[4, 5, 6]
[7, 8, 9 ]

]

lista4[1][1] #5

# slownik

slownik = {}

slownik2 = { "klucz": "wartość"}
slownik3 = {0: "Adam"}
slownik2["klucz"]
slownik3[0]
slownik2.keys()
slownik2.values()
