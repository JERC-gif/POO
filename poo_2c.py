class personaje:
    #Atributos de la clase
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    #¿Qué es self (En Python)? Es una referencia al mismo objeto
    #¿Qué es el metodo init (En python)? Constructor que inicializa atributos de un objeto
    #¿Porque se usa doble __ (En python)? Dunder. Porque es metodo magico 
    #¿Cuando  se ejecuta el metodo init? Autom. al crear una nueva 
    
    #Una nueva instancia
    def imprimir_atributos(self):
        print(self.nombre)
        print("-Fuerza", self.fuerza)
        print("-Inteligencia", self.inteligencia)
        print("-Defensa", self.defensa)
        print("-Vida", self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def dañar(self, enemigo):
        return max (0, self.fuerza - enemigo.defensa)
    
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida =enemigo.vida - daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de" , enemigo.nombre, "es", enemigo.vida)
        
class Guerrero (personaje):    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    #sobreescribir el constructor
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Espada:", self.espada)
        
    #Sobreescribir el calculo del año
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #Escoger Navaja
    def escoger_navaja(self):
        opcion = int(input ("Escoge la navaja de la muerte:\n(1) Navaja Suiza, daño 10.\n(2)Navaja pioja, daño 6.\n>>>>>>"))
        if (opcion == 2):
            self.espada = 10
        elif (opcion == 1):
            self.espada = 6
        else:
            print("Valor invalido, intenta nuevamente")
            self.escoger_navaja()
            

class Mago(personaje):    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    #sobreescribir el constructor
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Libro:", self.libro)
        
    #Sobreescribir el calculo del año
    def dañar(self, enemigo):
        return self.inteligencia*self.libro - enemigo.defensa
    
    #Escoger Libro
    def escoger_libro(self):
        opcion = int(input ("Escoge el libro de la sabiduria:\n(1) El principito, daño 10.\n(2) Crepesculo, daño -10.\n>>>>>>"))
        if (opcion == 2):
            self.libro = 10
        elif (opcion == 1):
            self.libro = 6
        else:
            print("Valor invalido, intenta nuevamente")
            self.escoger_libro()
        
        
arturoSuarez = Guerrero("Arturo Súarez", 12, 3000, 2, 100, .5)

class Guerrero (personaje):    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    #sobreescribir el constructor
    def imprimir_atributos(self):
        super().imprimir_atributos()
        print("Espada:", self.espada)
        
    #Sobreescribir el calculo del año
    def dañar(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa
    
    #Escoger Navaja
    def escoger_navaja(self):
        opcion = int(input ("Escoge la navaja de la muerte:\n(1) Navaja Suiza, daño 10.\n(2)Navaja pioja, daño 6.\n>>>>>>"))
        if (opcion == 2):
            self.espada = 10
        elif (opcion == 1):
            self.espada = 6
        else:
            print("Valor invalido, intenta nuevamente")
            self.escoger_navaja()
            
persona = personaje("Angel Suarez", 20, 15, 2, 100)           
gandalf = Mago("Gandalf", 10, 100, 2, 100)
arturoSuarez = Guerrero("Arturo Súarez", 12, 3000, 2, 100)2

#Ataques antes de la tragedia
persona.imprimir_atributos()
gandalf.imprimir_libro ()
arturoSuarez.imprimir_atributos

#Ataques sin piedad
persona.atacar(arturoSuarez)
arturoSuarez.atacar(gandalf)
gandalf.atacar(persona)

#Atributos despues de la tragedia
persona.imprimir_atributos()
gandalf.imprimir_libro ()
arturoSuarez.imprimir_atributos

#print("El valor de espada es: ", arturoSuarez.espada)


#Variable del constructor vacío
# mi_personaje = personaje("EsteBandido", 100, 50, 45, 100 )
# mi_enemigo = personaje("Angel", 70, 100, 40, 100)
# mi_personaje.imprimir_atributos()
# mi_personaje.atacar(mi_enemigo)
#print(mi_personaje.esta_vivo())
#mi_personaje.morir()
# mi_personaje.subir_nivel(15,5,10)
# print("Valores actaulizados")
# mi_personaje.imprimir_atributos()