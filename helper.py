import pandas as pd
import random


def getPlaces():
    with pd.ExcelFile("lugares_visitar.xlsx") as xlsx:
        df_all_places = pd.read_excel(xlsx)
        df_all_places_lower = df_all_places.copy()
        df_all_places_lower["Cidade"], df_all_places_lower["Estabelecimento"] = df_all_places_lower["Cidade"].str.lower(), df_all_places_lower["Estabelecimento"].str.lower()
    return df_all_places_lower


###############################
######### First filter ########
###############################
def filterByVisitedPlaces(df_places=getPlaces()):
    df_new_places = df_places[df_places["Visitado"] == "S"].copy()
    return reIndex(df_new_places)


def filterByNonVisitedPlace(df_places=getPlaces()):
    df_visited = df_places[df_places["Visitado"] == "N"].copy()
    return reIndex(df_visited)


###############################
######## Second filter ########
###############################
def filterByCity(df_places=getPlaces(), city=""):
    df_places_by_city = df_places[df_places["Cidade"] == city].copy()
    return reIndex(df_places_by_city)


def filterByPlace(df_places=getPlaces(), place=""):
    df_places_by_city = df_places[df_places["Estabelecimento"] == place]
    return reIndex(df_places_by_city)


def randomizePlace(df_places=getPlaces()):
    df_places["Cidade"] = df_places["Cidade"].str.title()
    df_places["Estabelecimento"] = df_places["Estabelecimento"].str.title()
    place = df_places.iloc[random.randint(0, len(df_places) - 1)]
    return place


def reIndex(df_places=getPlaces()):
    ls = list(range(len(df_places)))
    pdIndex = pd.Index(ls)
    return df_places.set_index(pdIndex)
