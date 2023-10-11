#Librerias adicionales
import time
from datetime import date
import random


#Librerias adicionales


#Ejercicio 01: Implementacion de colas (inicio, terminado)
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0

    def insertar_inicio(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.contador += 1

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.contador += 1

    def insertar_dentro(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        indice = 0
        while actual != None:
            if indice == posicion:
                anterior = actual
                siguiente = actual.siguiente
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = siguiente
                return
            indice += 1
            actual = actual.siguiente
        self.contador += 1

    def eliminar_primero(self):
        if self.cabeza == None:
            raise Exception("Lista enlazada vacia")
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            segundo = self.cabeza.siguiente
            self.cabeza.siguiente = None
            self.cabeza = segundo
        self.contador -= 1

    def eliminar_final(self):
        actual = self.head
        if self.cabeza == None:
            raise Exception("Lista enlazada vacia")
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            while actual != None:
                if actual.siguiente == self.cola:
                    break
                actual = actual.siguiente
            actual.siguiente = None
            self.cola = actual
        self.contador -= 1

    def eliminar_dentro(self, dato):
        actual = self.cabeza
        anterior = None
        while actual != None:
            if actual.siguiente.valor == dato:
                anterior = actual
                actual = actual.siguiente
                break
            actual = actual.siguiente
        anterior.siguiente = actual.siguiente
        self.contador -= 1

    def eliminar_todo(self):
        self.cabeza = None

    def size(self):
        return self.contador

    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual.valor, end=" - ")
            actual = actual.siguiente
        print("None")

class ColaEnlazada(ListaEnlazada):
    def __init__(self):
        super().__init__()

    def enqueue(self, dato):
        super().insertar_final(dato)

    def dequeue(self):
        devolver = self.cabeza.valor
        super().eliminar_primero()
        return devolver

    def size(self):
        return super().size()

    def is_empty(self):
        return self.contador == 0

    def front(self):
        return self.cabeza.valor


class ColaArray():
    def __init__(self):
        self.datos = []

    def enqueue(self, dato):
        self.datos.append(dato)

    def dequeue(self):
        devolver = self.datos[0]
        self.datos.remove(self.datos[0])
        return devolver

    def size(self):
        return len(self.datos)

    def is_empty(self):
        return self.size() == 0

    def front(self):
        return self.datos[0]

    def imprimir_cola(self):
        print(self.datos)

    def __str__(self):
        return str(self.datos)


class Elemento():
    def __init__(self, valor, prioridad):
        self.valor = valor
        self.prioridad = prioridad

    def __str__(self):
        return "Value: " + str(self.valor) + " Prioridad: " + str(self.prioridad)


class ColaPrioridad(ColaArray):
    def __init__(self):
        super().__init__()

    def enqueue(self, elemento):
        aux = 0
        if self.size() == 0:
            self.datos.append(elemento)
        else:
            for i in range(self.size()):
                if elemento.prioridad < self.datos[i].prioridad:
                    break
                aux += 1
            self.datos.insert(aux, elemento)



#Ejercicio 01: Implementacion de colas (fin)

#Ejercicio 02: Simulacion de Fila de supermercado (inicio, terminado)

class Supermercado():
    def __init__(self, nombre):
        self.nombre = nombre
        self.fila = ColaArray()

    def atender(self):
        return self.fila.dequeue()

    def mostrar_fila(self):
        print("[", end="")
        for i in range(self.fila.size()):
            print(self.fila.datos[i], end= "  ")
        print("]")
    def __str__(self):
        return "Supermercado " + self.nombre

class ClienteSupermercado():
    def __init__(self, nombre, supermercado):
        self.nombre = nombre
        self.supermercado = supermercado

    def pagar(self):
        self.supermercado.fila.enqueue(self)

    def __str__(self):
        return self.nombre



supermercadoPrueba = Supermercado("Islay")

cliente1 = ClienteSupermercado("Juan", supermercadoPrueba)
cliente2 = ClienteSupermercado("Maria", supermercadoPrueba)
cliente3 = ClienteSupermercado("Jose", supermercadoPrueba)

cliente1.pagar()
cliente3.pagar()
cliente2.pagar()

print("Ejercicio 02: Simulacion de Fila de supermercado")
print(supermercadoPrueba)
print(supermercadoPrueba.mostrar_fila())

print(supermercadoPrueba.atender())
print(supermercadoPrueba.atender())
print(supermercadoPrueba.atender())

print("\n--------------------------------------------------\n")
#Ejercicio 02: Simulacion de Fila de supermercado (fin)

#Ejercicio 03: Procesamiento de tareas en una cola (inicio, terminado)

class ColaTareas():
    def __init__(self):
        self.tareas = ColaArray()

    def procesar_tarea(self):
        tiempo_ejecucion = self.tareas.front().tiempo
        print("Procesando tarea...")
        time.sleep(tiempo_ejecucion)
        print("Tarea procesada en " + str(tiempo_ejecucion) + " segundos")
        return self.tareas.dequeue()

    def mostrar_cola_tareas(self):
        print("[", end="")
        for i in range(self.tareas.size()):
            print(self.tareas.datos[i], end=" - ")
        print("]")

class Tarea():
    def __init__(self, nombre, tiempo):
        self.nombre = nombre
        self.tiempo = tiempo

    def encolar_tarea(self, colaTareas):
        colaTareas.tareas.enqueue(self)

    def __str__(self):
        return self.nombre

print("Ejercicio 03: Procesamiento de tareas en una cola")
nueva_cola_tareas = ColaTareas()

tarea1 = Tarea("servicio de conexion a internet", 1)
tarea2 = Tarea("Copiar archivo", 2)

tarea1.encolar_tarea(nueva_cola_tareas)
tarea2.encolar_tarea(nueva_cola_tareas)

nueva_cola_tareas.mostrar_cola_tareas()

nueva_cola_tareas.procesar_tarea()
nueva_cola_tareas.procesar_tarea()

print("\n--------------------------------------------------\n")

#Ejercicio 03: Procesamiento de tareas en una cola (fin)

#Ejercicio 04: Cola de mensaje en redes sociales(inicio, terminado)

class RedSocial():
    def __init__(self, nombre):
        self.nombre = nombre

class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_mensajes = ColaArray()

    def enviar_mensaje(self, contenido, para):
        mensaje = Mensaje(contenido)
        para.cola_mensajes.enqueue(mensaje)

    def recibir_mensaje(self):
        mensaje = self.cola_mensajes.dequeue()
        print(mensaje)


class Mensaje():
    def __init__(self, contenido):
        self.contenido = contenido
        self.date = date.today()

    def __str__(self):
        return self.contenido + " (Mensaje enviado a las " + str(self.date) + ")."


print("Ejercicio 04: Cola de mensaje en redes sociales")
twitter = RedSocial("Twitter")
carlos = Usuario("Carlos")
renato = Usuario("Renato")

carlos.enviar_mensaje("Hola!", renato)
carlos.enviar_mensaje("¿Como estas?", renato)
carlos.enviar_mensaje("Adios", renato)

renato.recibir_mensaje()
renato.recibir_mensaje()
renato.recibir_mensaje()

print("\n--------------------------------------------------\n")
#Ejercicio 04: Cola de mensaje en redes sociales(fin)

#Ejercicio 05: Procesamiento de ordenes en un restaruante (inicio, terminado)

class Restaurante():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_pedidos = ColaArray()

    def recibir_pedido(self, pedido):
        self.cola_pedidos.enqueue(pedido)

    def procesar_pedido(self):
        print(self.cola_pedidos.dequeue())

    def mostrar_cola_pedidos(self):
        print("[", end="")
        for i in range(self.cola_pedidos.size()):
            print(self.cola_pedidos.datos[i], end=" - ")
        print("]")

class Pedido():
    def __init__(self, nombre, platos_pedidos):
        self.nombre = nombre
        self.platos_pedidos = platos_pedidos

    def __str__(self):
        return self.nombre + " - " + str(self.platos_pedidos)

class Cliente_restaurante():
    def __init__(self, nombre, restaurant_ingresado):
        self.nombre = nombre
        self.platos_elegidos = []
        self.restaurant_ingresado = restaurant_ingresado
    def realizar_pedido(self):
        pedidoFinal = Pedido(str("pedido de " + self.nombre), self.platos_elegidos)
        self.restaurant_ingresado.recibir_pedido(pedidoFinal)
    def elegir_plato(self, comida):
        plato = Comida(comida)
        self.platos_elegidos.append(str(plato))


class Comida():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

print("Ejercicio 05: Procesamiento de ordenes en un restaruante")

rest_china = Restaurante("China-Town")

tecsup = Cliente_restaurante("tecsup", rest_china)

familia1 = Cliente_restaurante("familia1", rest_china)

tecsup.elegir_plato("chaufa de carne")
tecsup.elegir_plato("lomo saltado")
tecsup.elegir_plato("aeropuerto")

tecsup.realizar_pedido()

familia1.elegir_plato("sopa wantan")
familia1.elegir_plato("chaufa de cerdo")

familia1.realizar_pedido()

rest_china.mostrar_cola_pedidos()

rest_china.procesar_pedido()
rest_china.procesar_pedido()

print("\n--------------------------------------------------\n")
#Ejercicio 05: Procesamiento de ordenes en un restaruante (fin)

#Ejercicio 06: Cola de impresion (inicio, terminado)

class Impresora():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_impresion = ColaArray()

    def recibir_documento(self, documento):
        self.cola_impresion.enqueue(documento)

    def imprimir_documento(self):
        asignacion_duracion = random.randint(1,3)
        cadena_suply = str(self.cola_impresion.front())
        print("Iniciando la impresion de " + cadena_suply)
        time.sleep(asignacion_duracion)
        print("Impresion finalizada en " + str(asignacion_duracion))
        self.cola_impresion.dequeue()

class DocumentoImprimir():
    def __init__(self, nombre):
        self.nombre = nombre
        self.contenido = None

    def __str__(self):
        return self.nombre

class UsuarioImpresion():
    def __init__(self, nombre):
        self.nombre = nombre

    def enviar_documento_imprimir(self, nombre, impresora):
        documento_enviar = DocumentoImprimir(nombre)
        impresora.recibir_documento(documento_enviar)

print("Ejercicio 06: Cola de impresion")

impresora1 = Impresora("HP fulltank 510")

roberto = UsuarioImpresion("Roberto")

roberto.enviar_documento_imprimir("Cotizaciones software", impresora1)
roberto.enviar_documento_imprimir("lab01 seguridad informatica", impresora1)
roberto.enviar_documento_imprimir("Codigo lanzamientos", impresora1)


impresora1.imprimir_documento()
impresora1.imprimir_documento()
impresora1.imprimir_documento()

print("\n--------------------------------------------------\n")
#Ejercicio 06: Cola de impresion (fin)

#Ejercicio 07: Sistema de turnos en una clinica (inicio, terminado)

class Clinica():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_pacientes = ColaArray()

    def paciente_espera(self, paciente):
        self.cola_pacientes.enqueue(paciente)

    def atender_paciente(self):
        print("Paciente " + str(self.cola_pacientes.front()) + " atendido.")
        self.cola_pacientes.dequeue()

    def mostrar_cola_pacientes(self):
        print("[", end="")
        for i in range(self.cola_pacientes.size()):
            print(self.cola_pacientes.datos[i], end=" - ")

        print("]")

    def __str__(self):
        return self.nombre + " - " + self.cola_pacientes.size()

class Paciente():
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_cola(self, clinica):
        clinica.paciente_espera(self)

    def __str__(self):
        return self.nombre

print("Ejercicio 07: Sistema de turnos en una clinica")
clinicaCielo = Clinica("Cielo")

pedro = Paciente("Pedro")
luz = Paciente("Luz")

pedro.hacer_cola(clinicaCielo)
luz.hacer_cola(clinicaCielo)

clinicaCielo.mostrar_cola_pacientes()

clinicaCielo.atender_paciente()
clinicaCielo.atender_paciente()

print("\n--------------------------------------------------\n")
#Ejercicio 07: Sistema de turnos en una clinica (fin)

#Ejercicio 08: Organizacion de eventos (inicio, terminado)

class EventoPrioridad():
    def __init__(self, nombreEvento):
        self.nombre = nombreEvento
        self.cola_prioridad = ColaPrioridad()

    def encolar_participante(self, participante):
        self.cola_prioridad.enqueue(participante)

    def dejar_entrar(self):
        print("Se dejo entrar a " + str(self.cola_prioridad.front()))
        self.cola_prioridad.dequeue()

    def mostrar_cola_participantes(self):
        print("[", end="")
        for i in range(self.cola_prioridad.size()):
            print(self.cola_prioridad.datos[i], end=" - ")
        print("]")

class Participante():
    def __init__(self, nombres, prioridad):
        self.nombres = nombres
        self.prioridad = prioridad

    def hacer_cola(self, evento):
        evento.encolar_participante(self)

    def __str__(self):
        return self.nombres + " - " + str(self.prioridad) + " | "

print("Ejercicio 08: Organizacion de eventos")
evento_matrimonio = EventoPrioridad("Matrimonio")

jeremy = Participante("Jeremy", 3)
magaly = Participante("Magaly", 2)
pepe = Participante("Pepe", 1)
renata = Participante("Renata", 3)
julia = Participante("Julia", 1)
#orden prioritario = [Pepe, Julia, Magaly, Jeremy, Renata]
jeremy.hacer_cola(evento_matrimonio)
magaly.hacer_cola(evento_matrimonio)
pepe.hacer_cola(evento_matrimonio)
renata.hacer_cola(evento_matrimonio)
julia.hacer_cola(evento_matrimonio)

evento_matrimonio.mostrar_cola_participantes()

evento_matrimonio.dejar_entrar()
evento_matrimonio.dejar_entrar()
evento_matrimonio.dejar_entrar()
evento_matrimonio.dejar_entrar()
evento_matrimonio.dejar_entrar()

print("\n--------------------------------------------------\n")
#Ejercicio 08: Organizacion de eventos (fin)

#Ejercicio 09: Implementacion de una cola con 2 pilas (inicio, terminado)

class ColaDosPilas():
    def __init__(self):
        self.entrada = []
        self.salida = []

    def queue(self, dato):
        self.entrada.append(dato)

    def dequeue(self):
        if not self.salida:
            while self.entrada:
                self.salida.append(self.entrada.pop())

        if self.salida:
            return self.salida.pop()
        else:
            return None

    def is_empty(self):
        return not self.entrada and not self.salida

    def size(self):
        return len(self.entrada)

print("Ejercicio 09: Implementacion de una cola con 2 pilas")

cola_dos_pilas = ColaDosPilas()

cola_dos_pilas.queue(1)
cola_dos_pilas.queue(2)
cola_dos_pilas.queue(3)
print(cola_dos_pilas.size())
print(cola_dos_pilas.is_empty())
print(cola_dos_pilas.dequeue())
print(cola_dos_pilas.dequeue())
print(cola_dos_pilas.dequeue())
print(cola_dos_pilas.size())
print(cola_dos_pilas.is_empty())

print("\nLaboratorio 06 terminado")
#Ejercicio 09: Implementacion de una cola con 2 pilas (fin)
