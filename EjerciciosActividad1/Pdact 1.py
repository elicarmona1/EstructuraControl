''' Si la edad es mayor o igual a 18 y menor o igual a 22
 y los puntos de evaluación obtenidos fueron superiores o iguales a 80,
  pasa para el programa de LIGA PROFESIONAL DE FUTBOL
Si la edad es mayor o igual a 18 y menor o igual a 22
y los puntos de evaluación obtenidos fueron menores a 80,
pasa para el programa de LIGA SEMIPROFESIONAL
'''


edad = int(input("Por favor ingrese la edad: "))
punt_evaluacion = int(input("Por favor ingrese en un rango de 0 a 100 sus puntos de evaluación: "))
if edad>=18 and edad<=22 and punt_evaluacion >= 80:
    print("Usted pasa para el programa de  LIGA PROFESIONAL DE FUTBOL")
else :
    if edad>=18 and edad<=22 and punt_evaluacion < 80:
        print("Usted pasa para el programa de LIGA SEMIPROFESIONAL")
    else :
        print("Usted no aplica para el programa")
