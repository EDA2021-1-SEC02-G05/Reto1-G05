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
 """

import config as cf
import model
import csv
import time

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros}

def initCatalog():

    """
    Inicializa la estructura del catalogo.
    """

    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y carga los datos en la
    estructura de datos seleccionada
    """
    loadArtists(catalog)
    loadArtworks(catalog)

def loadArtworks(catalog):

    """
    Carga el archivo .csv de los artworks en la respectiva lista 
    """
    artworksfile = cf.data_dir + 'MoMA/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artworksfile, encoding='utf-8'))
    for artworks in input_file:
        model.addArtwork(catalog, artworks)

def loadArtists(catalog):
    """
    Carga el archivo .csv de los artistas en la respectiva lista 
    """
    artistsfile = cf.data_dir + 'MoMA/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artistsfile, encoding='utf-8'))
    for artist in input_file:
        model.addArtist(catalog, artist)

# Funciones de ordenamiento
def sortYear_Artist(catalog):
    """
    Ordena a los artistas por fecha de nacimiento
    """
    model.sortYear_Artist(catalog)

def sortYear_Artwork(catalog):
    """
    Ordena a las obras de arte por fecha de adquisición
    """
    model.sortYear_Artwork(catalog)
    

#PARTE DEL LAB

#def sortYear_Artwork(catalog, algo_ord, tamano_muestra):
    
#    return model.sortYear_Artwork(catalog, algo_ord, tamano_muestra)
    

# Funciones de consulta sobre el catálogo

def getArtistYear(catalog,año_inicial, año_final):

    """
    REQ 1
    Llama a la función en el model para poder obtener una lista ordenada de menor a mayor de aquellos artistas que
    nacieron en un rango de fechas dadas. 
    """

    artist = model.getArtistYear(catalog, año_inicial, año_final)
    return artist

def getArtworkYear(catalog,año_inicial, año_final):

    """
    REQ 2
    Llama a la función en el model para poder obtener una lista ordenada de menor a mayor de aquellas obras de arte que
    fueron adquiridas en un rango de fechas dadas. 
    """

    artwork = model.getArtworkYear(catalog, año_inicial, año_final)
    return artwork

def getArtistTecnique(catalog,name):

    """
    REQ 3
    Llama a la función en el model para poder obtener una lista clasificada por técnica de las obras de un artista dado 
    """

    tecnique = model.getArtistTecnique(catalog, name)
    return tecnique

def getArtistNationality(catalog):

    """
    REQ 4
    Llama a la función en el model para poder obtener una lista clasificando las obras por las nacionalidades de sus artistas 
    """

    nationality = model.getArtistNationality(catalog)
    return nationality

def getTransportationCost(catalog,dpto):
    
    """
    REQ 5
    Llama a la función en el model para poder obtener una lista con los costos asociados a transportar las obras de arte de un dpto especifico
    """

    transport_cost = model.getTransportationCost(catalog,dpto)
    return transport_cost