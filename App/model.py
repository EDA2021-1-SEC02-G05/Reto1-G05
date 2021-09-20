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


"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""


# Construccion de modelos
def newCatalog(list_type):
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
                    'DateAcquired':artwork['DateAcquired']}

    lt.addLast(catalog['Artwork'], artwork)
    
    addArtworkDate(catalog,artwork['Title'],artwork['DateAcquired'],artwork['ConstituentID'], artwork['Medium'], artwork['Dimensions'] , artwork['CreditLine'])
    
    artist_id = artwork['ConstituentID'].split(',')
    for artist in artist_id:
        addArtworkArtist(catalog, artist, artwork)


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

    #print(artwork_inrange)
    return artwork_inrange

def getArtistTecnique(catalog,name):
    tecniques = lt.newList('ARRAY_LIST', cmpfunction=cmpArtistTecnique)
    
    for artist in lt.iterator(catalog['Artist']):

        if artist['DisplayName'].lower() == name.lower():

            for artwork in lt.iterator(artist['Artworks']):
                tecnique = artwork['Medium']
                postechnique = lt.isPresent(tecniques, tecnique)
                
                if postechnique > 0:
                    tec = lt.getElement(tecnique,postechnique)
                    lt.addLast(tecniques[tec], artwork)
                else:
                    tec = {tecnique: lt.newList('ARRAY_LIST')}

                    lt.addLast(tec, artwork)
                    lt.addLast(tecniques,tec)
        break

def getArtistNationality(catalog,nationality):
    nationalities = lt.newList('ARRAY_LIST', cmpfunction=cmpartistID)
    
    for artist in lt.iterator(catalog['Artist']):

        if artist['Nationality'].lower() == nationality.lower():

            for artwork in lt.iterator(artist['Artworks']):
                national = artwork['ConstituentID']
                exists = lt.isPresent(nationalities, national)
                
                if exists > 0:
                    n = lt.getElement(national,exists)
                    lt.addLast(nationalities[n], artwork)
                else:
                    n = {national: lt.newList('ARRAY_LIST')}

                    lt.addLast(n[national], artwork)
                    lt.addLast(nationalities,n)
        break                

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpartistyear(artist1,artist2):

    return int(artist1['BeginDate']) < int(artist2['BeginDate'])


def cmpartworkyear(artwork1,artwork2):
    #date_1 = artwork1['DateAcquired'].split("-") 2020-09-10 [2020,09,10]
    #date_2 = artwork2['DateAcquired'].split("-")

    if artwork1['DateAcquired'] != '' and artwork2['DateAcquired'] != '':

        date_1 = d.date.fromisoformat(artwork1['DateAcquired'])
        date_2 = d.date.fromisoformat(artwork2['DateAcquired'])

        #d1 = d.datetime(int(date_1[0]),int(date_1[1]),int(date_1[2]))
        #d2 = d.datetime(int(date_2[0]),int(date_2[1]), int(date_2[2]))

        return date_1 < date_2

def cmpartistID(artistid1,artist):
    if (artistid1 in artist['ConstituentID']):
        return 0
    else:
        return -1

def cmpArtistTecnique(tecnique1, artwork):

    if (tecnique1.lower() in artwork['Medium'].lower()):
        return 0 
    else:
        return -1

# Funciones de ordenamiento

def sortYear_Artist(artist_inrange):

    ms.sort(artist_inrange, cmpartistyear)


#def sortYear_Artwork(artwork_inrange):

#        ms.sort(artwork_inrange, cmpartworkyear)

##PARTE DEL LABORATORIO

def sortYear_Artwork(catalog, algo_ord, tamano_muestra):
    
    muestra = lt.subList(catalog['Artwork'], 1, tamano_muestra)

    if algo_ord.lower() == 'merge sort':

        start_time = time.process_time()
        sorted_list = ms.sort(muestra, cmpartworkyear)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list


    elif algo_ord.lower() == 'quick sort':

        start_time = time.process_time()
        sorted_list = qs.sort(muestra, cmpartworkyear)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

       
    elif algo_ord.lower() == 'shell sort':

        start_time = time.process_time()
        sorted_list = ss.sort(muestra, cmpartworkyear)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list

    elif algo_ord.lower() == 'insertion sort':
        
        start_time = time.process_time()
        sorted_list = iss.sort(muestra, cmpartworkyear)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)*1000
        return elapsed_time_mseg, sorted_list
        