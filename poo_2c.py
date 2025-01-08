class personaje:
    #Atributos de la clase
    nombre = "Default"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
#Variable del constructor vacío
mi_personaje = personaje()
#Modificando valores de los atributos
mi_personaje.nombre = "EstebanDido"
mi_personaje.fuerza = 300
mi_personaje.inteligencia = -2
mi_personaje.defensa = 30
mi_personaje.vida = 2


print("EL nombre de mi personaje es: ",mi_personaje.nombre)
print("EL nombre de mi personaje es: ",mi_personaje.fuerza)
print("EL nombre de mi personaje es: ",mi_personaje.inteligencia)
print("EL nombre de mi personaje es: ",mi_personaje.defensa)
print("EL nombre de mi personaje es: ",mi_personaje.vida)