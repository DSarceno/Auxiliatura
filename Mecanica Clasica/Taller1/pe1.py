suma = 0 # suma total

for i in range(3,1000,1):
    if ((i%3 == 0) or (i%5 == 0)):
        suma += i
print(suma)
