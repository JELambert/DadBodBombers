import streamlit as st
import pandas as pd

from Home import get_sideBar, get_data, get_project_id
from utils import *

def labeler():

    st.markdown("# Team Stats")
    st.markdown("--------")



    df_full, df_full_nums = data_munging()
    df_agg = df_full.groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    df_games = df_full.groupby(['game'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    df = add_cumulative_stats(df_games)

    game_list = []
    for i in df_full['game'].unique():
        game_df = df_full.loc[df_full['game']==i]
        game_df_stats = add_cumulative_stats(game_df)
        game_df_stats['game'] = 'Game ' + str(i)
        game_list.append(game_df_stats)
    temporal = pd.concat(game_list)
    
    with st.sidebar: get_sideBar('Team Stats')

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Team Batting Average:")
        st.markdown('')
        st.markdown("### Average: " + str(df['batting_average'].astype(int).mean().round(2)))
        st.line_chart(temporal.groupby('game')['batting_average'].mean().reset_index(), x='game', y='batting_average')
        st.markdown('')
        st.markdown('Team Runs Scored:')
        st.write("### Overall: " + str(df['run'].astype(int).sum()))
        st.write("### Average: " + str(df['run'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['run'].sum().reset_index(), x='game', y='run')
        st.markdown('')

        st.markdown('Team Hits:')
        st.write("### Overall: " + str(df['hits'].astype(int).sum()))
        st.write("### Average: " + str(df['hits'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['hits'].sum().reset_index(), x='game', y='hits')

        st.markdown('')

        st.markdown("Team On Base Percentage:")
        st.write("### Average: " + str(df['onbase'].astype(int).mean()))
        st.line_chart(temporal.groupby('game')['onbase'].mean().reset_index(), x='game', y='onbase')
        
        st.markdown('')

        st.markdown("Team Slugging Percentage:")
        st.write("### Average: " + str(df['slugging'].astype(int).mean()))
        st.line_chart(temporal.groupby('game')['slugging'].mean().reset_index(), x='game', y='slugging')

    with col2:
        st.markdown('Team RBI:')    
        st.write("### Overall: " + str(df['rbi'].astype(int).sum()))
        st.write("### Average: " + str(df['rbi'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['rbi'].sum().reset_index(), x='game', y='rbi')

        st.markdown('')

        st.markdown('Team HR:')
        st.write("### Overall: " + str(df['homerun'].astype(int).sum()))
        st.write("### Average: " + str(df['homerun'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['homerun'].sum().reset_index(), x='game', y='homerun')

        st.markdown('')

        st.markdown('Team Triples:')
        st.write("### Overall: " + str(df['triple'].astype(int).sum()))
        st.write("### Average: " + str(df['triple'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['triple'].sum().reset_index(), x='game', y='triple')

        st.markdown('')

        st.markdown('Team Doubles:')
        st.write("### Overall: " + str(df['double'].astype(int).sum()))
        st.write("### Average: " + str(df['double'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['double'].sum().reset_index(), x='game', y='double')

        st.markdown('')

        st.markdown('Team Singles:')
        st.write("### Overall: " + str(df['single'].astype(int).sum()))
        st.write("### Average: " + str(df['single'].astype(int).mean()))
        st.bar_chart(temporal.groupby('game')['single'].sum().reset_index(), x='game', y='single')

if __name__ == "__main__":
    labeler()
