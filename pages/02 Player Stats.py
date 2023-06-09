import streamlit as st
import pandas as pd
from PIL import Image

from utils import *

def labeler():

    st.markdown("# Dad Bod Bombers")
    st.markdown("--------")

    df_full, df_full_nums = data_munging()
    df_agg = df_full.groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()

    df = add_cumulative_stats(df_agg)

    with st.sidebar: get_sideBar('Player Stats')

    player = st.selectbox('Select a player', sorted(df_full['name'].unique()))

    game_list = []
    for i in df_full['game'].unique():
        game_df = df_full.loc[(df_full['game']==i) & (df_full['name']==player)]
        game_df_stats = add_cumulative_stats(game_df)
        game_df_stats['game'] = 'Game ' + str(i)
        game_list.append(game_df_stats)
    temporal = pd.concat(game_list)

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
    st.write(df_full.loc[(df_full['name']==player)])

if __name__ == "__main__":
    labeler()
