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
               'ArtworkArtist':lt.newList(list_type,
                                 cmpfunction=""),
                }

    catalog['Artwork'] = lt.newList(list_type, cmpfunction=cmpartistID)
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
                    'Classification': artwork['Classification'],
                    'Dimensions':artwork['Dimensions'],
                    'CreditLine': artwork['CreditLine'], 
                    'Department':artwork['Department'], 
                    'DateAcquired':artwork['DateAcquired'],
                    'Weight': artwork['Weight (kg)'],
                    'Circumference': artwork['Circumference (cm)'],
                    'Depth': artwork['Depth (cm)'],
                    'Diameter':artwork['Diameter (cm)'],
                    'Height': artwork['Height (cm)'],
                    'Length': artwork['Length (cm)'],
                    'Width':artwork['Width (cm)']}

    lt.addLast(catalog['Artwork'], artwork)
    
    addArtworkDate(catalog,artwork['Title'],artwork['DateAcquired'],artwork['ConstituentID'], artwork['Medium'], artwork['Dimensions'] , artwork['CreditLine'])
    """
    A medida que se lee el archivo, se van extrayendo los artists_id para poder crear una lista que relacione 
    a los artistas con sus obras de arte.
    """
    artist_id = artwork['ConstituentID'].split(',')

    for artist in artist_id:
        addArtworkArtist(catalog, artist, artwork)
        #addArtistArtwork(catalog,artist, artwork)

"""
    
def addArtistArtwork(catalog, artist_id, artwork):
    
    artistsartwork = catalog['ArtworkArtist']
    artists = catalog['Artist']
    posartist = lt.isPresent(artists, artist_id)
    if posartist > 0:
        artist = lt.getElement(artists, posartist)
        artwarti = {'ObjectID':artwork['ObjectID'],
                    'Title': artwork['Title'],
                    'ConstituentID':artist['ConstituentID'],
                    'DisplayName':artist['DisplayName']}
        lt.addLast(artistsartwork, artwarti)

            

def addNationality(catalog,artists):
    
    Se utiliza un diccionario para extraer únicamente los datos necesarios del archivo de excel Artists.csv y
    con base en ese diccionario se crean otras listas útiles para resolver los requerimientos.
    

    nationality = {'Nationality':artists['Nationality'],
                    'Artworks':lt.newList('ARRAY_LIST')}
                    
    lt.addLast(catalog['Nationality'], nationality) 

    nationalities = nationality['Nationality'].split(',')
    for place in nationalities:
        addArtworkNationality(catalog, place, nationality)

    print(nationality)
"""
    

def addArtworkNationality(catalog, nationalities, nationality):
   
    nations = catalog['Artist']
    postnationality = lt.isPresent(nations, nationalities)

    if postnationality > 0:
        nationality = lt.getElement(nations, postnationality)
        lt.addLast(nationality['Artworks'], nationality)

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


def getArtistNationality(catalog,artists):
    nationalities = lt.newList('ARRAY_LIST', cmpfunction=cmpArtistNationality)         
    for artist in lt.iterator(catalog['Artist']):
        
        for n in lt.iterator(artist['Nationality']):
                nationality = n['Nationality']
                posnationality = lt.isPresent(nationalities, nationality)

                if posnationality > 0:
                    nation = lt.getElement(nationality,posnationality)
                    lt.addLast(nationalities[nation], artists)
                else:
                    nation = {nationality: lt.newList('ARRAY_LIST')}

                    lt.addLast(nation, artists)
                    lt.addLast(nationalities,nation)
                    #tecnique es la tecnica encontrada en la lista de tecnicas


def getTransportationCost(catalog, dpto):
    costo_total = 0
    transp_cost = lt.newList('ARRAY_LIST')
    artworksBydpto = lt.newList('ARRAY_LIST')


    for artwork in lt.iterator(catalog['Artwork']):

        if artwork['Department'].lower() == dpto.lower():

            lt.addLast(artworksBydpto, artwork)

    for artwork in lt.iterator(artworksBydpto):
        artwork_filtrada = {'Title': artwork['Title'],
                            'Artist/s':artwork['ConstituentID'],
                            'Classification': artwork['Classification'],
                            'Date':artwork['Date'],
                            'Medium':artwork['Medium'],
                            'Dimensions':artwork['Dimensions']}
        weight = artwork['Weight']

        if artwork['Weight'] == '':
            weight = 0
        else: 
            weight = float(artwork['Weight'])

        cost_weight=round(((weight)*72),2)
        cost_a = round(((cost_Area(artwork))/10000),2) 
        cost_vol = round(((cost_volume(artwork))/1000000),2)

        if cost_weight == 0 and cost_a == 0 and cost_vol == 0:
            costo_total =+ 48.00
            cost = {'Artwork':artwork_filtrada, 
                    'Cost':48.00}

            lt.addLast(transp_cost,cost)

        elif cost_weight > cost_vol and cost_weight > cost_a:
            
                costo_total =+ cost_weight
                cost = {'Artwork':artwork_filtrada, 
                        'Cost':cost_weight}

                lt.addLast(transp_cost,cost)

        elif cost_a > cost_weight and cost_a > cost_vol:
            
                costo_total =+ cost_a
                cost = {'Artwork':artwork_filtrada, 
                        'Cost':cost_a}

                lt.addLast(transp_cost,cost)

        elif cost_vol > cost_a and cost_vol > cost_weight:

                costo_total =+ cost_vol
                cost = {'Artwork':artwork_filtrada, 
                        'Cost':cost_vol}

                lt.addLast(transp_cost,cost)
        
    copy=lt.subList(transp_cost,1,lt.size(transp_cost))
    sortTranspOld(copy)
    sortTransportation(transp_cost)
    return transp_cost, costo_total, copy
    
def cost_Area(artwork):
    pi = math.pi
    length = artwork['Length']
    height = artwork['Height']
    width = artwork['Width']
    diameter =artwork['Diameter']

    #area de la forma largo por altura
    if artwork['Length'] == '':
        length = 0
    else: 
        length = float(length)
    if artwork['Height'] == '':
        height = 0
    else: 
        height = float(height)   
    
    if artwork['Diameter'] == '':
        diameter = 0
    else: 
        diameter = float(diameter)

    if artwork['Width'] == '':
        width = 0
    else: 
        width = float(width)


    cost_area1 = (length*height)*72
    cost_area5 = (width*height)*72
    #area de circulo    
    cost_area2 = (pi*((diameter)/2)**2)*72
    #area cilindro
    cost_area3 = (2*(pi*(diameter)/2)*height) + 2*((math.pi*((diameter)/2)**2))*72
    #area esfera
    cost_area4 = (4*(pi*(diameter)/2)**2)*72

    if cost_area1 > cost_area2 and cost_area1 >cost_area3 and cost_area1 > cost_area4 and cost_area1 > cost_area5:
        return cost_area1
    elif cost_area2 > cost_area1 and cost_area2 > cost_area3 and cost_area2 > cost_area4 and cost_area2 > cost_area5: 
        return cost_area2
    elif cost_area3 > cost_area1 and cost_area3 > cost_area2 and cost_area3 > cost_area4 and cost_area3 > cost_area5 :
        return cost_area3
    elif cost_area4 > cost_area1 and cost_area4 > cost_area2 and cost_area4 > cost_area3 and cost_area4 > cost_area5 :
        return cost_area4
    else: 
        return cost_area5


def cost_volume(artwork):

    pi = math.pi

    length = artwork['Length']
    height = artwork['Height']
    diameter = artwork['Diameter']
    width = artwork['Width']
    depth = artwork['Depth']

    if artwork['Width'] == '':
        width = 0
    else: 
        width = float(width)
    if artwork['Length'] == '':
        length = 0
    else: 
        length = float(length)
    if artwork['Height'] == '':
        height = 0
    else: 
        height = float(height)
    if artwork['Diameter'] == '':
        diameter = 0
    else: 
        diameter = float(diameter)
    if artwork['Depth'] == '':
        depth = 0
    else: 
        depth = float(depth)

    #volumen de la forma longitud por altura por ancho

    cost_vol1 = (length*height*width)*72
    cost_vol2 = (length*height*depth)*72

    #volumen esfera
    cost_vol3 = ((4/3)*((pi*(diameter)/2)**3))*72
    #volumen cilindro
    cost_vol4 = ((pi*((diameter)/2)**2)*height)*72

    if cost_vol1 > cost_vol2 and cost_vol1 > cost_vol3 and cost_vol1 > cost_vol4:
        return cost_vol1
    elif cost_vol2 > cost_vol1 and cost_vol2 > cost_vol3 and cost_vol2 > cost_vol4:
        return cost_vol2
    elif cost_vol3 > cost_vol1 and cost_vol3 > cost_vol2 and cost_vol3 > cost_vol4:
        return cost_vol3
    
    else: 
        return cost_vol4


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

def cmpArtistNationality(artist):

    if artist["Nationality"] in artist ["Nationality"]:
        return 0 
    else:
        return -1
def cmpTecniquesize(tec1,tec2):

    return (lt.size(tec1['Artworks'])) > (lt.size(tec2['Artworks']))

def cmpTranspCost(cost1,cost2):

    return int(cost1['Cost']) > int(cost2['Cost'])

def cmpTranspOld (artwork1,artwork2):
    #date1 = artwork1['Artwork']['Date']
    #date2 = artwork2['Artwork']['Date']
    if artwork1['Artwork']['Date'] != '' and artwork2['Artwork']['Date'] != '':
        return int(artwork1['Artwork']['Date']) <  int(artwork2['Artwork']['Date'])

# Funciones de ordenamiento

def sortYear_Artist(artist_inrange):

    ms.sort(artist_inrange, cmpartistyear)


def sortYear_Artwork(artwork_inrange):

    ms.sort(artwork_inrange, cmpartworkyear)

def sortTecnique_size(tecnique_list):
    
    ms.sort(tecnique_list, cmpTecniquesize)

def sortTransportation(transp_cost):

    ms.sort(transp_cost, cmpTranspCost)

def sortTranspOld(copy):
    ms.sort(copy, cmpTranspOld)
      