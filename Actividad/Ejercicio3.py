from asyncio.windows_events import NULL 
def fibonacci(longitud):
       fibo=[0,1]
       if longitud > 1: 
           for i in range(2, longitud):
                  val= fibo [i- 2] + fibo[i-1]
                  fibo.append(val)
           return fibo 
       elif longitud ==1: 
             return fibo [0] 
       else:
               return NULL 
long=50
x=[]
if len (x)==0:
    x = fibonacci (long) 
else:
        print('Esta lista no está vacía')

if x: 
       print(x) 
else: 
        print ('El tamaño no es válido')