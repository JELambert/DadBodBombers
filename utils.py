import streamlit as st
from PIL import Image
import pandas as pd
import json
from google.oauth2 import service_account
import gspread
import os
from googleapiclient.discovery import build

pd.set_option('future.no_silent_downcasting', True)

# Set up credentials
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/drive.readonly",
        "https://www.googleapis.com/auth/spreadsheets.readonly"
    ]
)

# Use the Drive API 
service = build('drive', 'v3', credentials=credentials)


@st.cache_resource()
def get_sideBar(title):
    st.sidebar.title(title)
    image = get_image()
    st.image(image)
    st.markdown("## [Click here for Schedule](https://www.teamsideline.com/sites/georgetown/schedule/535705/Thursday-Mens-Recreation-League)")
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
    ##### SET NEW Game ID HERE #####
    return 'dadbod_7_25_24'

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
                    'game7': 'data/dadbod_6_8_23 - lineup.csv',
                    'game8': 'data/dadbod_6_15_23 - lineup.csv',
                    'game9': 'data/dadbod_6_22_23 - lineup.csv',
                    'game10': 'data/dadbod_6_29_23 - lineup.csv',
                    'game11': 'data/dadbod_7_6_23 - lineup.csv',
                    'game12': 'data/dadbod_7_20_23 - lineup.csv',
                    'game13': 'data/dadbod_7_27_23 - lineup.csv',
                    'game14': 'data/dadbod_8_3_23 - lineup.csv',
                    'game15': 'data/dadbod_9_7_23 - lineup.csv',
                    'game16': 'data/dadbod_9_14_23 - lineup.csv',
                    'game17': 'data/dadbod_9_21_23_a - lineup.csv',
                    'game18': 'data/dadbod_9_21_23_b - lineup.csv',
                    'game19': 'data/dadbod_9_28_23 - lineup.csv',
                    'game20': 'data/dadbod_10_13_23 - lineup.csv',
                    'game21': 'data/dadbod_10_19_23 - lineup.csv',
                    'game22': 'data/dadbod_11_2_23 - lineup.csv',
                    'game23': 'data/dadbod_3_7_24 - lineup.csv',
                    'game24': 'data/dadbod_3_14_24 - lineup.csv',
                    'game25': 'data/dadbod_3_21_24 - lineup.csv',
                    'game26': 'data/dadbod_3_28_24 - lineup.csv',
                    'game27': 'data/dadbod_4_4_24 - lineup.csv',
                    'game28': 'data/dadbod_4_11_24 - lineup.csv',
                    'game29': 'data/dadbod_4_18_24 - lineup.csv',
                    'game30': 'data/dadbod_4_25_24 - lineup.csv',
                    'game31': 'data/dadbod_6_13_24 - lineup.csv',
                    'game31': 'data/dadbod_6_28_24 - lineup.csv'
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
        recent_game.loc[:, 'game'] = str(len(dict_of_games) + 1)
        recent_game.loc[:, 'games_played'] = 1
        dfs_list.append(recent_game)

    df_full = pd.concat(dfs_list)
    df_full[['atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'game']] = df_full[['atbats', 'walks', 'single', 'double', 'triple', 'homerun',  'game']].astype(int)
    df_full_nums = df_full[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]
    
    df_full['season'] = df_full.apply(add_season, axis=1)
    df_full_nums['season'] = df_full['season']

    return df_full, df_full_nums

def add_season(x):
    if x['game'] < 7:
        return 1
    elif x['game'] > 6 and x['game'] < 15:
        return 2
    elif x['game'] > 14 and x['game'] < 23:
        return 3
    elif x['game'] > 22 and x['game'] < 31:
        return 4
    else:
        return 5

def add_cumulative_stats(df_orig):
    df = df_orig.copy()
    df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    df.loc[:, 'batting_average']  = (df['single'] + df['double'] + df['triple'] + df['homerun'])  / (df['atbats'] - df['walks']) * (1000)
    df.loc[:, 'hits'] = df['single'] + df['double'] + df['triple'] + df['homerun']
    df.loc[:, 'onbase'] = (df['hits'] + df['walks']) / df['atbats'] * (1000)
    df.loc[:, 'slugging'] = (df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])) / df['atbats'] * (1000)
    df.loc[:, 'onbase_plus_slugging'] = df['onbase'] + df['slugging']
    df.loc[:, 'total_bases'] = df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])

    for c in ['single', 'double', 'triple', 'homerun', 'hits', 'total_bases']:
        newname = c + "_array"


    return df


def make_cumulative_array(player, df_full, category):
    game_list = []
    for i in df_full['game'].unique():
        game_df = df_full.loc[(df_full['game']==i) & (df_full['name']==player)]
        game_df_stats = add_cumulative_stats(game_df)
        game_df_stats['game'] = 'Game ' + str(i)
        game_list.append(game_df_stats)
    temporal = pd.concat(game_list)
    temporal['Game Number'] = temporal['game'].str.split(' ').str[1].astype(int)
    temporal = temporal.sort_values(by='Game Number')

    df_sorted = temporal.sort_values(by='game')
    hits_array = df_sorted[category].to_numpy()
    return hits_array




def return_google_markdown(file_id):
    request = service.files().get_media(fileId=file_id)
    content = request.execute()
    _, content_to_display = content.decode("utf-8").split('SKIPABOVE', 1)
    return content_to_display

def get_file_store():
    request = service.files().get_media(fileId='1K97IkXCQefclbzcKY0L9lb1ST1irNpD8')
    content = request.execute()
    json_file = content.decode("utf-8")
    json_file = json.loads(json_file)

    with open('temp_json.json', 'w') as f:
        json.dump(json_file, f)

def delete_file_store():
    os.remove('temp_json.json')

@st.cache_data()
def make_fielding():

    fielding_files = {
        'game23': 'data/fielding_3_7_24.csv', 
        'game24': 'data/fielding_3_14_24.csv',
        'game25': 'data/fielding_3_21_24.csv',
        'game26': 'data/fielding_3_28_24.csv',
        'game27': 'data/fielding_4_4_24.csv',
        'game28': 'data/fielding_4_11_24.csv',
        'game29': 'data/fielding_4_18_24.csv',
        'game30': 'data/fielding_4_25_24.csv'
    }

    fielding_dict = {}

    for f in fielding_files.keys():
        fielding = pd.read_csv(fielding_files[f])
        fielding = fielding.fillna(0)
        fielding['raw_defense'] = fielding.apply(build_raw_defense_totals, axis=1)
        
        fielding_dict[f] = {}

        fielding_dict[f]['disaggregate'] = fielding
    
        intermediate = fielding.groupby(['name', 'id'])[['raw_defense', 'E', 'EH', 'OC', 'OCH', 'OT', 'OTH', 'RM']].sum().reset_index()
        scaled = scaler(intermediate)
        fielding_dict[f]['aggregate'] = scaled

    games_disaggregate = []

    for g in fielding_dict.keys():
        games_disaggregate.append(fielding_dict[g]['disaggregate'])
    
    fullset = pd.concat(games_disaggregate)
    fullset_agg = fullset.groupby(['name', 'id'])[['raw_defense', 'E', 'EH', 'OC', 'OCH', 'OT', 'OTH', 'RM']].sum().reset_index()
    fullset_scaled = scaler(fullset_agg)
    fielding_dict['overall'] = {}
    fielding_dict['overall']['aggregate'] = fullset_scaled
    fielding_dict['overall']['disaggregate'] = fullset
    return fielding_dict

def build_raw_defense_totals(x):
    position_config = {'1B': 3, 
                        '2B': 3, 
                        '3B': 4, 
                        'SS': 5, 
                        'LF': 4, 
                        'LC': 4, 
                        'RC': 4,
                        'RF': 3, 
                        'P': 3, 
                        'C': 1}
    return ((x['E'] *-3 / position_config[x['Positions']]) + (x['OC']*position_config[x['Positions']]) + (x['OCH'] * 2 * position_config[x['Positions']]) + (x['OT']*position_config[x['Positions']]) + (x['OTH']*2 * position_config[x['Positions']]) + (x['RM']*-1 /position_config[x['Positions']]))


def scaler(intermediate):

    colname = 'DPI'

    def custom_scaler(x):
        max_val = x.max()
        min_val = x.min()
        if max_val == min_val:
            return x
        max_abs = max(abs(max_val), abs(min_val))
        scaled_values = x / max_abs
        return scaled_values

    # Apply the custom scaler to
    intermediate[colname] = custom_scaler(intermediate['raw_defense'])

    return intermediate


def make_temporal_games(df_full):
    game_list = []
    for i in df_full['game'].unique():
        game_df = df_full.loc[df_full['game']==i]
        game_df_stats = add_cumulative_stats(game_df)
        game_df_stats['game'] = 'Game ' + str(i)
        game_list.append(game_df_stats)
    temporal = pd.concat(game_list)
    temporal['Game Number'] = temporal['game'].str.split(' ').str[1].astype(int)
    temporal = temporal.sort_values(by='Game Number')

    return temporal


def make_temporal_player(df_full, player):
    game_list = []
    for i in df_full['game'].unique():
        game_df = df_full.loc[(df_full['game']==i) & (df_full['name']==player)]
        game_df_stats = add_cumulative_stats(game_df)
        game_df_stats['game'] = 'Game ' + str(i)
        game_list.append(game_df_stats)
    temporal = pd.concat(game_list)
    temporal['Game Number'] = temporal['game'].str.split(' ').str[1].astype(int)
    temporal = temporal.sort_values(by='Game Number')
    return temporal

@st.cache_data()
def make_data_dict():

    df_full, df_full_nums = data_munging()
    fielding = make_fielding()

    big_dict = {}
    big_dict['df_full'] = df_full
    big_dict['df_full_nums'] = df_full_nums
    big_dict['fielding'] = fielding
    
    ### Season disaggregates
    big_dict['df_s1'] = df_full.loc[df_full.game <7]
    big_dict['df_s2'] = df_full.loc[(df_full.game >6) & (df_full.game <15)]
    big_dict['df_s3'] = df_full.loc[(df_full.game >14) & (df_full.game<23)]
    big_dict['df_s4'] = df_full.loc[(df_full.game >22) & (df_full.game<31)]
    big_dict['df_s5'] = df_full.loc[df_full.game >30]

    ### Baseline aggregates player
    big_dict['df_agg_all'] = big_dict['df_full'].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_agg_s1'] = big_dict['df_s1'].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_agg_s2'] = big_dict['df_s2'].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_agg_s3']  = big_dict['df_s3'].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_agg_s4'] = big_dict['df_s4'].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_agg_s5'] = big_dict['df_s5'].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    
    ### Add cumulative player
    big_dict['df_cumulative_all'] = add_cumulative_stats(big_dict['df_agg_all'])
    big_dict['df_cumulative_s1']  = add_cumulative_stats(big_dict['df_agg_s1'])
    big_dict['df_cumulative_s2'] = add_cumulative_stats(big_dict['df_agg_s2'])
    big_dict['df_cumulative_s3'] = add_cumulative_stats(big_dict['df_agg_s3'])
    big_dict['df_cumulative_s4'] = add_cumulative_stats(big_dict['df_agg_s4'])
    big_dict['df_cumulative_s5'] = add_cumulative_stats(big_dict['df_agg_s5'])

    ### Make game temporal data
    big_dict['temporal_all'] = make_temporal_games(big_dict['df_full'])
    big_dict['temporal_s1'] = make_temporal_games(big_dict['df_s1'])
    big_dict['temporal_s2'] = make_temporal_games(big_dict['df_s2'])
    big_dict['temporal_s3'] = make_temporal_games(big_dict['df_s3'])
    big_dict['temporal_s4'] = make_temporal_games(big_dict['df_s4'])
    big_dict['temporal_s5'] = make_temporal_games(big_dict['df_s5'])

    ### Baseline aggregates team
    big_dict['df_games_all'] = df_full.groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_games_s1']  = df_full.loc[df_full.game <7].groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_games_s2'] = df_full.loc[(df_full.game >6) & (df_full.game <15)].groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_games_s3'] = df_full.loc[(df_full.game >14) & (df_full.game<23)].groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_games_s4'] = df_full.loc[(df_full.game >22) & (df_full.game<31)].groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    big_dict['df_games_s5'] = df_full.loc[df_full.game >30].groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()


    big_dict['player'] = {}

    ### Make player temporal data
    for i in big_dict['df_full'].name.unique():
        big_dict['player'][i] = {}
        for df in ['df_full', 'df_s1', 'df_s2', 'df_s3', 'df_s4', 'df_s5']:    
            big_dict['player'][i][df] = make_temporal_player(big_dict[df], i)

    return big_dict

