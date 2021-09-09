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
from DISClib.Algorithms.Sorting import mergesort as sa
assert cf

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
               'ArtworkArtist': None,
               'ArtistDate':None,
                }

    catalog['Artwork'] = lt.newList(list_type)
    catalog['Artist'] = lt.newList(list_type,
                                    cmpfunction="")
    catalog['ArtistDate'] = lt.newList(list_type,
                                 cmpfunction="")


    return catalog

# Funciones para agregar informacion al catalogo


def addArtwork(catalog, artwork):

    "Se utiliza un diccionario para extraer únicamente los datos necesarios"

    list_artwork = {'ObjectID':artwork['ObjectID'], 
                    'Title':artwork['Title'], 
                    'ConstituentID':artwork['ConstituentID'], 
                    'Date': artwork[ 'Date'],
                    'Medium':artwork['Medium'], 
                    'Dimensions':artwork['Dimensions'],
                    'CreditLine': artwork['CreditLine'], 
                    'Department':artwork['Department'], 
                    'DateAcquired':artwork['DateAcquired']}

    lt.addLast(catalog['Artwork'], list_artwork)
    'agregar listas para ordenar'
    artist_id = artwork['ConstituentID'].split(',')

    for artist in artist_id:
        addArtworkArtist(catalog, artist.strip(), artwork)


def addArtist(catalog,artists):
    artist = {'ConstituentID':artists['ConstituentID'],
                    'DisplayName': artists['DisplayName'],
                    'Nationality':artists['Nationality'],
                    'Gender':artists['Gender'],
                    'BeginDate':artists['BeginDate'],
                    'EndDate':artists['EndDate'],
                    'Artworks':lt.newList('ARRAY_LIST')}
                    
    addArtistDate(catalog, artist['DisplayName'], artist['BeginDate'],artist['EndDate'],artist['Nationality'],artist['Gender'])
    
    lt.addLast(catalog['Artist'], artist)  
    
        
def addArtworkArtist(catalog, artist_id, artwork):
    artists = catalog['Artist']
    posartist = lt.isPresent(artists, artist_id)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
        lt.addLast(artist['Artworks'], artwork)

def addArtistDate(catalog, artist, date, deathdate, nationality, gender):
    
    if int(date) != 0 :
        adate = newArtistDate(artist,date, deathdate, nationality, gender )

        lt.addLast(catalog['ArtistDate'],adate)
    

# Funciones para creacion de datos


def newArtistDate(artist, date, deathdate, nationality, gender):
    artist_date = {'name': '', 'BeginDate':'', 'EndDate':'', 'nationality':'','gender':''}
    artist_date['name'] = artist
    artist_date['BeginDate'] = date
    artist_date['EndDate'] = deathdate
    artist_date['nationality'] = nationality
    artist_date['gender'] = gender

    return artist_date

# Funciones de consulta
def getArtistYear(catalog,año_inicial,año_final):

    

    artist_inrange = lt.newList("ARRAY_LIST")

    for artist in lt.iterator(catalog['ArtistDate']):

        if int(artist['BeginDate']) >= año_inicial and int(artist['BeginDate']) <= año_final:
        
            lt.addLast(artist_inrange, artist )

    sortYear(artist_inrange)
    return artist_inrange

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpartistyear(artist1,artist2):

    return int(artist1['BeginDate']) < int(artist2['BeginDate'])

# Funciones de ordenamiento

def sortYear(artist_inrange):

    sa.sort(artist_inrange, cmpartistyear)