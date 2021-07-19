
from csv import DictReader

def crear_datos(nombre_archivo):
	"""
	Entradas: 
	(str) nombre_archivo
	Nombre o ruta del archivo .csv a trabajar
	
	Salidas:
	(Oredered Dict)	diccionario cuyo formato para ingresar la distancia 
	de una ciudad 'x'con respecto de otra ciudad 'y' es:
 	(Nombre de Diccionario)[indice de ciudad de origen][nombre de ciudad de destino]
	
	(Dict) indices_ciudades el cual contiene los indices de la forma
	{'Nombre_ciudad': 0}
	"""

	diccionario = []
	indices_ciudades = {}
	with open(nombre_archivo, mode='r') as csv_Ciudades:
		csv_reader = DictReader(csv_Ciudades)
		n_ciudades = len(csv_reader.fieldnames)-1
		i_ciudad = iter(range(n_ciudades))
		for fila in csv_reader:
			diccionario.append(fila)
			indices_ciudades[fila['km/min']] = next(i_ciudad)
	return diccionario,indices_ciudades

def ListaNombres(nombre_archivo):
	lista = []
	diccionario,indices = crear_datos(nombre_archivo)
	for i in diccionario:
		lista.append(i['km/min'])
	return lista
