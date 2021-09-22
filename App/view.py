"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """


import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf

default_time = 1000
sys.setrecursionlimit(default_time*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de una artista por técnica")
    print("5- Clasificar las obras por nacionalidad de sus creadores")
    print("6- Transportar obras de un departamento")
    print("7- Nuevo exposición en el museo")

def initCatalog():
    """
    Inicializa el catalogo de obras
    """
    return controller.initCatalog()

def loadData(catalog):
    """
    Carga las obras y los artistas en la estructura de datos
    """
    controller.loadData(catalog)

def printArtistDate(artists, año_inicial, año_final):
    tamano = lt.size(artists)

    first_3_artists = lt.subList(artists, 1, 3 )
    last_3_artists = lt.subList(artists, tamano - 2, 3)

    if tamano > 0 :
        
        print ('Se encontraron ' + str(tamano) + ' artistas nacidos en el rango de ' + str(año_inicial) + ' hasta ' + str(año_final)+ "\n")

        print('Los primeros 3 artistas encontrados en el rango son: ')
        for artist in lt.iterator(first_3_artists):
            print("Nombre: " + artist["name"] + ", Año de nacimiento: " + artist["BeginDate"] + ", Año de muerte: " + artist["EndDate"] + ", Nacionalidad: "+ artist["nationality"] + ", Género: " + artist["gender"])
            

        print('\nLos últimos 3 artistas encontrados en el rango son: ')
        for artist in lt.iterator(last_3_artists):
            print("Nombre: " + artist["name"] + ", Año de nacimiento: " + artist["BeginDate"] + ", Año de muerte: " + artist["EndDate"] + ", Nacionalidad: "+ artist["nationality"] + ", Género: " + artist["gender"])
    else:
        print('No se encontraron artistas nacidos en este rango de años')

catalog = None

def printArtworkDate(artworks, año_inicial, año_final):
    
    tamano = lt.size(artworks)

    first_3_artworks = lt.subList(artworks, 1, 3 )
    last_3_artworks = lt.subList(artworks, tamano - 2, 3)

    if tamano > 0:

        print ('Se encontraron ' + str(tamano) + ' obras de arte adquiridas en el rango de ' + str(año_inicial) + ' hasta ' + str(año_final)+ "\n")
        cont = 0
        for artwork in lt.iterator(artworks):
            
            if 'purchase' in artwork['CreditLine'].lower():
                cont += 1

        print('Se encontraron ' + str(cont) + ' obras que fueron compradas.')
    
        print('Las primeras 3 obras de arte encontradas en el rango son: \n')
        for artwork in lt.iterator(first_3_artworks):
            print("Titulo: " + artwork["Title"] + ", Año de adquisición: " + artwork["DateAcquired"] + ", Artista/s : " + artwork["Artist"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"])
            

        print('\nLas últimas 3 obras de arte encontradas en el rango son: \n ')
        for artwork in lt.iterator(last_3_artworks):
            print("Titulo: " + artwork["Title"] + ", Año de adquisición: " + artwork["DateAcquired"] + ", Artista/s : " + artwork["Artist"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"])
    else:
        print('No se encontraron obras de arte adquiridas en este rango de años')


def printArtistTecnique(tecnique, tamano, name):
    
    print('Se encontraron ' + str(tamano) + ' obras del artista ' + name)
    tamano_tecnicas = lt.size(tecnique)
    print('El total de medios/tecnicas utilizados por el artista son: '+str(tamano_tecnicas))

    mayor_tec = lt.getElement(tecnique, 1)
    
    print('La técnica más utilizada es: '+str(mayor_tec['Tecnique'])+'\n y las obras que la utilizan son: \n')

    for obra in lt.iterator(mayor_tec['Artworks']):
            print(obra)

def printArtworkBynationalities(nationalities):
    pass

def printTransportationCost(transportation, dpto, total, old):
    tamano = lt.size(transportation)


    print('El total de obras a transporte del departamento seleccionado es: '+str(tamano)+'\n')
    print('\n El estimado total en USD para el costo del servicio es: '+ str(total)+'\n')
    top5_viejas = lt.subList(old, 1, 5 )
    print('Las 5 obras más antiguas a transportar son: \n')
    for obra_vieja in lt.iterator(top5_viejas):
        print(obra_vieja)
    
    top5_costosas = lt.subList(transportation, 1 , 5)
    print('Las 5 obras más costosas de transportar son: \n')

    for obra_costosa in lt.iterator(top5_costosas):
        print(obra_costosa)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        
        
        print("Cargando información de los archivos ...\n")
        catalog = initCatalog()
        loadData(catalog)

        tamano_artwork = lt.size(catalog['Artwork'])
        tamano_artist = lt.size(catalog['Artist'])

        last_3_artworks = lt.subList(catalog['Artwork'], tamano_artwork - 2, 3 )
        last_3_artists = lt.subList(catalog['Artist'], tamano_artist - 2, 3)

        print('Obras de arte cargadas: ' + str(tamano_artwork)+'\n')
        print('Artistas cargados: ' + str(tamano_artist)+ '\n')
        print('Últimas tres obras de arte cargadas:')

        for artwork in lt.iterator(last_3_artworks):
            print(artwork)

        print("")
        print("-----------------------------------------------------------------------------------")
        print("")
        print('Últimos tres artistas cargados:')
        
        for artist in lt.iterator(last_3_artists):
            print(artist)

    

    elif int(inputs[0]) == 2:

        "Requerimiento 1: artistas por fecha de nacimiento"

        año_inicial = int(input('Año inicial para el rango de busqueda: '))
        año_final = int(input ('Año final para el rango de busqueda: '))
        artist = controller.getArtistYear(catalog, año_inicial, año_final)
        printArtistDate(artist, año_inicial, año_final )

    elif int(inputs[0]) == 3:


        "Requerimiento 2: obras de arte por fecha de adquisición"
        #TODO:arreglar que salga nombre de artista

        año_inicial = (input('Año inicial para el rango de busqueda: '))
        año_final = (input('Año final para el rango de busqueda: '))
        artwork = controller.getArtworkYear(catalog, año_inicial, año_final)
        printArtworkDate(artwork, año_inicial, año_final )

    elif int(inputs[0]) == 4:

        "Requerimiento 3: clasifica obras de un artista por técnica"
        
        name = input('Nombre del artista sobre el cual quiere realizar la consulta: ')
        tecniques = controller.getArtistTecnique(catalog, name)
        printArtistTecnique( tecniques[0],tecniques[1], name)

    elif int(inputs[0]) == 5:
        
        "Requerimiento 4: clasifica las obras por la nacionalidad de sus creadores"
        
        nationalities = controller.getArtistNationality(catalog)
        print(nationalities)
        

    elif int(inputs[0]) == 6:

        'Requerimiento 5: transportar obras de un departamento '
        
        dpto = input('Ingrese el departamento del que quiere calcular el costo de transporte de sus obras: ')
        transport = controller.getTransportationCost(catalog, dpto)
        printTransportationCost(transport[0], dpto,transport[1], transport[2])
        

    elif int(inputs[0]) == 7:
        pass


    else:
        sys.exit(0)

sys.exit(0)
