import streamlit as st
from PIL import Image
import pandas as pd
from google.oauth2 import service_account
import gspread

@st.cache_resource()
def get_sideBar(title):
    st.sidebar.title(title)
    image = get_image()
    st.image(image)
    st.markdown("## [Click here for Schedule](https://www.teamsideline.com/sites/georgetown/schedule/476652/Thursday-Mens-Recreational-League)")
    st.markdown("")
    st.markdown('## [Click here for Budget](https://docs.google.com/spreadsheets/d/1AYZyMQNMqUqAaN0m9aw4U5Uc73Vi5PNcn7pKeOcFMOg/edit?usp=sharing)')

@st.cache_data()
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
    return image

@st.cache_data()
def get_image():
    image = Image.open('assets/logo.png')
    return image


credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

client = gspread.authorize(credentials)

def get_googlesheet_id():
    ##### SET NEW PROJECT ID HERE #####
    return 'dadbod_6_8_23'

@st.cache_resource()
def get_recent_data(project_id):
    sheet = client.open(project_id).sheet1
    dataframe = pd.DataFrame(sheet.get_all_records())
    return dataframe

@st.cache_data()
def data_munging(recent = True):

    dict_of_games = {'game1': 'data/dadbod_3_9_23 - lineup.csv',
                    'game2': 'data/dadbod_3_30_23 - lineup.csv',
                    'game3': 'data/dadbod_4_13_23 - lineup.csv',
                    'game4': 'data/dadbod_4_27_23 - lineup.csv',
                    'game5': 'data/dadbod_5_4_23_1 - lineup.csv',
                    'game6': 'data/dadbod_5_4_23_2 - lineup.csv',
                    }

    id_name = pd.read_csv('data/id_name.csv').set_index('id')
    dfs_list = []
    for k in dict_of_games.keys():
        df = pd.read_csv(dict_of_games[k]).set_index('id').drop(columns=['name'])
        df = df.merge(id_name, left_index=True, right_index=True)
        df.fillna(0, inplace=True)
        df.replace('', 0, inplace=True)
        df['game'] = k.replace('game', '')
        df['games_played'] = 1
        dfs_list.append(df)

    if recent == True:
        recent_id = get_googlesheet_id()
        recent_game = get_recent_data(recent_id)
        recent_game = recent_game.set_index('id').drop(columns=['name'])
        recent_game = recent_game.merge(id_name, left_index=True, right_index=True)
        recent_game.fillna(0, inplace=True)
        recent_game.replace('', 0, inplace=True)
        recent_game['game'] = str(len(dict_of_games) + 1)
        recent_game['games_played'] = 1
        dfs_list.append(recent_game)

    df_full = pd.concat(dfs_list)
    df_full[['atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'game']] = df_full[['atbats', 'walks', 'single', 'double', 'triple', 'homerun',  'game']].astype(int)
    df_full_nums = df_full[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]

    return df_full, df_full_nums

def add_cumulative_stats(df):
    df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    df['batting_average'] = (df['single'] + df['double'] + df['triple'] + df['homerun'])  / (df['atbats'] - df['walks']) * (1000)
    df['hits'] = df['single'] + df['double'] + df['triple'] + df['homerun']
    df['onbase'] = (df['hits'] + df['walks']) / df['atbats'] * (1000)
    df['slugging'] = (df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])) / df['atbats'] * (1000)
    df['onbase_plus_slugging'] = df['onbase'] + df['slugging']
    df['total_bases'] = df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])
    return df
    