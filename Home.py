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

st.set_page_config(layout="wide")

credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ],
)

client = gspread.authorize(credentials)

@st.cache_resource()
def get_sideBar(title):
    st.sidebar.title(title)
    image = get_image()
    st.image(image)
    st.markdown("## [Click here for Schedule](https://teamsideline.com/sites/georgetown/schedule/450570/2680885/0/Dad-Bod-Bombers)")
    st.markdown("")
    st.markdown('## [Click here for Budget](https://docs.google.com/spreadsheets/d/1AYZyMQNMqUqAaN0m9aw4U5Uc73Vi5PNcn7pKeOcFMOg/edit?usp=sharing)')

def get_project_id():
    return 'dadbod_4_13_23'

@st.cache_resource()
def get_data(project_id):
    sheet = client.open(project_id).sheet1
    dataframe = pd.DataFrame(sheet.get_all_records())
    return dataframe

@st.cache_data()
def get_image():
    image = Image.open('assets/logo.png')
    return image

@st.cache_data()
def get_dadimage_1():
    image = Image.open('assets/dadbod_3_9_23.jpg')
    return image

@st.cache_data()
def manage_dfs(df):
    game1 = pd.read_csv('data/dadbod_3_9_23 - lineup.csv').set_index('id').drop(columns=['name'])
    id_name = pd.read_csv('data/id_name.csv').set_index('id')
    
    game1 = game1.merge(id_name, left_index=True, right_index=True)
    game1.fillna(0, inplace=True)
    game1.replace('', 0, inplace=True)


    game2 = pd.read_csv('data/dadbod_3_30_23 - lineup.csv').set_index('id').drop(columns=['name'])
    
    game2 = game2.merge(id_name, left_index=True, right_index=True)
    game2.fillna(0, inplace=True)
    game2.replace('', 0, inplace=True)


    df = df.set_index('id').drop(columns=['name'])
    df = df.merge(id_name, left_index=True, right_index=True)
    recent_game = df
    recent_game.fillna(0, inplace=True)
    recent_game.replace('', 0, inplace=True)

    game1[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game1[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    game2[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = game2[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)
    
    recent_game[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']] = recent_game[['atbats', 'walks', 'single', 'double', 'triple', 'homerun']].astype(int)


    dfnumsonly = df[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game1numsonly = game1[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    game2numsonly = game2[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi']]
    
    merged_df = dfnumsonly.add(game1numsonly, fill_value=0)
    merged_df = merged_df.add(game2numsonly, fill_value=0)
    merged_df = merged_df.merge(id_name, left_index=True, right_index=True)
    full_set = merged_df.reset_index()
    
    return full_set, game1, game2, recent_game



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

    st.markdown("# Home Page")
    st.markdown("--------")

    with st.sidebar: get_sideBar('Home Page')

    project_id = get_project_id()
    df = get_data(project_id)
    full_set, game1, game2, recent_game = manage_dfs(df)
    df = batting_average(full_set)
    st.markdown("### Team Leaders")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown("#### Singles")
        singles = df.loc[df.single>0].sort_values(by=['single'], ascending=False).head(5)[['name', 'single']]
        st.write(singles)

    with c2:
        st.markdown("#### Doubles")
        doubles = df.loc[df.double>0].sort_values(by=['double'], ascending=False).head(5)[['name', 'double']]
        st.write(doubles)
    with c3:
        st.markdown("#### Triples")
        triples = df.loc[df.triple>0].sort_values(by=['triple'], ascending=False).head(5)[['name', 'triple']]
        st.write(triples)
    with c4:
        st.markdown("#### Homeruns")
        homers = df.loc[df.homerun>0].sort_values(by=['homerun'], ascending=False).head(5)[['name', 'homerun']]
        st.write(homers)

    st.markdown("--------")
    cl1, cl2, cl3, cl4 = st.columns(4)
    with cl1:
        st.markdown("#### Batting Average")
        baframe = df.sort_values(by=['batting_average'], ascending=False).head(5)[['name', 'batting_average']]
        st.write(baframe)
    with cl2:
        st.markdown("#### On Base %")
        onbase = df.sort_values(by=['onbase'], ascending=False).head(5)[['name', 'onbase']]
        st.write(onbase)
    with cl3:
        st.markdown("#### Runs")
        runs = df.sort_values(by=['run'], ascending=False).head(5)[['name', 'run']]
        st.write(runs)
    with cl4:
        st.markdown("#### RBI")
        rbi = df.sort_values(by=['rbi'], ascending=False).head(5)[['name', 'rbi']]
        st.write(rbi)


    st.markdown("-------")
    st.write("### Game 1 - 3/9/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", 21, )
    with col2:
        st.metric('Home', "Dr. Unks", -8)
    with st.expander("See the evidence:"):
        evidence1 = get_dadimage_1()
        st.image(evidence1)
    st.markdown("--------")

    st.write("### Game 2 - 3/30/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Dad Bod Bombers", -15, )
    with col2:
        st.metric('Home', "Team Ramrod", 16)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")

    

    st.write("### Game 3 - 4/13/2023")
    col1, col2 = st.columns(2)
    with col1:
        st.metric('Away', "Mad Lads", 22, )
    with col2:
        st.metric('Home', "Dad Bod Bombers", -11)
    with st.expander("See the evidence:"):
        st.markdown('NO evidence of losses')
    st.markdown("--------")



if __name__ == "__main__":
    labeler()
