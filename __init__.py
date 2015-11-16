# -*- coding: utf-8 -*-

'''
Python realizado en 2.7.9, requiere del modulo csv
'''
import csv, pylab

def parse(inFile = '.\Datos Originales\\res_contenedor.CSV'):
    ''' Dado el path del archivo csv (por ejemplo: 'C:\Windows\\archivo')
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
    '''
    data = [[], []]
    with open(inFile, 'r+') as csvfile:
        reader = csv.reader(csvfile, delimiter = ';')
        for line in reader:
            if line[0] == 'WKT':
                data[1].append(line)
            else:
                data[0].append(line)
    return data

class Dato(object):
    '''
    Saca datos para cualquier aspecto de los contenedores

        0 = WKT
        1 = codvia
        2 = numportal
        3 = anyo
        4 = empresa
        5 = modelo
        6 = productor_
        7 = tipo_carga
        8 = tipo
        9 = tipovia
        10 = calleempre
    '''
    def __init__(self, index, data = parse()):
        self.data, self.mode = data
        self.setIndice(index)

    def setIndice(self, index):
        '''
        Cambia el indice y resetea los datos

            0 = WKT
            1 = codvia
            2 = numportal
            3 = anyo
            4 = empresa
            5 = modelo
            6 = productor_
            7 = tipo_carga
            8 = tipo
            9 = tipovia
            10 = calleempre
        '''
        self.index = index
        self.reset()
    def reset(self):
        '''
        Resetea los datos al cambiar el indice y al iniciar, no usar solo
        '''
        print 'Creando listado de datos para indice %d...' % self.index
        self.datos = []
        self.datos_unicos = []
        for d in self.data:
            self.datos.append(d[self.index])
            if d[self.index] not in self.datos_unicos:
                self.datos_unicos.append(d[self.index])
        self.datos.sort()
        self.datos_unicos.sort()
        print 'Listado completado.'
    def getModo(self):
        '''
        Devuelve el nombre del indice que se esta analizando
        '''
        return self.mode[0][self.index]
    def getDatos(self):
        '''
        Devuelve una lista con los datos
        '''
        return self.datos
    def getDato(self, dato):
        '''
        Devuelve el dato especificado
        '''
        return self.getDict()[dato]
    def getDatosUnicos(self):
        '''
        Devuelve una lista con los datos únicos
        '''
        return self.datos_unicos
    def getLongitudLlaves(self):
        '''
        Devuelve el numero de datos unicos
        '''
        return len(self.datos_unicos)
    def getLongitudDatos(self):
        '''
        Devuelve la longitud de los datos
        '''
        return len(self.datos)
    def getMedia(self):
        '''
        Devuelve la media de cuantas veces se repite cada dato único
        '''
        return sum(self.getDict().values())/float(self.getLongitudLlaves())
    def getMediaDatos(self):
        '''
        Devuelve la media numerica de los datos, solo funciona cuando los datos
        son númericos
        '''
        return sum(self.getDatos())/float(self.getLongitudDatos())
    def getMax(self):
        '''
        Devuelve el valor o los valores maximos y su llaves
        '''
        valMax = 0
        ans = {}
        d = self.getDict()
        for i in d.keys():
            if d[i] > valMax:
                valMax = d[i]
        for i in d.keys():
            if d[i] == valMax:
                ans[i] = d[i]
        return ans
    def getMin(self):
        '''
        Devuelve el valor o los valores minimos y su llaves
        '''
        valMin = float('inf')
        ans = {}
        d = self.getDict()
        for i in d.keys():
            if d[i] < valMin:
                valMin = d[i]
        for i in d.keys():
            if d[i] == valMin:
                ans[i] = d[i]
        return ans

    def graphPie(self, figure_number):
        '''
        Dibuja un grafico circular, debe darsele el número de la figura para evitar colisiones
        '''
        pylab.figure(figure_number, figsize=(8,8), facecolor='white')
        pylab.title(self.mode[0][self.index])
        pylab.pie(self.getDict().values(), labels = self.getDict().keys(), autopct='%1.1f%%')
        pylab.show()
    def getDict(self):
        '''
        Devuelve un diccionario dato_único: numero ocurrencias de ese dato
        '''
        ans = {}
        for d in self.datos_unicos:
            ans[d] = self.datos.count(d)
        return ans
    def __str__(self):
        ans = []
        d = self.getDict()
        keys = sorted(self.getDict().keys())
        for i in range(self.getLongitudLlaves()):
            t = []
            t.append(str(keys[i]))
            t.append(str(d[keys[i]]))
            ans.append(' '.join(t))
        return str('\n'.join(ans))
