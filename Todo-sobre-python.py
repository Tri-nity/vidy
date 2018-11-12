#Aprende python 3 con el maestro tri-nity de figuri-ty etical hackers para mas información visita www.hmtrinity.com
#esto es un comentario
#hola soy un comentario
#imprime un texto porque pusiste comillas, tambien se pueden usar comillas dobles "", mas no variables
print ('khe')###imprime khe
#imprime variable o alguna regla algoritmica (sin comillas)
a = 1###se almacena 1 en a
b = 1###se almacena 1 en b
print (a+b)###imprime 2 osea suma a + b
print (2+2)###imprime 4
#reglas algoritmicas pueden ser colocados en cualquier funcion, nunca se escriben palabras separadas siempre con un _ u otro
#se almacenan estas reglas algoritmicas en las variables para cuando se impriman sean operadas
suma = 1+1###almacena 1+1 se opera dentro y da 2 cuando se imprima
resta = 2-2###almacena 2-2 se opera dentro y da 0 cuando se imprima
multiplicación = 3*3###almacena 3*3 se opera dentro y da 9 cuando se imprima
exponente = 3**3###almacena 3**3 se opera dentro y da 27 cuando se imprima
división = 5/8###almacena 5/8 se opera dentro y da 0.625 cuando se imprima
divicion_entera = 3//9###almacena 3//9 se opera dentro y da 0 cuando se imprima
Módulo = 3%5###almacena 3%5 se opera dentro y da 3 cuando se imprima
#variables
#solo se almacenan dichos digitos
num_entero = 10
num_real = 13.1415
tipo_cadena = 'hola mundo'
tipo_bool1 = True
tipo_bool2 = False
#tuplas
#son listas de palabras almacenadas que se puede seleccionar
mi_tupla = ('hola', 'amigo', 'estoi', 'creando')
#            0       1         2          3  [0] y [3:] y [2:4] y [0:2]
#            0      -3        -2         -1  [-1]

print (mi_tupla[0])#imprime hola
print (mi_tupla[-1])#imprime creando
print (mi_tupla[0:2])#imprime hola amigo exepto el seleccionado osea el 2 que es, estoi, solo el antes de llegar a 2 que es amigo
print (mi_tupla[2:4])#imprime estoi creando
print (mi_tupla[3:])#imprime creando
#listas
#son listas de palabras almacenadas que se pueden modificar y seleccionar
mi_list = ['hola', 'amigo', 'estoi', 'creando']
#            0       1         2          3  [1] y [0:3]
#            0      -3        -2         -1  [-1]
mi_list[1] = 'nel'###modifica amigo a nel
mi_list[0:3] = ['1', '2', '3']###modifica hola, amigo, estoi por 1, 2, 3... la tercer palabra no se modifica, solo para hasta 3
mi_list[-1]###muestra creando
mi_list.append('r')###añade 'r' con las comillas
mi_list.append(5)###añade 5
#len es un comando muy importante por si utilisaras cualquier lista,tuplas etc
len(mi_list)###muestra la cantidad de palabras que contiene mi_list
#esto es un diccionario
#es modificable
mi_diccionario = {'hola':'amigo', 'edad':21, 'curso':['python', 'ruby'], (2, 3): [1,2,3]}###el diccionario tiene que tener resultado o saldra error
#esto es muy pero muy importante imprime listas,tuplas,diccionarios etc asi se imprimen
print (mi_diccionario['edad'])###21
mi_diccionario['edad'] = 'años'###cambia el resultado de edad que es 21 por años, solo cambia el resultado de la palabra en el diccionario ejenplo 'edad':21 <----- el 21 en este caso se modificaria
del(mi_diccionario['edad'])###borra la palabra edad del diccionario mas su resultado
print (mi_diccionario[(2,3)])###imprime 1,2,3
#operadores relacionales si no tiene un valor da error
#    ==  ###igual que
#    !=  ###distinto que
#    <   ###menor que
#    >   ###mayor que
#    <=  ###menor o igual que
#    >=  ###mayor o igual que
#ejemplo
5 == 7 ###true
rojo = 1
verde = 2
rojo != verde ###verdadero (true)
8 < 12 ###verdadero (true)
12 > 7 ###verdadero (true)
12 <= 12 ###verdadero (true)
4 >= 5 ###falso (false)
#operadores logicos
# and  <----- (conjunción (union))
#el resultado es true (verdadero) solamente si las comparaciones también lo son. si una de las comparaciones es false, el resultado también.
10 == 10 and 8 > 7 ###verdadero (true) porque los resultados son iguales de verdaderos
(100 > 1000) and ('chann' == 'chann') ###falso (false), tambien se pueden poner caracteres usando comillas ''
(100 < 1000) and ('chann' == 'chann') ###verdadero (true)
# or   <----- (disyunción (desunión))
#el resultado es true si alguna de las comparaciones lo es. si ninguna comparación es true, el resultado es false.
(100 > 1000) or ('chann' == 'chann') ###verdadero (true) solo porque ('chann' == 'chann') es verdadero
(100 > 1000) or ('chann' == 'CHANN') ###falso (false) solo porque los dos son falsos tanto chan y 100 es mayor a 1000
# not  <----- (negación)
#El resultado es true si es false y viceversa
not (1 > 0) ###tendria que devolver true pero not lo niega y devuelbe false
not (1 < 0) ###tendria que devolver false pero not lo niega y devuelbe true
not ('hola' == 'HOlA') ###tendria que devolver false pero not lo niega y devuelbe true
not ('hola' == 'hola') ###tendria que devolver true pero not lo niega y devuelbe false
not (0 > 0) ####tendria que devolver false pero not lo niega y devuelbe true
#control de flujo
# if (si, sucede dicha condición, que hago)
# if condición
# ----Instrucciones
numeral = 1
if numeral > 0:### da como resultado numero es verdadero por que print lo imprimió porque fue true
	print('numero es verdadero')### no olvides usar tabulador |<--- ----->|
# else (sino, sucede dichas condiciónes, que hago)
numeral2 = 1
if numeral2 < 0:### da como resultado numero no es verdadero porque no se cumplio la condición porque es false
	print('numero es verdadero')
else:
	print('numero no es verdadero')
# elif nos permite agregar una condición mas
# (si, sucede dicha condición, que hago)
numeral3 = 5 ### numeral3 vale 5
if numeral3 < 1: ### si (numeral3(5)) es menor que 1
	print('numero es verdadero porque 5 es menor que 1') ### se imprime esto
elif numeral3 > 3: ### si (numeral3(5)) es mayor que 3
	print('numero es verdadero por que 5 es mayor que 3') ### se imprime esto
else: ### si ninguna de las condiciones se cumplen
	print('numero no tubo cumplimiento') ### imprime esto
#ciclo while
#nos permite ejecutar un bloque de código hasta que la condición deje de cumplirse o un numero determinados de veces
#mientras la condición se cumpla, se ejecutaran las Instrucciones dentro de la estructura
# while condition:
# ----Instrucciones
respuesta = 'si' ### la variable respuesta vale 'si'
numero = 0 ### la variable numero vale 0
while respuesta == 'si': ###mientras respuesta es igual a 'si' por lo tanto da True y activa la siguiente linea de código. haciendo un siclo
	numero = int(input('digite un numero ')) ### la variable numero pide una resuesta usando input(), dentro de input contiene un texto que te preguntara 'digite un numero', pero estando dentro de una exigencia pidiendo forsozamente un numero entero usando int()
	if numero > 0: ###si numero(0) es mayor que 0
		print('el numero ingresado es grande ') ### imprime este mensaje
	elif numero < 0: ### si numero(0) es menor que 0
		print('el numero ingresado es negativo menor ') ### imprime este mensaje
	else: ### sino se cumple ninguna condición
		print('el numero ingresado es igual a cero ') ### imprime este mensaje
	respuesta = input('quieres seguir usando el programa? < escribe si, sino escribe otra tecla y preciona enter > ') ### cada que respuesta sea contestada aparecera este input() porque esta dentro de la linea de codigo llamando a respuesta, si contestas si, respuesta es igual a si, por lo tanto el siclo nunca se corta
#ciclo for
#nos permite realizar iteraciones sobre una variable compleja ya sea lista o tupla
mi_lista = ['lala', 'lele', 'lili', 'lolo', 'lulu'] ###esto es una lista
for palabras in mi_lista: ###para palabras dentro mi_lista
	print(palabras) ###imprime palabras
#otro ejemplo
for años in range(5, 10): ###para años dentro serie de 5 hasta el 10 (hasta 10 para por lo cual no se imprime 10)
	print('tu edad es ', años) ###imprime tu edad es + resultado de años
#otro ejemplo
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ###esto es una lista
multiplicar = int(input('¿que tabla de multiplicar decea? ')) ###multiplicar pide un numero entero
for numero in tabla: ###para numero dentro tabla
	print(multiplicar, 'x', numero, ' = ', multiplicar * numero) ###imprime resultado de multiplicar x numero = multiplicar * numero
#Funciones
#bloque de codigo con un nombre asignado que tiene como objetivo realizar tareas especificas y devolver un resultado
def mi_funcion(): ### inicia mi_funcion
	'''primera funcion en python imprime dos mensajes'''
	print('hola a todos') ###imprime como mensaje hola a todos
	print('esta es mi primera funcion en python3.5') ###imprime como mensaje esta es mi primera funcion en python3.5
mi_funcion() ###muestra el proceso de mi_funcion
#otro ejemplo
def mi_funcion2(cadena, numero): ###inicia mi_funcion2(), contiene cadena y numero
	'''escribe una cadena de texto que le asignemos a numero'''
	print(cadena * numero) ###imprime el resultado de cadena * numero
mi_funcion2('hacker ', 5) ###muestra el proceso de mi_funcion2(), cadena cambiara a hacker y numero a 5
###otro ejemplo
def mi_funcion3(cadena, numero=4): ###inicia mi_funcion3(), contiene cadena y numero con valor a 4
	'''escribe una cadena de texto por default 4 veces'''
	print(cadena * numero) ###imprime el resultado de cadena * numero
mi_funcion3('hackercrack ')###muestra el proceso de mi_funcion3(), cadena cambiara a hackercrack
#otro ejemplo
def cuadrado(num): ###inicia cuadrado, contiene dentro num
	'''muestra el cuadrado de un numero'''
	print(num * num) ###imprime el resultado de num * num
cuadrado(5) ###muestra el proceso de cuadrado, num cambiara a 5
#otro ejemplo
def cuadrado1(num1): ###inicia cuadrado1(), contiene dentro num1
	print(num1 * num1) ###imprime el resultado de num1 * num1
def cuadrado2(): ###inicia cuadrado2
	'''imprime el cuadrado de numero ingresado'''
	n = int(input('(1) ingrese un numero: ')) ###la variable n pide un numero entero
	cuadrado1(n) ###num1 de cuadrado1 cambiará a n
cuadrado2() ###muestra el proceso de cuadrado2()
#otro ejemplo
print(cuadrado2()) ###devuelbe none
#otro ejemplo
def cuadrado_return(): ###inicia cuadrado_return()
	'''(devuelbe)retorna el cuadrado de un numero'''
	nn = int(input('(2) ingrese un numero ')) ###la variable nn pide un numero entero
	return nn * nn ###imprime el resultado de nn * nn ... devuelbe
cuad = cuadrado_return()###la variable cuad contiene cuadrado_return
print(cuad) ###imprime el resultado del proceso de cuadrado_return que esta en cuad
#es recomendable cambiar las variables para no crear conflictos de datos
#Funciones2
#asignacion multiple, python3.5 nos permite asignar en una sola linea (Instruccion) multiples variables
#a, b, c = 1, 'dos', True
#1, 'dos',True asi seria como quedase
#Modulos
#dividir programas grandes en modulos facilita el mantenimiento y lo hace mas legible
#para llamar un modulo nesesitamos ir al directorio de tu pc donde lo tengas usando cmd(batch) luego estando en la carpeta donde este tu modulo pones la vercion de python y el nombre de tu modulo
#ejemplo cd /home/tri-nity/Escritorio/Ensayos python/ (enter) luego (python3.5) o (python3) luego dentro de python (>>> import TUMODULO) (no es necesario .py ni los parentecis, solo es para que comprendas mejor) y para llamar una funcion tienes que poner asi (    >>> TUMODULO.TUFUNCIONPAPU()    )
#lo mejor de todo es que puedes importar los modulos y usarlos a tu manera
import modulosTri_nity ###se importa el modulo modulosTri_nity
modulosTri_nity.suma()
modulosTri_nity.resta()### se importa el comando resta del modulo
modulosTri_nity.multiplicacion()
modulosTri_nity.divicion()
#Paquetes
#nos permiten estructurar nuestros namespace (modulos)
#para crear un paquete nesesitamos crear una carpeta depues crear un archivo .py con este nombre (  __init__   ) para que python reconosca la carpeta como un paquete y ya nosotros podemos crear modulos dentro del paquete
import logopaquete.log ###se importa el paquete logopaquete y el modulo log
#POO (programacion orientada a objetos)
#paradicma: teoria cuyo nucleo central suministra la base y modelo para resolver problemas
#POO: el paradicma consiste en traer los conseptos del mundo real que sean relevantes para resolver un problema, en forma de clases y objetos
#objetos: pueden contener atributos los cuales definen el estado del objeto (caracteristicas) y metodos que definen sus funciones (herrmientas)
#clases: es una plantilla (modelo) sobre la cual se construyen nuestros objetos (instanciar objetos)
class miclaseejemplo: ### clase miclaseejemplo
	"""esto es un ejemplo clases, objetos y metodos""" # informacion sobre mi clase mensaje oculto
	entero = 3000  ### la variable entero contiene el numero 3000
	def mensaje(self, msj): ###la funcion mensaje contiene la variable (self que referencia a un objeto no es propia de python pero es necesario para conveniencia de nosotros) y nuestra abreviacion propia que deseamos msj
		print(msj) ###imprime el resultado de msj (hola POO)
#instanciamos de la clase y asignamos el objeto a las varibles
x = miclaseejemplo() ### la variable x contiene miclaseejemplo()
y = miclaseejemplo() ### la variable y contiene miclaseejemplo()

print (x.entero) ### se accede a x luego dentro de entero se imprime el resultado
print (y.mensaje('hola POO')) ### se accede a y luego dentro de mensaje hola POO toma el lugar de msj ... el resultado es none porque self no contiene un resultado
#para que no te agas bolas cuando el ultimo print accede a y osea miclaseejemplo luego a mensaje, directamente en msj se almacena hola POO pero si solo se ubiece accedido a y contendria hola POO.
#otro ejmplo de clases
#El método __init__ es un método especial de una clase en Python. El objetivo fundamental del método __init__ es inicializar los atributos del objeto que creamos.
#Básicamente el método __init__ remplaza al método inicializar que habíamos hecho en el concepto anterior.
#Las ventajas de implementar el método __init__ en lugar del método inicializar son:
#El método __init__ es el primer método que se ejecuta cuando se crea un objeto.
#El método __init__ se llama automáticamente. Es decir es imposible de olvidarse de llamarlo ya que se llamará automáticamente.
class miperro: ###esto es una clase llamada miperro
	'''segundo ejemplo para el manejo y comprencion de clases, objetos y metodos. con metodo __init__'''
	def __init__(selfinstancia, raza): ###funcion que se ejecuta automaticamente al instanciarla porque contiene __init__ (__init__ ará que se inicie antes de)... dentro contiene la variable selfinstancia y raza
		#--1--se recorre a la segunda variable... la primera variable osea selfinstancia (self) hasta que no la llamemos con print no se reconocerá su valor
		#definimos atributos
		selfinstancia.razza1 = raza ###dentro de selfinstancia se crea razza1 y se almacena la variable raza con su contenido
		#se inicia 2 veces porque se ejecuta dos veces esta funcion
		print('todos somos objetos') ###se imprime el mensaje todos somos objetos
	def ladrar(self, ladrido):  ###funcion con nombre ladrar contiene self y ladrido (  solo lo dire una vez mas self solo es una simple variable pero nos ayuda a acordarnos que esto referencia a un objeto no es necesario ponerlo asi.  xD :v  )
		#--2--se recorre a la segunda variable y ahi almacena el mensaje nunca en la primera, a menos que usemos la segunda variable y dentro de la primera variable cramos otra variable para almacenar
		print(ladrido) ###se imprime el resultado de ladrido
	def juego(self, jugar): ###funcion con nombre juego contiene la variable self y jugar
		print(jugar) ###se imprime el resultado de jugar
	def protejer(self, cuidar):  ###funcion con nombre protejer contiene la variable self y cuidar
		print(cuidar) ###se imprime el resultado de cuidar
#instanciamos dos obejos de la clase miperro
getrudis = miperro('dalmata') ###la variable getrudis contiene el resultado de miperro y carga un mensaje a miperro en raza que dice dalmata
parker = miperro('boxer') ###la variable parker contiene el resultado de miperro y carga un mensaje a mi miperro en raza que dice parker
#accedemos a los atributos
print(getrudis.razza1) ###accede a getrudis luego miperro y imprime el resultado de razza1
print(parker.razza1) ###accede a parker luego miperro y imprime el resultado
#accedemos a los metodos
getrudis.ladrar('*getrudis*----guau guau guau soy un perro ladrando xD') ###como getrudis contiene miperro() se accede a ladrar y en ladrido contendra el mensaje
parker.ladrar('*parker*----guau guau guau ajio ajio ajio no me gusta ladrar :v')###como parker contiene miperro() se accede a ladrar y en ladrido contendra el mensaje
#--3-- ENTIENDE ESTE PASO PRIMERO PARA QUE NO TE ATASQUES

#otro ejemplo
### lee lo de abajo v v v es muy importante saber como funciona self porque nos puede costar comprendelo
#el primer parámetro self del método se asigna automáticamente al propio objeto y el resto de parámetros a los argumentos con que llames al método
#Un método es una función que “pertenece a” un objeto. En Python, el término método no está limitado a instancias de clase: otros tipos de objetos pueden tener métodos también.
#Definición de clases. Un objeto puede ser creado instanciando una clase, Primero existen los objetos; luego aparecen las clases en función de la solución que estemos buscando
#en pocas palabras un parametro es un lugar en donde se coloca algo, un objeto puede ser una clase y la funcion de la clase pueden ser parametros, en los parametros pueden aver funciones y en las funciones las podemos llamar por el parametro self
#es como un segundo titulo a tu funcion
class reptil_lento(): ###clase con nombre reptil_lento
	"""llamamos las funciones de la tortuga"""
	def comiendo(self): ###funcion con nombre comiendo contiene self
		print('') ###imprime una linea de espacio
		print('como lechuga ñam ñam que me ves dejame comer agusto') ###imprime un texto
	def caminando(self): ###funcion con nombre cominando
		print('')
		print('mira como me muevo con estilo papu :v') ###imprime un texto
	def respirando(self): ###funcion con nombre respirando contiene self
		print('')
		print('respiro respiro pero devajo del agua nel') ###imprime un texto
	def viendounbuenmomaso(self): ###funcion con nombre viendounbuenmomaso
		print('')
		print('when estas programando en python3 but no le entiendes nada desde aqui xD tri-nity no sabe enseñar') ###imprime un texto

class tortuga(reptil_lento): ###clase tortuga llama a reptil_lento
	def presentacion(self): ###funcion con nombre presentacion contiene self
		self.comiendo() ###dentro de reptil_lento se llama la funcion de comiendo
		self.caminando()###dentro de reptil_lento se llama la funcion de caminando
		self.respirando()###dentro de reptil_lento se llama la funcion de respirando
		self.viendounbuenmomaso()###dentro de reptil_lento se llama la funcion de viendounbuenmomaso
tortuga_meme = tortuga()  ###la variable tortuga_meme contendra el resultado de tortuga
tortuga_meme.presentacion() ###se abre tortuga_meme y se inicia presentacion

#POO: herencia
#la erencia de clases, permite multiples clases base (super-clases), una clase derivada (sub-clase) puede hacer uso de los metodos de una clase base
class casa: ###clase con nombre casa
	'''personaje que viven en casa'''
	print('yo soy hijo de toni stark') ###se imprime el mensaje
	def __init__(self, apellido): ###funcion con ejecucion al ser instanciada(llamada para que me entiendas)... contiene self y apellido
		self.apellidoh = apellido###contiene self dentro de apellidoh el resultado de apellido

class persona(casa): ###clase personas llama a casa (instanciado, estan unidos, conectados)
	'''sub clase que hereda la clase casa'''
	def nombres(self, nombre, apellidoh): ###funcion nombres contiene self, nombre y llama a apellidoh de la clase casa en su funcion __init__ (instanciado, conectado, unido)
		print('mi nombre es ', nombre, 'de la casa de', apellidoh) ###se imprime el mensaje mi nombre es mas el resultado de nombre mas el mensaje de la casa de mas el resultado de apellidoh

class hereda(casa): ###clase con nombre hereda
	'''sub clase que hereda de la clase casa'''
	def nombres_f(self, nombre_t, apellidoh):###funcion con nombre nombres_f contiene self, nombre_t, apellidoh se liga de la clase casa en la funcion __init__
		print('mi nombre es ', nombre_t, 'hereda la casa', apellidoh) ###se imprime mi nombre es mas el resultado de nombre_t mas hereda la casa mas apellidoh

optimusprime = persona('stark') ###optimusprime contiene la clase persona, con el mensaje stark que se depositara accediendo a persona luego a casa despues en la funcion __init__ al final en apellido estara depositada
samus = persona('stark')###samus contiene la clase persona, con el mensaje stark con el mensaje stark que se depositara accediendo a persona luego a casa despues en la funcion __init__ al final en apellido estara depositada
tron = persona('stark')###tron contiene la clase persona, con el mensaje stark con el mensaje stark que se depositara accediendo a persona luego a casa despues en la funcion __init__ al final en apellido estara depositada
ironman = persona('stark')###ironman contiene la clase persona, con el mensaje stark con el mensaje stark que se depositara accediendo a persona luego a casa despues en la funcion __init__ al final en apellido estara depositada

print(optimusprime.nombres('optimusprime', optimusprime.apellidoh))###se accede a optimusprime(persona) luego en nombres y en nombre se deposita 'optimusprime' despues se accede a optimusprime(persona) luego a casa luego dentro de la funcion __init__ despues se pide el resultado de apellidoh
print(samus.nombres('samus', samus.apellidoh))###se accede a samus(persona) luego en nombres y en nombre se deposita 'samus' despues se accede a samus(persona) luego a casa luego dentro de la funcion __init__ despues se pide el resultado de apellidoh
print(tron.nombres('tron', tron.apellidoh))###se accede a tron(persona) luego en nombres y en nombre se deposita 'tron' despues se accede a tron(persona) luego a casa luego dentro de la funcion __init__ despues se pide el resultado de apellidoh
print(ironman.nombres('ironman', ironman.apellidoh))###se accede a ironman(persona) luego en nombres y en nombre se deposita 'ironman' despues se accede a ironman(persona) luego a casa luego dentro de la funcion __init__ despues se pide el resultado de apellidoh

add = hereda('papu :v') ###add contiene la clase hereda, primero se accede a la clase hereda luego se ingresa a casa despues en la funcion __init__ luego en apellido se almacena papu :v
acc = hereda('papu :v') ###acc contiene la clase hereda, primero se accede a la clase hereda luego se ingresa a casa despues en la funcion __init__ luego en apellido se almacena papu :v

print(add.nombres_f('wasaaa', add.apellidoh)) ###se ingresa a add(hereda) despues a la funcion nombres_f despues se deposita wasaaa en nombre_t luego se ingresa a hereda y se llama a apellidoh luego se imprime
print(acc.nombres_f('wazaaa', add.apellidoh)) ###se ingresa a acc(hereda) despues a la funcion nombres_f despues se deposita wazaaa en nombre_t luego se ingresa a hereda y se llama a apellidoh luego se imprime
#otro ejemplo

class perro: ###clase con nombre perro
	def __init__(self, temperamento): ###funcion con __init__...contiene self y temperamento
		self.temperamento = temperamento ### dentro de self temperamento contiene temperamento

class gatos: ###clase con nombre gatos
	def rrasgar(self): ###funcion con nombre rrasgar... contiene self y return con un mensaje
		return 'cazando ratones :3' ###devuelbe cazar ratones :3

class union(perro, gatos): ###clase con nombre  union contiene ligadas las funciones perro y gato
	pass ###se usa cuando no requiere ejecutar ninguna accion

animal = union('desastroso') ###variable con nombre animal contiene la clase union.... dentro de union dentro de perro y en temperamento contendra el mensaje

print('por mi gato estoi', animal.rrasgar(), 'y por mi perro soy bien', animal.temperamento) ###imprime el mensaje por mi gato estoi luego se mete a animal(union) luego a gatos y inicia la funcion rrasgar luego escribe el mensaje y por mi perro soy bien se mete a animal(union) luego a perro luego a la funcion __init__ luego en dentro de self en temperamento se imprime el resultado que la otra variable temperamento almaceno
#si se pone __init__ en gatos la prioridad seria para gatos y no para perro y en la clase union se tendria que poner primero gatos y luego perro
print('hola\nprueba\nde\nsalto\n') ###esto es un salto de lina
#polimorfismo y encapsulacion
#polimorfismo objetos de diferentes clase que tienen metodos y atributos con el mismo nombre, pero pueden tener diferentes resultados

class aeronave: ###clase con nombre aeronave
	def viajar(self): ###funcion con nombre
		print('yo viajo por los aires')  ###imprime un mensaje

class automovil: ###clase con nombre automovil
	def viajar(self): ###funcion con nombre viajar
		print('yo viajo por el camino') ###imprime un mensaje

zeppelin = aeronave() ###variable zeppelin contiene la clase aeronave
coche = automovil() ###variable coche contiene la clase automovil

zeppelin.viajar() ###se imprime de manera automatica sin necesidad de usar print
coche.viajar() ###se imprime de manera automatica sin necesidad de usar print

#Encapsulacion
#restringe el acceso a metodos y atributos determinados a los objetos instanciados de cierta clase
class ejemplo: ### clase con nombre ejemplo
	def __init__(self): ###funcion con __init__
		self.__oculto = 'soy un metodo oculto' ###contiene una variable oculta
	def publico(self): ### funcion con nombre publico
		return 'soy un metodo publico' ### devuelbe un mensaje
	def __privado(self): ### el doble guion bajo lo hace privado
		print('dentro de la clase todos me puede ver') ###imprime un mensaje
	def get_oculto(self): ###funcion con nombre get_oculto
		return self.__oculto ### devuelbe una variable oculta
	def set_oculto(self): ### funcion con nombre set_oculto
		self.__oculto = self.__privado() ###la variable __oculto contiene la funcion __privado y se hace visible

objeto = ejemplo() ### variable objeto contiene clase ejemplo
#intentamos acceder al metodo publico
#print(objeto.publico()) ###imprime dentro de ejemplo dentro de la clase publico el return ///// (es un mensaje pero si le quitas el # funcionara como la descripcion igual los mensajes de abajo )
#intentamos acceder al metodo __privado
#print(objeto.__privado()) ###sale error porque no reconoce la funcion __privado
#name mangling
#print(objeto._ejemplo__privado()) ### de esta manera se hace un metodo privado en vicible se accede al metodo objeto luego con un _ a ejemplo y se llama al metodo privado para hacerlo visible __privado
#accedemos al atributo __oculto del metodo __init__
#metodo get_
#print(objeto.get_oculto()) ###se accede a ejemplo t en __oculto se optiene el texto gracias a get_
objeto.set_oculto() ### se accede a ejemplo(objeto) luego se accede a set_oculto y se imprime el resultado de __oculto que contiene __oculto
#Metodos del objeto String
cadena = input('>>> digite una cadena de texto: ')### variable con nombre cadena escribe mensaje digite una cadena de texto y pide texto

print('\nel numero de caracteres de la cadena es: ', len(cadena)) ###se imprime una separacion junto con un texto y la cantidad de letras que contenga cadena con len

if cadena.isalpha(): ### si lo que ingresas(cadena contiene input) es alfabetica(isalpha() da true o false no se te olvide(es codigo de python))
	print('\nla cadena es alfabetica') ### se imprime una separacion junto con un texto

if cadena.isdigit(): ### si lo que ingresas(cadena contiene input) es un digito (isdigit() da true o false no se te olvide (es codigo de python))
	print('\nla cadena es numerica')

print('\nen mayusculas: ', cadena.upper()) ### si lo que ingresas(cadena contiene input) es un texto en mayusculas (upper() da true o false no se te olvide (es codigo de python))

print('\nen minusculas: ', cadena.lower()) ### si lo que ingresas(cadena contiene input) es un textp en minusculas (lower() da true o false no se te olvide (es codigo de python))

print('\ninvierte mayusculas y minusculas: ', cadena.swapcase()) ### si lo que ingresas(cadena contiene input) es un texto se invierte de mayusculas a minusculas y si la palabra es revuelta mayusculas y minusculas se invierte (swapcase() da true o false no se te olvide (es codigo de python))

print('remplaza a por z: ', cadena.replace('a', 'z')) ### si lo que ingresas(cadena contiene input) es una a se remplazara por z (replace() da true o false no se te olvide (es codigo de python))
#find() inicia desde la izquierda del digito 0 al (numero donde se encuentre el digito)
print('\nla posicion del caracter solicitado es: ', cadena.find('a')) ### si lo que ingresas(cadena contiene input) es una cadena de palabras o digitos la busca, por lo que pediste en este caso buscará a pero si no la alla imprime -1(find() da true o false no se te olvide (es codigo de python))
#rfind() inicia desde la derecha del digito 0 al (numero donde se encuentre el digito)
print('\nla posicion del caracter solicitado es: ', cadena.rfind('a')) ### si lo que ingresas(cadena contiene input) es una cadena de palabras o digitos la busca, por lo que pediste en este caso buscará a pero si no la alla imprime -1 (rfind() da true o false no se te olvide (es codigo de python))
#####ADVERTENCIA si no se alla true marca error######
print('lista de sub cadenas: ', cadena.split('a'))### si lo que ingresas(cadena contiene input) es un digito o letra de tal manera que este acomodada ejemplo abcdefg o aceghijkl o 12345 o 1356789 (de manera consecutiva como con el abecedario aunque falte una letra o digito) se crearan cadenas con el paquete de frases (split() da true o false no se te olvide (es codigo de python))
