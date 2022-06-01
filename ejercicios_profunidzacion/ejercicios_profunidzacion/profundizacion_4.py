# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con texto
'''
Enunciado:
Realice un programa que solicite por consola 3 palabras cualesquiera
Luego el programa debe consultar al usuario como quiere ordenar las palabras
1 - Ordenar por orden alfabético (usando el operador ">")
2 - Ordenar por cantidad de letras (longitud de la palabra (len) y operador ">")

Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
e imprimir en pantalla de la mayor a la menor

Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
e imprimir en pantalla de la mayor a la menor

IMPORTANTE: Para ordenar las palabras deben realizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido.
'''

print('Ejercicios de práctica con cadenas')
# Empezar aquí la resolución del ejercicio

primer_palabra = (str(input("Ingrese una palabra: ")))
segunda_palabra = (str(input("Ingrese otra palabra: ")))
tercer_palabra = (str(input("Ingrese otra palabra más: ")))

#Longitud de palabras
len_1 = len(primer_palabra)
print(f"La primer palabra tiene {len_1} letras")
len_2 = len(segunda_palabra)
print(f"La segunda palabra tiene {len_2} letras")
len_3 = len(tercer_palabra)
print(f"La tercer palabra tiene {len_3} letras")


#Solicitu de ordenamiento de palabras
orden = int(input("ingrese una opcion: 1- orden alfabetico ; 2-orden longitud: "))


if(orden == 1):
    if(primer_palabra > segunda_palabra > tercer_palabra):  
        print(primer_palabra, segunda_palabra , tercer_palabra)
    elif (primer_palabra > tercer_palabra > segunda_palabra):  
        print(primer_palabra, tercer_palabra , segunda_palabra)
    elif (segunda_palabra > primer_palabra > tercer_palabra):  
        print(segunda_palabra, primer_palabra , tercer_palabra)
    elif (segunda_palabra > tercer_palabra > primer_palabra):
        print(segunda_palabra, tercer_palabra, primer_palabra)
    elif (tercer_palabra > primer_palabra > segunda_palabra):  
        print(tercer_palabra, primer_palabra , segunda_palabra)
    elif (tercer_palabra > segunda_palabra > primer_palabra):  
        print(tercer_palabra, segunda_palabra , primer_palabra)

elif (orden == 2):
    if(len_1 > len_2 > len_3):  
        print(primer_palabra, segunda_palabra , tercer_palabra)
    elif (len_1 > len_3 > len_2):  
        print(primer_palabra, tercer_palabra , segunda_palabra)
    elif (len_2 > len_1 > len_3):  
        print(segunda_palabra, primer_palabra , tercer_palabra)
    elif (len_2 > len_3 > len_1):  
        print(segunda_palabra, tercer_palabra , primer_palabra)  
    elif (len_3 > len_1 > len_2):  
        print(tercer_palabra, primer_palabra , segunda_palabra)
    elif (len_3 > len_2 > len_1):  
        print(tercer_palabra, segunda_palabra , primer_palabra)

else:
    print("Ingrese una opción correcta: 1 o 2")

