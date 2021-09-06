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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newCatalog(list_type = 'ARRAY_LIST'):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'Artwork': None,
               'Artist': None,
               'Artist_ID_Nationality': None,
               'Artwork_ID':None,
               'ArtworkArtist': None,
               'Tecnique': None,
                }

    catalog['Artwork'] = lt.newList(list_type)
    catalog['Artist'] = lt.newList(list_type,
                                    cmpfunction=cmpartist)
    catalog['ArtworkArtist'] = lt.newList(list_type,
                                 cmpfunction=cmpartwork_artist)
    catalog['Tecnique'] = lt.newList(list_type,
                                 cmpfunction=cmptecnique)


    return catalog

# Funciones para agregar informacion al catalogo


def addArtwork(catalog, artwork):

    list_artwork = {'ObjectID':artwork['ObjectID'], 'Title':artwork['Title'], 'ConstituentID':artwork['ConstituentID'], 'Date': artwork[ 'Date'],
     'Medium':artwork['Medium'], 'Dimensions':artwork['Dimensions'],'CreditLine': artwork['CreditLine'], 'Department':artwork['Department'] }

    lt.addLast(catalog['Artwork'], list_artwork)
    
    artist_id = artwork['ConstituentID'].split(',')

    for artist in artist_id:
        addArtworkArtist(catalog, artist.strip(), artwork)


def addArtist(catalog,artists):
    list_artist = {'ConstituentID':artists['ConstituentID'], 'DisplayName': artists['DisplayName'], 'Nationality':artists['Nationality'],
    'Gender':artists['Gender'], 'BeginDate':artists['BeginDate'], 'EndDate':artists['EndDate']}
    
    lt.addLast(catalog['Artist'], list_artist)   
        
def addArtworkArtist(catalog, artist_id, artwork):
  
  
    pass


def addArtist_ID(catalog, artists):
    pass



# Funciones para creacion de datos

def newArtist(name, ID):

    artist = {'name':'','Constituent_ID':0,'Artworks':None,'Date':0}
    artist['name'] = name
    artist['Constituent_ID'] = ID
    artist['Artworks'] = lt.newList('ARRAY_LIST')

    return artist



# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpartist():
    pass

def cmpartist_ID():
    pass

def cmpartwork_ID():
    pass

def cmptecnique():
    pass

def cmpartwork_artist():
    pass

# Funciones de ordenamiento