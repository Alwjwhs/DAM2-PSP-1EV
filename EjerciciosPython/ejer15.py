""" Ejercicio 15: Crea un fichero de texto con el nombre y contenido que tú desees. Por ejemplo, Ejercicio15.txt. 
Realiza un programa en Python que lea el fichero <<Ejercicio15.txt>> y muestre su contenido por pantalla sin espacios. 
Por ejemplo, si el fichero contiene el siguiente texto “Hola que haces”, deberá mostrar “Holaquehaces”."""
with open("Ejercicio15.txt", "r") as file:
    contenido = file.read()
"Sustituye dos espacios en blanco por solo uno"
contenido_sin_espacios = contenido.replace(" ", "")

print(contenido_sin_espacios)
