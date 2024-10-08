year = int(input("Podaj rok\n"))
leap = False

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
    else:
        leap = True

if leap:
    print("Przestępny")
else:
    print("Nieprzestępny")
