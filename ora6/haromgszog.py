sides = []
side_name = "a"
for i in range(3):
    side = 0
    while side == 0:
        try:
            side = float(input(f"Kerem adja meg a haromszog {side_name} erteket: "))
            if side > 0:
                if side_name == "a":
                    side_name == "b"
                else:
                    side_name == "c"
                sides.append(side)
            else:
                side = 0
                print("A haromszog oldala csak pozitiv valos szam lehet")
        except ValueError:
            print("A megadott ertek nem megfelelo")
if sides[1] + sides[2] <= sides[0] or sides[0] + sides[2] <= sides[1] or sides[0] + sides[1] <= sides[2]:
    print("Nem haromszog oldalai")
else:
    k = sides[0] + sides[1] + sides[2]
    d = k / 2
    t = (d * (d - sides[0]) * (d - sides[1]) * (d - sides[2])) ** 0.5