input_data = input("kerek egy egesz szamot: ")
try:
    int_number = int(input_data)
    print("a kapott szam haromszorosa:", 3 * int_number)
    print(type(input_data))
    print(type(int_number))
except ValueError:
    print("Ez nem egesz szam")

input_data = input("kerek egy valos szamot")
try:
    float_number = float(input_data)
    print("a kapott szam haromszorosa:", 3 * float_number)
    print(type(input_data))
    print(type(float_number))
    str_number = str(float_number)
    print(type(str_number), str_number)
except ValueError:
    print("Ez nem valos szam")