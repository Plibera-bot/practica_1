#1
edad = int(input("Ingrese su edad: "))
edad = 100 - edad
print ("Para llegar a 100 años le faltan: "f"{edad}")
#2
grados = int(input("Ingrese valor de grado celsius: "))
comversion_grado = grados * 9 / 5 + 32
print (comversion_grado)
#3
suma = 0
for naturales in range(1,101):
    suma = suma + naturales 
#4 
lista = [2,5,6,2,3,9]
for i in lista :
    if (i % 2 != 0):
        continue
    print(i)
#5
lista2 = [3,7,5,11,-2,8]
cantidad = len(lista2)
for i in range(cantidad):
    if lista2[i] < 0 :
        break
    print (lista2[i])
    # consultar como ingresar la lista
#6
lista_par = []
lista_impar = []
lista = [2,5,6,2,3,9]
for i in lista :
    if (i % 2 != 0):
        lista_impar.append(i)
    else:
        lista_par.append(i)
print(lista_par)
print(lista_impar)        
#7
lista3 = []
i=0
n = int(input("agregue un valor "))
lista3.append(n)
while i < 5:
    i+=1
    n = int(input("agregue un valor "))
    lista3.append(n)
print (lista3)
tamaño = len(lista3)
for i in range(tamaño):
    if i % 3 == 0:
        lista3.pop(i)
print (lista3)  
#consultar