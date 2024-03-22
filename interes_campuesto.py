#input

C = float(input("porfavor ingrese el dinero deseado : "))

# variables
n = 0
d = 2*C

#procesing
while(C <= d):
    C = 1.05 * C
    n = n + 1
print("el numero de meses totales fueron : ",n)
print("el dinero final fue de : ",C)