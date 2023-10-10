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


class Elemento():
    def __init__(self, valor, prioridad):
        self.valor = valor
        self.prioridad = prioridad

    def __str__(self):
        return "Value: " + str(self.valor) + " Prioridad: " + str(self.prioridad)

class ColaPrioridad():
    def __init__(self):
        self.datos = []

    def enqueue(self, elemento):
        if len(self.datos) == 0:
            self.datos.append(elemento)
        else:
            for i in range(len(self.datos)):
                if elemento.prioridad >= self.datos[i].prioridad:
                    break
            self.datos.insert(i, elemento)


#Ejercicio 04: Cola de mensaje en redes sociales(inicio, terminado)

class RedSocial():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad_usuarios = 0
        self.BDusuarios = []

    def usuario_nuevo(self,usuario):
        self.cantidad_usuarios += 1
        self.BDusuarios.append(usuario)


class Usuario():
    def __init__(self, nombre, username):
        self.nombre = nombre
        self.username = username
        self.cola

    def mandar_msj(self, contenido):
        mensaje = Mensaje(contenido)



class Mensaje():
    def __init__(self, contenido):
        self.contenido = contenido





#Ejercicio 04: Cola de mensaje en redes sociales(fin)

#Ejercicio 05: Procesamiento de ordenes en un restaruante (inicio, terminado)

class Restaurante():
    def __init__(self, nombre):
        self.nombre = nombre
        self.cola_pedidos = ColaPrioridad

    def recibir_pedido(self):
        pass

    def procesar_pedido(self):
        pass



class Pedido():
    def __init__(self, nombre):
        self.nombre = nombre



class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre

class Comida():
    def __init__(self, nombre):
        self.nombre = nombre

#Ejercicio 05: Procesamiento de ordenes en un restaruante (inicio, terminado)