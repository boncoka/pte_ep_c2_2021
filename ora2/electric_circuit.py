A_electric_circuit = 25
capacity_of_the_electric_circuit = A_electric_circuit * 230
light_bulb = 150
clime = 1500
washing_machine = 1200
iron = 2000
already_used_power = light_bulb + clime + washing_machine
power_with_iron = already_used_power + iron
print("Lekapcsol e:", capacity_of_the_electric_circuit > power_with_iron)
