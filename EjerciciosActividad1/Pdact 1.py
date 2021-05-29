producto = (input('ingrese el producto: '))
cantidad = int(input('ingrese la cantidad: '))
valunitario = int(input('ingrese el valor unitario: '))
ciudadvent = (input('ingrese la ciudad de venta: '))

total = 0
total = cantidad*valunitario

print(total)

if ciudadvent=='medellin' or ciudadvent=='cali':
    total=total*0.95
    print('el valor con el descuento es de: ',total)
else:
    print('no se aplica el descuento')
    print('su total a pagar es: ',total)
