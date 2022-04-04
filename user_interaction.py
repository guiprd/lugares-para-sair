from helper import filterByNonVisitedPlace, filterByVisitedPlaces, filterByPlace, filterByCity, randomizePlace

layout1 = '''
#############################################################
#############################################################
############# Bem-Vindo ao Sorteador de Lugares #############
#############################################################
#############################################################
'''

firstActions = '''
1 - Escolher novo lugar
2 - Repetir um lugar
3 - Escolher aleatoriamente
9 - Sair
'''

switcher1 = {"1": "filtrar", "2": "novo", "3": "repetir"}
switcherList1 = ["filtrar", "Escolher novo lugar", "Repetir um lugar"]

secondActions = '''
1 - Filtrar por Estabelecimento
2 - Filtrar por Cidade
8 - Voltar
9 - Sair
'''
switcher2 = {"1": "aleatorio", "9": "sair"}
switcherList2 = ["Filtrar por estabelecimento", "Filtrar por cidade", "Filtrar por status Visitado"]

thirdActions = '''
1 - Início
9 - Sair
'''

switcher3 = {"1": "aleatorio", "2": "voltar"}
switcherList3 = ["inicio"]

switcher = {"1": {"1": {"1": "aleatorio"}, "2": ""}, "2": "aleatorio", "3": "repetir"}

actionsList = [firstActions, secondActions, thirdActions]


def userImput(action=firstActions, interactions=0):
    try:
        numInput = int(input("Escolha uma das opções abaixo:" + action))
    except:
        print("Insira uma opção válida.")
        userImput(action)
    return numInput


def interactionLogic(action=firstActions, interactions=0):
    while True:
        print("\n")
        numInput = userImput(action)
        if numInput != 9:
            if (interactions == 1 or interactions == 2) and numInput == 8:
                action, interactions = actionsList[interactions - 1], interactions - 1
                continue
            else:
                if interactions == 0:
                    if numInput == 1:
                        df = filterByNonVisitedPlace()
                        action, interactions = actionsList[interactions + 1], interactions + 1
                        continue
                    if numInput == 2:
                        df = filterByVisitedPlaces()
                        action, interactions = actionsList[interactions + 1], interactions + 1
                        continue
                    if numInput == 3:
                        print("\n")
                        print(randomizePlace())
                        action, interactions = actionsList[2], 2
                        continue
                if interactions == 1:
                    if numInput == 1:
                        print(df["Estabelecimento"])
                        print("Digite o estabelecimento que deseja filtrar:")
                        place = input().lower()
                        df_filtered_places = filterByPlace(df, place)
                        print("\n")
                        print("Local escolhido:")
                        print(df_filtered_places)
                        action, interactions = actionsList[interactions + 1], interactions + 1
                        continue
                    if numInput == 2:
                        print(df["Cidade"].drop_duplicates())
                        print("Digite a cidade que deseja filtrar:")
                        city = input().lower()
                        df_filtered_cities = filterByCity(df, city)
                        print("\n")
                        print(randomizePlace(df_filtered_cities))
                        action, interactions = actionsList[interactions + 1], interactions + 1
                        continue
                if interactions == 2:
                    if numInput == 1:
                        action, interactions = actionsList[0], 0
                        continue
        print("Fechando a aplicação... Obrigado por utilizar o Sorteador de Lugares!")
        exit()
