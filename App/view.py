﻿"""
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

def printArtistDate(artists,tiempo, año_inicial, año_final):
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
        
        print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo))
    else:
        print('No se encontraron artistas nacidos en este rango de años')

catalog = None

def printArtworkDate(artworks,tiempo, año_inicial, año_final):
    
    tamano = lt.size(artworks)


    if tamano > 0:
        first_3_artworks = lt.subList(artworks, 1, 3 )
        last_3_artworks = lt.subList(artworks, tamano - 2, 3)

        print ('Se encontraron ' + str(tamano) + ' obras de arte adquiridas en el rango de ' + str(año_inicial) + ' hasta ' + str(año_final)+ "\n")
        cont = 0
        for artwork in lt.iterator(artworks):
            
            if 'purchase' in artwork['CreditLine'].lower():
                cont += 1

        print('Se encontraron ' + str(cont) + ' obras que fueron compradas.')
    
        print('Las primeras 3 obras de arte encontradas en el rango son: \n')
        for artwork in lt.iterator(first_3_artworks):
            artist_list = str(artwork["Artist"]['elements'])
            #print(artwork)
            print("Titulo: " + artwork["Title"] + ", Año de adquisición: " + artwork["DateAcquired"] + ", Artista/s : " + artist_list + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"])
            

        print('\nLas últimas 3 obras de arte encontradas en el rango son: \n ')
        for artwork in lt.iterator(last_3_artworks):
            artist_list = str(artwork["Artist"]['elements'])
            print("Titulo: " + artwork["Title"] + ", Año de adquisición: " + artwork["DateAcquired"] + ", Artista/s : " + artist_list + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"])
        
        print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo))
    else:
        print('No se encontraron obras de arte adquiridas en este rango de años')


def printArtistTecnique(tecnique, tiempo, tamano, name):

    if tamano > 0:
    
        print('Se encontraron ' + str(tamano) + ' obras del artista ' + name)
        tamano_tecnicas = lt.size(tecnique)
        print('El total de medios/tecnicas utilizados por el artista son: '+str(tamano_tecnicas))

        mayor_tec = lt.getElement(tecnique, 1)
        
        print('La técnica más utilizada es: '+str(mayor_tec['Tecnique'])+'\n y las obras que la utilizan son: \n')

        for artwork in lt.iterator(mayor_tec['Artworks']):
                print("Titulo: " + artwork["Title"] + ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')

        print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo)) 
    else:
        print('No se encontraron obras de arte de la técnica requerida.')

def printArtworkBynationalities(nationalities, tiempo):
    print('Las 10 nacionalidades con mayor número de obras son: ')

    top10 = lt.subList(nationalities,1, 10)
    top = lt.subList(nationalities,1, 1)


    for nacionalidad in lt.iterator(top10):
        tamano = lt.size(nacionalidad['Artworks'])
        print(nacionalidad['Nationality']+': '+ str(tamano))
    
    for nacionalidad in lt.iterator(top):
        tamano = lt.size(nacionalidad['Artworks'])
        print("La nacionalidad con más obras es: "+nacionalidad["Nationality"]+" con un total de "+str(tamano)+" obras.")
        print("La información de las primeras y ultimas 3 obras de dicha nacionalidad se presenta a continuación:")
        tresprimeras = lt.subList(nacionalidad['Artworks'], 1, 3)
        tresultimas = lt.subList(nacionalidad['Artworks'],tamano-2, 3)
        for artwork in lt.iterator(tresprimeras):
            #print(artwork)
            print("Titulo: " + artwork["Title"] + ", Artista/s : " + str(artwork["Artists"]["elements"])+ ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')
        
        for artwork in lt.iterator(tresultimas):
            #print(artwork)
            print("Titulo: " + artwork["Title"] + ", Artista/s : " + str(artwork["Artists"]["elements"])+ ", Fecha: "+ artwork["Date"] + ", Medio: "+ artwork["Medium"] + ", Dimensiones: " + artwork["Dimensions"] + '\n')
    
    print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo))

def printTransportationCost(transportation,tiempo, costo_total, old, dpto, peso_total):
    tamano = lt.size(transportation)
    if tamano > 0 :

        print('El total de obras a transporte del departamento de '+ dpto +' es: '+str(tamano)+'\n')
        print('\n El estimado total en USD para el costo del servicio es: '+ str(costo_total)+'\n')
        print('\n El estimado total del peso de las obras es: '+ str(peso_total)+'\n')

        top5_viejas = lt.subList(old, 1, 5 )
        print('\n Las 5 obras más antiguas a transportar son: \n')
        for artwork in lt.iterator(top5_viejas):
            print(artwork)
            #print("Titulo: " + artwork['Artwork']["Title"] + ", Artistas: "+  artwork['Artwork']["Artist/s"] + ", Clasificación : " + artwork['Artwork']["Classification"] + ", Fecha: "+ artwork['Artwork']["Date"] + ", Medio: "+ artwork['Artwork']["Medium"] + ", Dimensiones: " + artwork['Artwork']["Dimensions"] + ", Costo de Transporte: " + str(artwork["Cost"]) + '\n')
        
        top5_costosas = lt.subList(transportation, 1 , 5)
        print('\n Las 5 obras más costosas de transportar son: \n')

        for artwork in lt.iterator(top5_costosas):
            print(artwork)
            #print("Titulo: " + artwork['Artwork']["Title"] + ", Artistas: " + artwork['Artwork']["Artist/s"] + ", Clasificación : " + artwork['Artwork']["Classification"] + ", Fecha: "+ artwork['Artwork']["Date"] + ", Medio: "+ artwork['Artwork']["Medium"] + ", Dimensiones: " + artwork['Artwork']["Dimensions"] + ", Costo de Transporte: " + str(artwork["Cost"])+ '\n')
        print('El tiempo que tardó en ejecutarse el requerimiento es (mseg): ' + str(tiempo))
    else: 
        print('No se encontraron obras para transportar de ese departamento')
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
        printArtistDate(artist[0],artist[1], año_inicial, año_final )

    elif int(inputs[0]) == 3:


        "Requerimiento 2: obras de arte por fecha de adquisición"
   

        año_inicial = (input('Año inicial para el rango de busqueda: '))
        año_final = (input('Año final para el rango de busqueda: '))
        artwork = controller.getArtworkYear(catalog, año_inicial, año_final)
    
        printArtworkDate(artwork[0],artwork[1], año_inicial, año_final )

    elif int(inputs[0]) == 4:

        "Requerimiento 3: clasifica obras de un artista por técnica"
        
        name = input('Nombre del artista sobre el cual quiere realizar la consulta: ')
        tecniques = controller.getArtistTecnique(catalog, name)

        printArtistTecnique( tecniques[0],tecniques[2],tecniques[1], name)


    elif int(inputs[0]) == 5:
        
        "Requerimiento 4: clasifica las obras por la nacionalidad de sus creadores"
  
        
        nationalities = controller.getArtistNationality(catalog)
        printArtworkBynationalities(nationalities[0],nationalities[1])
        

    elif int(inputs[0]) == 6:

        'Requerimiento 5: transportar obras de un departamento '

        
        dpto = input('Ingrese el departamento del que quiere calcular el costo de transporte de sus obras: ')
        transport = controller.getTransportationCost(catalog, dpto)

        printTransportationCost(transport[0], transport[1] ,transport[2], transport[3],dpto, transport[4])
        

    elif int(inputs[0]) == 7:
        pass


    else:
        sys.exit(0)

sys.exit(0)
