import easygui
import math


diameter_str = easygui.enterbox("A kor atmeroje cm-ben: ", title="Adatbekeres")
try:
    diameter = float(diameter_str)
    if diameter > 0:
        radius = diameter / 2
        kerulet = 2 * radius * math.pi
        terulet = radius ** 2 * math.pi
        easygui.msgbox(f"A {diameter} cm atmeroju kor kerulete {kerulet:.3f} cm,"
                       f" terulete pedig {terulet:.3f} cm^2")
except ValueError:
    easygui.msgbox("Nem megfelelo atmero", title="Hiba")