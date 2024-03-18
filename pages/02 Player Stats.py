import streamlit as st
import pandas as pd
from PIL import Image

from utils import *

def labeler():

    st.markdown("# Dad Bod Bombers")
    st.markdown("--------")

    df_full, df_full_nums = data_munging()
    df_agg = df_full.groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()

    big_dict = make_data_dict()


    with st.form('selection'):

        split = st.radio("Select a Player split:", ("All-Time", 'Season 1', 'Season 2', 'Season 3', 'Season 4'))
        player = st.selectbox('Select a player', sorted(df_full['name'].unique()), index=13)
        submit = st.form_submit_button('Select')

    if split == 'All-Time':
        df_agg = big_dict['df_agg_all']
        df_games = big_dict['df_games_all']
        df_full = big_dict['df_full']
        temporal = big_dict['player'][player]['df_full']

    elif split == 'Season 1':
        df_agg = big_dict['df_agg_s1']
        df_games = big_dict['df_games_s1']
        df_full = big_dict['df_s1']
        temporal = big_dict['player'][player]['df_s1']

    elif split == 'Season 2':
        df_agg = big_dict['df_agg_s2']
        df_games = big_dict['df_games_s2']
        df_full = big_dict['df_s2']
        temporal = big_dict['player'][player]['df_s2']

    elif split == 'Season 3':
        df_agg = big_dict['df_agg_s3']
        df_games = big_dict['df_games_s3']
        df_full = big_dict['df_s3']
        temporal = big_dict['player'][player]['df_s3']

    elif split == 'Season 4':
        df_agg = big_dict['df_agg_s4']
        df_games = big_dict['df_games_s4']
        df_full = big_dict['df_s4']
        temporal = big_dict['player'][player]['df_s4']


    df = add_cumulative_stats(df_agg)

    with st.sidebar: get_sideBar('Player Stats')

    df = df[df['name'] == player]

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Player Batting Average:")
        st.markdown("### Overall: " + str(df['batting_average'].astype(int).mean()))
        st.line_chart(data=temporal, x='Game Number', y='batting_average')
        st.markdown('')
        st.markdown('')
        st.markdown('Player Runs Scored:')
        st.markdown("### Overall: " + str(df['run'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='run')
        
        st.markdown('')

        st.markdown('Player Hits:')
        st.markdown("### Overall: " + str(df['hits'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='hits')
        st.markdown('')

        st.markdown("Player On Base Percentage:")
        st.markdown("### Overall: " + str(df['onbase'].astype(int).mean()))
        st.line_chart(data=temporal, x='Game Number', y='onbase')
        st.markdown('')

        st.markdown("Player Slugging Percentage:")
        st.markdown("### Overall: " + str(df['slugging'].astype(int).mean()))
        st.line_chart(data=temporal, x='Game Number', y='slugging')


    with col2:

        st.markdown('Player RBI:')    
        st.markdown("### Overall: " + str(df['rbi'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='rbi')
        st.markdown('')

        st.markdown('Player Singles:')
        st.markdown("### Overall: " + str(df['single'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='single')
        st.markdown('')
        
        st.markdown('Player Doubles:')
        st.markdown("### Overall: " + str(df['double'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='double')
        st.markdown('')


        st.markdown('Player Triples:')
        st.markdown("### Overall: " + str(df['triple'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='triple')
        st.markdown('')

        st.markdown('Player HR:')
        st.markdown("### Overall: " + str(df['homerun'].astype(int).sum()))
        st.bar_chart(data=temporal, x='Game Number', y='homerun')
        
    st.write('------')
    st.write("Aggregate Stats")
    st.write(df)
    st.write('------')
    st.write("Temporal Stats")
    st.write(df_full.loc[(df_full['name']==player)])

if __name__ == "__main__":
    labeler()
