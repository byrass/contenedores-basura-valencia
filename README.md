# contenedores-basura-valencia
Biblioteca para analizar los datos abiertos sobre los contenedores de basura de valencia.

Como parte de la iniciativa de Transparencia, Datos Abiertos y Participación ciudadana del Ayuntamiento de Valencia (http://gobiernoabierto.valencia.es/), se han publicado datos sobre los contenedores, esta información incluye:

	Codvia: Código de la via donde se encuentra el contendores.
	Numportal: Numero de portal.
	Anyo: Año de carga.
	Empresa: Empresa que se encarga de su explotación.
	Modelo: Modelo del contenedor.
	productor_: Tipo de productor, domiciliaria, personalizada...
	tipo_carga: Tipo de carga del contenido.
	tipo: Tipo de contenido, residuos solidos, vidrio...
	tipovia: Tipo de la via
	calleempre: Descripcion de la calle donde se encuentra el contenedor.
Está en formato csv, entre otros. Link: http://gobiernoabierto.valencia.es/en/dataset/?id=contenedores-residuos-solidos

El programa consta de dos partes, parse() y Dato(). El primero lee los datos, y el segundo los analiza.

#parse()
	Help on function parse in module __main__:

	parse(inFile='res_contenedor.CSV')
		Dado el path del archivo csv (por ejemplo: 'C:\Windows\archivo')
		devolvera una lista de los datos,
		estos siendo:
		
			dato[0] = WKT
			dato[1] = codvia
			dato[2] = numportal
			dato[3] = anyo
			dato[4] = empresa
			dato[5] = modelo
			dato[6] = productor_
			dato[7] = tipo_carga
			dato[8] = tipo
			dato[9] = tipovia
			dato[10] = calleempre

#Dato()
	Help on class Dato in module __main__:

	class Dato(__builtin__.object)
	 |  Saca datos para cualquier aspecto de los contenedores
	 |  
	 |      0 = WKT
	 |      1 = codvia
	 |      2 = numportal
	 |      3 = anyo
	 |      4 = empresa
	 |      5 = modelo
	 |      6 = productor_
	 |      7 = tipo_carga
	 |      8 = tipo
	 |      9 = tipovia
	 |      10 = calleempre
	 |  
	 |  Methods defined here:
	 |  
	 |  __init__(self, index, data=parse())
	 |  
	 |  __str__(self)
	 |  
	 |  getDatos(self)
	 |      Devuelve una lista con los datos
	 |  
	 |  getDatosUnicos(self)
	 |      Devuelve una lista con los datos únicos
	 |  
	 |  getDict(self)
	 |      Devuelve un diccionario dato_único: numero ocurrencias de ese dato
	 |  
	 |  getLongitudDatos(self)
	 |      Devuelve la longitud de los datos
	 |  
	 |  getLongitudLlaves(self)
	 |      Devuelve el numero de datos unicos
	 |  
	 |  getMax(self)
	 |      Devuelve el valor o los valores maximos y su llaves
	 |  
	 |  getMedia(self)
	 |      Devuelve la media de cuantas veces se repite cada dato único
	 |  
	 |  getMediaDatos(self)
	 |      Devuelve la media numerica de los datos, solo funciona cuando los datos
	 |      son númericos
	 |  
	 |  getMin(self)
	 |      Devuelve el valor o los valores minimos y su llaves
	 |  
	 |  graphPie(self, figure_number)
	 |      Dibuja un grafico circular, debe darsele el número de la figura para evitar colisiones
	 |  
	 |  reset(self)
	 |      Resetea los datos al cambiar el indice y al iniciar, no usar solo
	 |  
	 |  setIndice(self, index)
	 |      Cambia el indice y resetea los datos
	 |      
	 |          0 = WKT
	 |          1 = codvia
	 |          2 = numportal
	 |          3 = anyo
	 |          4 = empresa
	 |          5 = modelo
	 |          6 = productor_
	 |          7 = tipo_carga
	 |          8 = tipo
	 |          9 = tipovia
	 |          10 = calleempre
	 |  
	 |  ----------------------------------------------------------------------
	 |  Data descriptors defined here:
	 |  
	 |  __dict__
	 |      dictionary for instance variables (if defined)
	 |  
	 |  __weakref__
	 |      list of weak references to the object (if defined)
