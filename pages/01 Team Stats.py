import streamlit as st
import pandas as pd
import os
import random
import datetime
import json

from Home import get_sideBar, get_data, get_project_id

st.set_page_config(layout="wide")

@st.cache_data()
def batting_average(df):
    df.fillna(0, inplace=True)
    df.replace('', 0, inplace=True)
    df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = df[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    df['batting_average'] = (df['single'] + df['double'] + df['triple'] + df['homerun'])  / (df['atbats'] - df['walks']) * (1000)
    df['hits'] = df['single'] + df['double'] + df['triple'] + df['homerun']
    df['onbase'] = (df['hits'] + df['walks']) / df['atbats'] * (1000)
    df['slugging'] = (df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])) / df['atbats'] * (1000)
    df['onbase_plus_slugging'] = df['onbase'] + df['slugging']
    df['total_bases'] = df['single'] + (2 * df['double']) + (3 * df['triple']) + (4 * df['homerun'])

    return df

def labeler():

    st.markdown("# Team Stats")
    st.markdown("--------")

    project_id = get_project_id()
    df = get_data(project_id)
     
    with st.sidebar: get_sideBar('Team Stats')

    df = batting_average(df)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Team Batting Average:")
        st.write(df['batting_average'].astype(int).mean())
        
        st.markdown('')
        st.markdown('Team Runs Scored:')
        st.write(df['run'].astype(int).sum())
        
        st.markdown('')

        st.markdown('Team Hits:')
        st.write(df['hits'].astype(int).sum())

        st.markdown('')

        st.markdown("Team On Base Percentage:")
        st.write(df['onbase'].astype(int).mean())
        
        st.markdown('')

        st.markdown("Team Slugging Percentage:")
        st.write(df['slugging'].astype(int).mean())
    with col2:

        st.markdown('Team RBI:')    
        st.write(df['rbi'].astype(int).sum())

        st.markdown('')

        st.markdown('Team HR:')
        st.write(df['homerun'].astype(int).sum())

        st.markdown('')

        st.markdown('Team Triples:')
        st.write(df['triple'].astype(int).sum())

        st.markdown('')

        st.markdown('Team Doubles:')
        st.write(df['double'].astype(int).sum())

        st.markdown('')

        st.markdown('Team Singles:')
        st.write(df['single'].astype(int).sum())

if __name__ == "__main__":
    labeler()
