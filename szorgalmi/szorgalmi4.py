start_number_system = 0
start_number = ""
end_number_system = 0
end_number = ""
raw_input_data = ""
invalid_value = True
while invalid_value:
    raw_input_data = input("Kerem adja meg a kiindulo szamrendszert: ")
    if raw_input_data.isnumeric():
        start_number_system = int(raw_input_data)
        if start_number_system > 1:
            invalid_value = False
        else:
            print("A megadott ertek nem egy egynel nagyobb pozitiv szam. ")
    else:
        print("A megadott ertek nem egy egynel nagyobb pozitiv szam. ")


invalid_value = True
while invalid_value:
    start_number = input("Kerem adja meg az atalakitando szamot: ")
    if start_number.isalnum():
        invalid_value = False
        for i in range(len(start_number)):
            if start_number[i].isnumeric():
                value2 = int(start_number[i])
            else:
                value2 = ord(start_number[i]) - 65 + 10
            if value2 > start_number_system:
                invalid_value = True
                print("Nem a kiiundalsi szamrendszerbeli szam. ")
    else:
        print("A megadott ertek nem csak szamjegyeket es betuket tartalmaz. ")


invalid_value = True
while invalid_value:
    raw_input_data = input("Kerem adja meg a cel szamrendszert: ")
    if raw_input_data.isnumeric():
        end_number_system = int(raw_input_data)
        if end_number_system > 1:
            invalid_value = False
        else:
            print("A megadott ertek nem egy egynel nagyobb pozitiv szam. ")
    else:
        print("A megadott ertek nem egy egynel nagyobb pozitiv szam. ")

number = 0
value = 0
for i in range(len(start_number)):
    if start_number[i].isnumeric():
        value = int(start_number[i])
    else:
        value = ord(start_number[i]) - 65 + 10
    number += value * start_number_system ** (len(start_number) - i - 1)

while number > 0:
    reminder = number % end_number_system
    if reminder < 10:
        end_number = str(reminder) + end_number
    else:
        end_number = chr(reminder + 65 - 10) + end_number
    number = number // end_number_system
print("A szam erteke a cel a szamrendszerben: ", end_number)
