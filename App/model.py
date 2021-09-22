"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import insertionsort as iss
from DISClib.Algorithms.Sorting import quicksort as qs
assert cf
import datetime as d
import time
import math


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newCatalog(list_type = 'ARRAY_LIST'):
    """
    Inicializa el catálogo de artistas y obras. Crea una lista vacia para guardar
    todas las obras y artistas del museo, adicionalmente se crea una lista que relaciona las obras de arte con sus artistas y una lista
    que relaciona a los artistas con su fecha de nacimiento. Retorna el catalogo inicializado.
    """
    catalog = {'Artwork': None,
               'Artist': None,
               'ArtistDate':None,
               'ArtworkDate':None,
                }

    catalog['Artwork'] = lt.newList(list_type)
    catalog['Artist'] = lt.newList(list_type,
                                    cmpfunction=cmpartistID)
    catalog['ArtistDate'] = lt.newList(list_type,
                                 cmpfunction="")

    catalog['ArtworkDate'] = lt.newList(list_type,
                                 cmpfunction="")
    

    return catalog

# Funciones para agregar informacion al catalogo
def addArtist(catalog,artists):
    """
    Se utiliza un diccionario para extraer únicamente los datos necesarios del archivo de excel Artists.csv y
    con base en ese diccionario se crean otras listas útiles para resolver los requerimientos.
    """

    artist = {'ConstituentID':artists['ConstituentID'],
                    'DisplayName': artists['DisplayName'],
                    'Nationality':artists['Nationality'],
                    'Gender':artists['Gender'],
                    'BeginDate':artists['BeginDate'],
                    'EndDate':artists['EndDate'],
                    'Artworks':lt.newList('ARRAY_LIST')}
                    
    addArtistDate(catalog, artist['DisplayName'], artist['BeginDate'],artist['EndDate'],artist['Nationality'],artist['Gender'])
    lt.addLast(catalog['Artist'], artist) 

def addArtwork(catalog, artwork):

    """
    Se utiliza un diccionario para extraer únicamente los datos necesarios del archivo de excel Artwork.csv y
    con base en ese diccionario se crean otras listas útiles para resolver los requerimientos.
    """


    artwork = {'ObjectID':artwork['ObjectID'], 
                    'Title':artwork['Title'], 
                    'ConstituentID':artwork['ConstituentID'][1:-1], 
                    'Date': artwork[ 'Date'],
                    'Medium':artwork['Medium'], 
                    'Dimensions':artwork['Dimensions'],
                    'CreditLine': artwork['CreditLine'], 
                    'Department':artwork['Department'], 
                    'DateAcquired':artwork['DateAcquired'],
                    #'Weight': artwork['Weight'],
                    #'Circumference': artwork['Circumference'],
                    #'Depth': artwork['Depth'],
                    #'Diameter':artwork['Diameter'],
                    #'Height': artwork['Height'],
                    #'Length': artwork['Length'],
                    #'Width':artwork['Width']
                    }

    lt.addLast(catalog['Artwork'], artwork)
    
    addArtworkDate(catalog,artwork['Title'],artwork['DateAcquired'],artwork['ConstituentID'], artwork['Medium'], artwork['Dimensions'] , artwork['CreditLine'])
    """
    A medida que se lee el archivo, se van extrayendo los artists_id para poder crear una lista que relacione 
    a los artistas con sus obras de arte.
    """
    artist_id = artwork['ConstituentID'].split(',')

    for artist in artist_id:
        addArtworkArtist(catalog, artist, artwork)

def addArtworkArtist(catalog, artist_id, artwork):
    """
    
    """
    artists = catalog['Artist']
    posartist = lt.isPresent(artists, artist_id)

    if posartist > 0:
        artist = lt.getElement(artists, posartist)
        lt.addLast(artist['Artworks'], artwork)
    

def addArtistDate(catalog, artist, date, deathdate, nationality, gender):
    
    if int(date) != 0 :
        adate = newArtistDate(artist,date, deathdate, nationality, gender )

        lt.addLast(catalog['ArtistDate'],adate)

def addArtworkDate(catalog, artwork, date, artist, medio, dimensions, creditline):
    
    if date != '' :
        
        adate = newArtworkDate(artwork,date, artist, medio, dimensions, creditline)

        lt.addLast(catalog['ArtworkDate'],adate)

# Funciones para creacion de datos


def newArtistDate(artist, date, deathdate, nationality, gender):
    artist_date = {'name': '', 'BeginDate':'', 'EndDate':'', 'nationality':'','gender':''}
    artist_date['name'] = artist
    artist_date['BeginDate'] = date
    artist_date['EndDate'] = deathdate
    artist_date['nationality'] = nationality
    artist_date['gender'] = gender

    return artist_date

def newArtworkDate(artwork, date, artist, medio, dimensions, creditline):
    artwork_date = {'Title': '', 'DateAcquired':'', 'Artist':'', 'Medium':'','Dimensions':'', 'CreditLine':''}
    artwork_date['Title'] = artwork
    artwork_date['DateAcquired'] = date
    artwork_date['Artist'] = artist
    artwork_date['Medium'] = medio
    artwork_date['Dimensions'] = dimensions
    artwork_date['CreditLine'] = creditline

    return artwork_date


# Funciones de consulta
def getArtistYear(catalog,año_inicial,año_final):

    artist_inrange = lt.newList("ARRAY_LIST")

    for artist in lt.iterator(catalog['ArtistDate']):

        if int(artist['BeginDate']) >= año_inicial and int(artist['BeginDate']) <= año_final:
        
            lt.addLast(artist_inrange, artist)

    sortYear_Artist(artist_inrange)
    return artist_inrange

    
def getArtworkYear(catalog,año_inicial,año_final):

    artwork_inrange = lt.newList("ARRAY_LIST")
    
    #Fechas ingresadas
    año_i = año_inicial.split("-")
    di = d.datetime(int(año_i[0]),int(año_i[1]), int(año_i[2]))
    año_f = año_final.split("-")
    df = d.datetime(int(año_f[0]),int(año_f[1]), int(año_f[2]))

    #Fechas del csv
    for artwork in lt.iterator(catalog['ArtworkDate']):
        date = artwork['DateAcquired'].split("-")
        d1 = d.datetime(int(date[0]),int(date[1]), int(date[2]))

        if d1 >= di and d1 <= df:
    
            lt.addLast(artwork_inrange, artwork )
    sortYear_Artwork(artwork_inrange)

    return artwork_inrange

def getArtistTecnique(catalog,name):

    '''
    Crea una lista nueva donde se van a ir clasificando las obras de arte de un artista según la técnica empleada.

    '''
    
    tecniques_list = lt.newList('ARRAY_LIST', cmpfunction=cmpArtistTecnique)

    for artist in lt.iterator(catalog['Artist']):
        if name.lower() in artist['DisplayName'].lower():
            total_obras = lt.size(artist['Artworks'])
            for artwork in lt.iterator(artist['Artworks']):
                medium = artwork['Medium']
                postechnique = lt.isPresent(tecniques_list, medium)
                artwork_filtrada = {'Title': artwork['Title'],
                                    'Date': artwork['Date'],
                                    'Medium': artwork['Medium'],
                                    'Dimensions': artwork['Dimensions']}
                
                if postechnique > 0:
                    tecnique = lt.getElement(tecniques_list,postechnique)
                    lt.addLast(tecnique['Artworks'], artwork_filtrada)
                else: 
                    #
                    tec = {'Tecnique': medium,
                            'Artworks': lt.newList('ARRAY_LIST')}

                    lt.addLast(tec['Artworks'], artwork_filtrada)
                    lt.addLast(tecniques_list, tec)
            
            sortTecnique_size(tecniques_list)

            return tecniques_list, total_obras


def getArtistNationality(catalog):

    nationality_artworks = lt.newList('ARRAY_LIST', cmpfunction=cmpArtistNationality)        
    #print(lt.size(catalog["Artist"])) 
    
    for artist in lt.iterator(catalog['Artist']):
        total_obras = lt.size(artist['Artworks'])
        
        nationality = artist['Nationality']   
        if nationality == "":
            nationality = "desconocido"
        
        if nationality == "Taiwanese":
            pass
        nation = lt.isPresent(nationality_artworks, nationality)
        artist_artworks = artist['Artworks']
        if nation > 0:
            nation_works = lt.getElement(nationality_artworks,nation)
            #lt.addLast(nationality_list, nationality)
        else:
            nation_works = {'Nationality': nationality,
                             'Artworks': lt.newList('ARRAY_LIST') } 
            lt.addLast(nationality_artworks, nation_works)
            
        for work in lt.iterator(artist_artworks):
            lt.addLast(nation_works["Artworks"], work)

    return nationality_artworks
            
def getTransportationCost(catalog, dpto):

    transp_cost = lt.newList('ARRAY_LIST')
    artworksBydpto = lt.newList('ARRAY_LIST')

    for artwork in lt.iterator(catalog['Artwork']):

        if artwork['Department'].lower == dpto.lower():

            lt.addLast(artworksBydpto, artwork)

    for artwork in lt.iterator(artworksBydpto):

        cost_weight=0
        cost_area=0
        cost_volume=0

        if artwork['Weight'] != '':
            cost_weight = int(artwork['Weight'])*72.000
        
        if artwork['Lenght'] != '' and artwork['Height'] != '':
            cost_area = (int(artwork['Lenght'])*int(artwork['Height']))*72.000
        
        elif artwork['Diameter'] != '':
            cost_area = (math.pi*(int(artwork['Diameter'])/2)**2)*72.000
        
        if artwork['Lenght'] != '' and artwork['Height'] != '' and artwork['Width'] != '':
            cost_volume = (int(artwork['Lenght'])*int(artwork['Height'])*int(artwork['Width']))*72.00
        
        elif artwork['Diameter'] != '' and artwork['Height'] != '':

            cost_volume = ((math.pi*(int(artwork['Diameter'])/2)**2)*artwork['Height'])*72.00
        
        



        

    pass
                    


# Funciones utilizadas para comparar elementos dentro de una lista

def cmpartistyear(artist1,artist2):

    return int(artist1['BeginDate']) < int(artist2['BeginDate'])


def cmpartworkyear(artwork1,artwork2):

    if artwork1['DateAcquired'] != '' and artwork2['DateAcquired'] != '':

        date_1 = d.date.fromisoformat(artwork1['DateAcquired'])
        date_2 = d.date.fromisoformat(artwork2['DateAcquired'])

        return date_1 < date_2

def cmpartistID(artistid1,artist):
    if (artistid1 in artist['ConstituentID']):
        return 0
    else:
        return -1

def cmpArtistTecnique(tec1, tec2):

    if (tec1.lower() == tec2['Tecnique'].lower()):
        return 0 
    else:
        return -1

def cmpArtistNationality(artist1, artist2):

    if artist1.lower() == artist2["Nationality"].lower():
        return 0 
    else:
        return -1
def cmpTecniquesize(tec1,tec2):

    return (lt.size(tec1['Artworks'])) > (lt.size(tec2['Artworks']))

def cmpNationalitysize(tec1,tec2):

    return (lt.size(tec1['Artworks'])) > (lt.size(tec2['Artworks']))

# Funciones de ordenamiento

def sortYear_Artist(artist_inrange):

    ms.sort(artist_inrange, cmpartistyear)


def sortYear_Artwork(artwork_inrange):

    ms.sort(artwork_inrange, cmpartworkyear)

def sortTecnique_size(tecnique_list):
    
    ms.sort(tecnique_list, cmpTecniquesize)

def sortNationality_size(nationalities):
    
    ms.sort(nationalities, cmpTecniquesize)
      