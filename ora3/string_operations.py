str1 = "Az almafan almak teremnek."
print("szoveg hossza" , len(str1))
str2 = "Terem"
print("Az str2 megvan az str1ben:" , str1.find(str2))
lower_str2 = str2.lower()
print(str2)
print("A lower str2 megvan az str1ben:" , str1.find(lower_str2))
upper_str2 = str2.upper()
print(str2, upper_str2)
str3 = "user12"
print("A lower str2 vegig kisbetus", lower_str2.islower())
print("A lower str2 vegig nagybetus", lower_str2.isupper())
print("A szovegek csak betut vagy szamjegyet tartalmaznak:")
print("\t", str1.isalnum())
print("\t", str2.isalnum())
print("\t", str3.isalnum())