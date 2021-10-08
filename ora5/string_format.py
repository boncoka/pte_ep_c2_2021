number = 5
number2 = number * 2
print("A number valtozo erteke: ", number, "\b.Ha megszorozzuk kettovel: ", number2, "\b-t kapok")
print("A number valtozo erteke: ", number, ".Ha megszorozzuk kettovel: ", number2)
print(f"A number valtozo erteke: {number} .Ha megszorozzuk kettovel: {number2}")
print("A number valtozo erteke: {}. Ha megszorozzuk kettovel, akkor {}-t kapok".format(number, number2))

# Igazitasok
print(f"A number valtozo erteke: {number:<3}. Ha megszorzom kettovel, akkor {number2:>5}-t kapok. ")
print("A number valtozo erteke: {:^3}. Ha megszorzom kettovel, akkor {:^4}-t kapok. ".format(number, number2))

# szamformatumok
number = 125
print(f"A szam binaris alakja: {number: b}, az oktalis alakja: {number: o}, a decimalis alakja: {number: d},"
      f"hexadecimalis alakja: {number: x}, es {number: X}")
print("A szam binaris alakja: {:b}, az oktalis alakja: {:o}, a decimalis alakja: {:d}, "
      "hexadecimalis alakja: {:x}, es {:X}".format(number, number, number, number, number))
number = 65
print(f"{number: c}")
print("{:c}".format(number))

number = 100.12345
print(f"Tudomanyos: {number: e} vagy {number: E}")
print(f"Valos szam")
print(f"3 tizedesjegy pontossag: {number: .3f}")
print(f"15 tizedesjegy pontossag: {number: .15f}")
print(f"15 karakteren: {number: 15%}")
print(f"15 karakteren, 3 tizedesjegy pontossag: {number: 15.3f}")
