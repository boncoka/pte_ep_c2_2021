import math
x1 = input("elso pont elso koordinata")
y1 = input("elso pont masodik koordinata")
x2 = input("masodik pont elso koordinata")
y2 = input("masodik pont masodik kordinata")

distance = math.sqrt( (( float(x1) - float(x2))**2) + (( float(y1) - float(y2) )**2) )
print("A ket pont tavolsaga:" , distance)
