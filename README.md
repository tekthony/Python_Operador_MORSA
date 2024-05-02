# OPERADOR MORSA

A partir de la versión 3.8 de Python se añadió un nuevo operador denominado morsa `(:= el nombre proviene de su similitud con los ojos y colmillos)`.

La característica de este operador es que nos permite la asignación de valores a una variable en una expresión, es decir, nos permite asignar el valor y devolverlo en la misma expresión, pudiendo reducir las líneas de código y mejorando legibilidad.

## EJEMPLOS

``` PYTHON
if (x := 10 + 5) > 10:
    print(x)  # Devuelve 15
```

`1.-` Queremos que un usuario introduzca números en una lista a través de un input, y que para dejar de incluirlos tenga que presionar el 0. Podríamos hacerlo así:

``` PYTHON
lista = []

while True:
    numero = int(input('Añade número: '))
    if numero == 0:
        break
    lista.append(numero)
    
print(lista)
```
Gracias al operador morsa, podremos reducir el código a lo siguiente:

``` PYTHON
lista = []

while (numero := int(input('Añade número: '))) != 0:
    lista.append(numero)
    
print(lista)
```
En ambos casos para las siguientes entradas de datos `4, 3, 6, 2, 9, 0`nos devolverá `[4, 3, 6, 2, 9]`, pero podemos ver que hemos reducido considerablemente el código, ya que podemos asignar el valor del `input` a la variable `numero` y comprobar que es distinta de 0 en la misma línea.

Con el operador morsa la asignación a la variable debe estar metida entre paréntesis ya que aunque no dará error, puede no devolver el resultado esperado, por ejemplo el código siguiente:

``` PYTHON
lista = []

while numero := int(input('Añade número: ')) != 0:
    lista.append(numero)

print(lista)
```
Para la misma entrada de datos anterior `(4, 3, 6, 2, 9, 0)`, nos devolvería `[True, True, True, True, True]`, que puede no ser lo que estamos buscando.

Otra característica es que se pueden hacer varias asignaciones en la misma línea de código:

``` PYTHON
(n_cuadrado:= (n:=10) * n)
print(n, n_cuadrado)  # Devuelve 10 100
```
De todas formas, el uso de esto operador debe limitarse a los casos en los que la legibilidad del código mejore, pero en los casos adecuados, puede resultar muy útil. Otro aspecto a valorar en su utilización es la falta de compatibilidad con versiones de `Python` anteriores a la 3.8.

