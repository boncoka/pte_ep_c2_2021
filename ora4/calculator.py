menu_command = ""
while menu_command != "0":
   menu_command = input("Kerlek valassz a menupontok kozul :\n\t0 - kilepes \n\t1 - osszeadas\n\t")
   if menu_command == "1":
      is_number = False
      a = 0
      b = 0
      while not is_number:
         try:
             a = float(input("Kerlek add meg az elso szamot: "))
             is_number = True
         except ValueError:
            print("A megadott ertek nem szam")
      is_number = False
      while not is_number:
         try:
            b = float(input("Kerlek add meg a masodik szamot: "))
            is_number = True
         except ValueError:
            print("A megadott ertek nem szam")
      print("A ket szam oszzege:", a + b)

print("Viszlat!")
