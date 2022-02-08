'''
4. Feladat
Írj egy programot while ciklussal, amely a felhasználó által meghatározott alkalommal írja ki a bekért szöveget!
'''
szamlalo = 1
szam = int(input("Kérek egy számot: "))
szam = szam + 1
szoveg = str(input("Kérek egy szöveget/mondatott: "))
while szamlalo < szam:
  print(szoveg)
  szamlalo = szamlalo + 1