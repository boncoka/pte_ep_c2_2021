import random

raw_input_data =  input("adj meg egy szamot: ")
try:
    number = int(raw_input_data)
    if number < 10:
        print("ez a szam kisebb mint tiz")
    else:
        print("nagyobb vagy egyenlo mint tiz")
    if number > 100:
        print("ez a szam nagyobb mint szaz")
    else:
        print("ez a szam kisebb mint szaz")


    if number % 2 > 0 :
        print("Ez a szam paratlan")
    else:
        print("Ez a szam paros")
    number1 = 100
    number2 = 20
    if number1 % number2 == 0:
        print("A", number2, "osztoja a", number1)
    else:
        print("nem osztoja")
        if number2 % number1 == 0:
            print("osztoja")
        else:
            print("egyik sem osztoja a masiknak")
    str = "Alma."
    if str[0] == str[-1]:
        print("Az elso es az utolso karakte megegyezik")
    else:
        print("Nem egyezik az elso es utolso karakter")
    if number > 0:
        print("pozitiv")
    elif number < 0:
        print("negativ")
    else:
        print("nulla")

    if str[0].isupper():
        print("nagybetuvel kezdodik")
    else:
        print("nem nagybetuvel kezdodik")
    str2 = "almafa"
    str3 = "almaszar"
    if str3[0:5] == str2[0:5]:
        print("az elso ot karakter egyezik")
    else:
        print("nem azonos")
    number = 17
    if number >= 3 and number < 17:
        print("beleesik a szam az intervallumba")
    else:
        print("nem esik bele")
    a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
    print(a, b, c)
    if a + b > c and a + c > b and c + b > a:
        print("Lehet oldalhossz")
    else:
        print("nem lehet oldalhossz")

    if b <= a and c <= a:
        print("a a legnagyobb")
        if b >= c:
            print("A c a legkisebb")
        else:
            print("A b a legkisebb")
    else:
        if b >= c:
            print("A b a legnagyobb")
            if a >= c:
                print("c a legkisebb")
            else:
                print("a a legkisebb")
        else:
            print("A c a legnagyobb")
        if a >= b:
            print("A b a legkisebb")
        else:
            print("a a legkisebb")



    character = "3"
    maganhangzok = "aAeEöüóőúéáÖÜÓŐÚÉÁ"
    numbers = "0123456789"
    if maganhangzok.find(character) >= 0:
        print("maganhanzo lesz")
    elif numbers.find(character) >= 0:
        print("szamjegy")

    number = 27
    if number % 3==0 and number % 5 == 0:
        print("oszthato 3mal es 5tel is")
    elif number % 3 == 0:
        print("csak 3mal")
    elif number % 5 == 0:
        print("csak 5tel")
    else:
        print("nem oszthato sem 3mal se 5tel")

    grade = random.randint(1, 5)
    if grade == 5:
        print("kivalo")
    elif grade == 4:
        print("jo")
    elif grade == 3:
        print("kozepes")
    elif grade == 2:
        print("elegseges")
    elif grade == 1:
        print("elegtelen")
    else:
        print("nem megfelelo ertek")

    print(random.random())
except ValueError:
    print("de en egy szamot kertem")
