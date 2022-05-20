list ()
longitud=int(input("Digite la longitud deseada: "))

if longitud:
    print("debe digitar la longitud deseada")
    
else:
    
    for i in range(longitud*2):
        ok=False
        while not ok:
            try:
                valor=int(input("Digite el valor: "))
                ok=True
            except:
                print('Error solo se permiten valores enteros')

        if valor <= 20:
            
            if len(list)<=longitud:
                if valor%2==0:
                    if len (list)==longitud:
                        for i in range(longitud):
                            if valor%2==0:
                                print('Recuerde digitar el maximo de la longitud')
                                valor=int(input("Digite el valor: "))
                            else:
                                list.append(valor)