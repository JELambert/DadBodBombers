import streamlit as st
import pandas as pd

from utils import *

def labeler():
    get_file_store()

    st.markdown("# Team Stats")
    st.markdown("--------")


    df_full, df_full_nums = data_munging()

    big_dict = make_data_dict()



    with st.form('selection'):
            
        split = st.radio("Select a Team split:", ("All-Time", 'Season 1', 'Season 2', 'Season 3', 'Season 4'))
        submit = st.form_submit_button('Select')

        if split == 'All-Time':
            df_agg = big_dict['df_agg_all']
            df_games = big_dict['df_games_all']
            df_full = big_dict['df_full']
            temporal = big_dict['temporal_all']

        elif split == 'Season 1':
            df_agg = big_dict['df_agg_s1']
            df_games = big_dict['df_games_s1']
            df_full = big_dict['df_s1']
            temporal = big_dict['temporal_s1']

        elif split == 'Season 2':
            df_agg = big_dict['df_agg_s2']
            df_games = big_dict['df_games_s2']
            df_full = big_dict['df_s2']
            temporal = big_dict['temporal_s2']

        elif split == 'Season 3':
            df_agg = big_dict['df_agg_s3']
            df_games = big_dict['df_games_s3']
            df_full = big_dict['df_s3']
            temporal = big_dict['temporal_s3']

        elif split == 'Season 4':
            df_agg = big_dict['df_agg_s4']
            df_games = big_dict['df_games_s4']
            df_full = big_dict['df_s4']
            temporal = big_dict['temporal_s4']

    df = add_cumulative_stats(df_games)

    with st.sidebar: get_sideBar('Team Stats')

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Team Batting Average:")
        st.markdown('')
        st.markdown("### Average: " + str(df['batting_average'].astype(int).mean().round(0)))
        st.line_chart(temporal.groupby('Game Number')['batting_average'].mean().reset_index(), x='Game Number', y='batting_average')
        st.markdown('')
        st.markdown('Team Runs Scored:')
        st.write("### Overall: " + str(df['run'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['run'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['run'].sum().reset_index(), x='Game Number', y='run')
        st.markdown('')

        st.markdown('Team Hits:')
        st.write("### Overall: " + str(df['hits'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['hits'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['hits'].sum().reset_index(), x='Game Number', y='hits')

        st.markdown('')

        st.markdown("Team On Base Percentage:")
        st.write("### Average: " + str(df['onbase'].astype(int).mean().round(0)))
        st.line_chart(temporal.groupby('Game Number')['onbase'].mean().reset_index(), x='Game Number', y='onbase')
        
        st.markdown('')

        st.markdown("Team Slugging Percentage:")
        st.write("### Average: " + str(df['slugging'].astype(int).mean().round(0)))
        st.line_chart(temporal.groupby('Game Number')['slugging'].mean().reset_index(), x='Game Number', y='slugging')

    with col2:
        st.markdown('Team RBI:')    
        st.write("### Overall: " + str(df['rbi'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['rbi'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['rbi'].sum().reset_index(), x='Game Number', y='rbi')

        st.markdown('')

        st.markdown('Team HR:')
        st.write("### Overall: " + str(df['homerun'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['homerun'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['homerun'].sum().reset_index(), x='Game Number', y='homerun')

        st.markdown('')

        st.markdown('Team Triples:')
        st.write("### Overall: " + str(df['triple'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['triple'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['triple'].sum().reset_index(), x='Game Number', y='triple')

        st.markdown('')

        st.markdown('Team Doubles:')
        st.write("### Overall: " + str(df['double'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['double'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['double'].sum().reset_index(), x='Game Number', y='double')

        st.markdown('')

        st.markdown('Team Singles:')
        st.write("### Overall: " + str(df['single'].astype(int).sum().round(0)))
        st.write("### Average: " + str(df['single'].astype(int).mean().round(0)))
        st.bar_chart(temporal.groupby('Game Number')['single'].sum().reset_index(), x='Game Number', y='single')
    

if __name__ == "__main__":
    labeler()
