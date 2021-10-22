import easygui

evszam_str = easygui.enterbox("Adjon meg egy evszamot:", title="adatgyujtes")
eredmeny_title = "Eredmeny"

try:
    evszam = int(evszam_str)
    if evszam % 4 ==0:
        if evszam % 100 ==0:
            if evszam % 400 == 0:
                easygui.msgbox("Ez az ev szokoev, mert oszthato 400-zal", title=eredmeny_title)
        else:
                easygui.msgbox("Ez az ev nem szokoev, mert 100-zal nem oszhato", title=eredmeny_title)
    else:
        easygui.msgbox("Ez az ev nem szokoev, mert nem oszthato 4-gyel")


except ValueError:
    easygui.msgbox("Nem evszamot adott meg.", title="Hiba")