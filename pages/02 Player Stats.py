import streamlit as st
import pandas as pd
import os
import random
import datetime
import json
from PIL import Image

from google.oauth2 import service_account
from gsheetsdb import connect
import gspread

from Home import get_sideBar, get_data, get_project_id

st.set_page_config(layout="wide")

@st.cache_data()
def manage_dfs(df, recent=True):
    game1 = pd.read_csv('data/dadbod_3_9_23 - lineup.csv').set_index('id').drop(columns=['name'])
    id_name = pd.read_csv('data/id_name.csv').set_index('id')
    
    game1 = game1.merge(id_name, left_index=True, right_index=True)
    game1.fillna(0, inplace=True)
    game1.replace('', 0, inplace=True)
    game1['games_played'] = 1

    game2 = pd.read_csv('data/dadbod_3_30_23 - lineup.csv').set_index('id').drop(columns=['name'])
    game2 = game2.merge(id_name, left_index=True, right_index=True)
    game2.fillna(0, inplace=True)
    game2.replace('', 0, inplace=True)
    game2['games_played'] = 1

    game3 = pd.read_csv('data/dadbod_4_13_23 - lineup.csv').set_index('id').drop(columns=['name'])
    game3 = game3.merge(id_name, left_index=True, right_index=True)
    game3.fillna(0, inplace=True)
    game3.replace('', 0, inplace=True)
    game3['games_played'] = 1

    game4 = pd.read_csv('data/dadbod_4_27_23 - lineup.csv').set_index('id').drop(columns=['name'])
    game4 = game4.merge(id_name, left_index=True, right_index=True)
    game4.fillna(0, inplace=True)
    game4.replace('', 0, inplace=True)
    game4['games_played'] = 1

    game5 = pd.read_csv('data/dadbod_5_4_23_1 - lineup.csv').set_index('id').drop(columns=['name'])
    game5 = game5.merge(id_name, left_index=True, right_index=True)
    game5.fillna(0, inplace=True)
    game5.replace('', 0, inplace=True)
    game5['games_played'] = 1

    game6 = pd.read_csv('data/dadbod_5_4_23_2 - lineup.csv').set_index('id').drop(columns=['name'])
    game6 = game6.merge(id_name, left_index=True, right_index=True)
    game6.fillna(0, inplace=True)
    game6.replace('', 0, inplace=True) 
    game6['games_played'] = 1


    game1[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game1[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    game2[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game2[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    game3[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game3[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    game4[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game4[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    game5[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game5[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    game6[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game6[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    


    game1numsonly = game1[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game2numsonly = game2[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game3numsonly = game3[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game4numsonly = game4[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game5numsonly = game5[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game6numsonly = game6[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]

    if recent == True:
        df = df.set_index('id').drop(columns=['name'])
        df = df.merge(id_name, left_index=True, right_index=True)
        recent_game = df
        recent_game.fillna(0, inplace=True)
        recent_game.replace('', 0, inplace=True)
        recent_game[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = recent_game[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
        dfnumsonly = df[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]

        merged_df = dfnumsonly.add(game1numsonly, fill_value=0)
        merged_df = merged_df.add(game2numsonly, fill_value=0)
        merged_df = merged_df.add(game3numsonly, fill_value=0)
        merged_df = merged_df.add(game4numsonly, fill_value=0)
        merged_df = merged_df.add(game5numsonly, fill_value=0)
        merged_df = merged_df.add(game6numsonly, fill_value=0)

        merged_df = merged_df.merge(id_name, left_index=True, right_index=True)
        full_set = merged_df.reset_index()
    
        return full_set, game1, game2, game3, game4, game5, game6, recent_game

    else:
        merged_df = game1numsonly.add(game2numsonly, fill_value=0)
        merged_df = merged_df.add(game3numsonly, fill_value=0)
        merged_df = merged_df.add(game4numsonly, fill_value=0)
        merged_df = merged_df.add(game5numsonly, fill_value=0)
        merged_df = merged_df.add(game6numsonly, fill_value=0)

        merged_df = merged_df.merge(id_name, left_index=True, right_index=True)
        full_set = merged_df.reset_index()
    
        return full_set, game1, game2, game3, game4, game5, game6



def batting_average(df):
    df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    df['batting_average'] = (df['single'] + df['double'] + df['triple'] + df['homerun'])  / (df['atbats'] - df['walks']) * (1000)
    df['hits'] = df['single'] + df['double'] + df['triple'] + df['homerun']
    df['onbase'] = (df['hits'] + df['walks']) / df['atbats'] * (1000)
    df['slugging'] = (df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])) / df['atbats'] * (1000)
    df['onbase_plus_slugging'] = df['onbase'] + df['slugging']
    df['total_bases'] = df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])
    return df

def labeler():

    st.markdown("# Dad Bod Bombers")
    st.markdown("--------")

    project_id = get_project_id()
    temp_df = get_data(project_id)
    full_set, game1, game2, game3, game4, game5, game6 = manage_dfs(temp_df, recent=False)
    df = batting_average(full_set)

    with st.sidebar: get_sideBar('Player Stats')

    player = st.selectbox('Select a player', sorted(df['name'].unique()))

    g1 = batting_average(game1[game1['name'] == player])
    g2 = batting_average(game2[game2['name'] == player])
    g3 = batting_average(game3[game3['name'] == player])
    g4 = batting_average(game4[game4['name'] == player])
    g5 = batting_average(game5[game5['name'] == player])
    g6 = batting_average(game6[game6['name'] == player])

    #rg = batting_average(recent_game[recent_game['name'] == player])
    g1['game'] = 'Game 1'
    g2['game'] = 'Game 2'
    g3['game'] = 'Game 3'
    g4['game'] = 'Game 4'
    g5['game'] = 'Game 5'
    g6['game'] = 'Game 6'
    #rg['game'] = 'Game 4'

    temporal = pd.concat([g1, g2, g3, g4, g5, g6])
    df = df[df['name'] == player]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Player Batting Average:")
        st.markdown("### Overall: " + str(df['batting_average'].astype(int).mean()))
        st.line_chart(data=temporal, x='game', y='batting_average')
        st.markdown('')
        st.markdown('')
        st.markdown('Player Runs Scored:')
        st.markdown("### Overall: " + str(df['run'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='run')
        
        st.markdown('')

        st.markdown('Player Hits:')
        st.markdown("### Overall: " + str(df['hits'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='hits')
        st.markdown('')

        st.markdown("Player On Base Percentage:")
        st.markdown("### Overall: " + str(df['onbase'].astype(int).mean()))
        st.line_chart(data=temporal, x='game', y='onbase')
        st.markdown('')

        st.markdown("Player Slugging Percentage:")
        st.markdown("### Overall: " + str(df['slugging'].astype(int).mean()))
        st.line_chart(data=temporal, x='game', y='slugging')


    with col2:

        st.markdown('Player RBI:')    
        st.markdown("### Overall: " + str(df['rbi'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='rbi')
        st.markdown('')

        st.markdown('Player Singles:')
        st.markdown("### Overall: " + str(df['single'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='single')
        st.markdown('')
        
        st.markdown('Player Doubles:')
        st.markdown("### Overall: " + str(df['double'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='double')
        st.markdown('')


        st.markdown('Player Triples:')
        st.markdown("### Overall: " + str(df['triple'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='triple')
        st.markdown('')

        st.markdown('Player HR:')
        st.markdown("### Overall: " + str(df['homerun'].astype(int).sum()))
        st.bar_chart(data=temporal, x='game', y='homerun')
    st.write('------')
    st.write("Aggregate Stats")
    st.write(df)
    st.write('------')
    st.write("Temporal Stats")
    st.write(temporal)

if __name__ == "__main__":
    labeler()
