############## IMPORTATION DES PACKAGES #### IMPORTATION DES PACKAGES #### IMPORTATION DES PACKAEGES #################################################################

import streamlit as st
import pandas as pd

######################################## ENTETE ET PRESENTATION DE L'APPLICATION #######################################################

st.markdown("<h1 style='text-align: center; color: white;'>RUFF internal Data App 🚘</h1>", unsafe_allow_html=True)

st.markdown("""
 
Cette application Data Engineering de la Compagnie RUFF (Riders Under Falilou Fall) déployée en interne permet au Data Scientist de cette 
Compagnie
de télécharger des données propres 
des (voitures, motos et scooters) en vente au Senegal et sur les voitures en location. 
Dans sa version stable l'application inclura une technologie de streaming de données (Data Streaming) qui permettra de scraper, nettoyer, organiser et stocker
des flux continus 
de données en temps réel. Des données qui seront scrapées sur Dakar-auto, Expat-Dakar et les autres plateformes e-commerce dédiées du Sénégal.
    
""")

################################################### BARRE DE RECHERCHE #################################################################


# Chargement de tous les fichiers CSV 
file_paths = [
    'data/Location_Voitures_Datas.csv',
    'data/Vente_Motos_Scooters_Datas.csv',
    'data/Vente_Voitures_Datas.csv',
    'data/WebScraper-Location-Voitures-Datas.csv',
    'data/WebScraper-Vente-Motos-Scooters-Datas.csv',
    'data/WebScraper-Vente-Voitures-Datas.csv'
]

# Dictionnaire pour stocker les DataFrames
dataframes = {}

for path in file_paths:
    try:
        df = pd.read_csv(path)
        dataframes[path] = df
    except FileNotFoundError:
        st.error(f'Fichier non trouvé: {path}')
    except pd.errors.EmptyDataError:
        st.error(f'Le fichier est vide: {path}')
    except pd.errors.ParserError:
        st.error(f'Erreur de parsing dans le fichier: {path}')
    except Exception as e:
        st.error(f'Une erreur est survenue avec le fichier {path}: {e}')

# Titre de l'application
st.title('')

# Barre de recherche
search_term = st.text_input('Recherchez ici un terme ou une valeur dans les données :')

# Filtrage et affichage des résultats
if search_term:
    for path, df in dataframes.items():
        st.write(f"##### Résultats pour '{search_term}' dans {path}")
        filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search_term, case=False).any(), axis=1)]
        st.write(filtered_df)
else:
    st.write("")

    


#################################################### BEAUTIFULSOUP ######################################################################



# Titre de la boîte de boutons
st.write("### Beautiful_Soup")

# Fonction de loading des données
def load_(dataframe,BeautifulSoup , key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(BeautifulSoup,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 13px;
    height: 3em;
    width: 27em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('data/Location_Voitures_Datas.csv'), 'Location de Voitures', '1')
load_(pd.read_csv('data/Vente_Motos_Scooters_Datas.csv'), 'Vente de Motos et Scooters', '2')
load_(pd.read_csv('data/Vente_Voitures_Datas.csv'), 'Vente de Voitures', '3')


######################################################## WEBSCRAPER ##############################################################

st.write("### Web_Scraper")

# Fonction de loading des données
def load_(dataframe, WebScraper, key) :
    st.markdown("""
    <style>
    div.stButton {text-align:center}
    </style>""", unsafe_allow_html=True)

    if st.button(WebScraper,key):
      
        st.subheader('Display data dimension')
        st.write('Data dimension: ' + str(dataframe.shape[0]) + ' rows and ' + str(dataframe.shape[1]) + ' columns.')
        st.dataframe(dataframe)

# définir quelques styles liés aux box
st.markdown('''<style> .stButton>button {
    font-size: 13px;
    height: 3em;
    width: 27em;
}</style>''', unsafe_allow_html=True)

          
# Charger les données 
load_(pd.read_csv('data/WebScraper-Location-Voitures-Datas.csv'), 'Location de Voitures', '4')
load_(pd.read_csv('data/WebScraper-Vente-Motos-Scooters-Datas.csv'), 'Vente de Motos et Scooters', '5')
load_(pd.read_csv('data/WebScraper-Vente-Voitures-Datas.csv'), 'Vente de Voitures', '6')
 

#################################### BAS DE PAGE (FOOTER) #########################################################################################
st.markdown("""
 
* **Source de Données :** [Dakar-auto](https://dakar-auto.com/)
* **Designed and developed by :** @ Mohamed Falilou Fall - Juillet 2024
""")
