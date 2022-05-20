#funcion 
def mostrarLista (producto):
    print(f' digite el nombre del producto que desea ver: {producto}')


#progprincipal
productos=['lenovo','apple', 'dell','asus', 'hp','lg', 'sony','samsung', 'acer','toshiba']
    
for i in productos:
    print(i)

#puntob recorrer la lista y devolver cadena con valores
cadena=", ". join(productos)
print(cadena)
#puntoc
ordenar=sorted(productos)
print(ordenar)
#puntod

productos=['lenovo','apple', 'dell','asus', 'hp','lg', 'sony','samsung', 'acer','toshiba']
print('la longitud de la lista es:{}' .format(len(productos)))