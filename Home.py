import streamlit as st
import pandas as pd
import os
import random
import datetime
import json
from PIL import Image


import matplotlib.pyplot as plt

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
    st.markdown("## [Click here for Schedule](https://www.teamsideline.com/sites/georgetown/schedule/476652/Thursday-Mens-Recreational-League)")
    st.markdown("")
    st.markdown('## [Click here for Budget](https://docs.google.com/spreadsheets/d/1AYZyMQNMqUqAaN0m9aw4U5Uc73Vi5PNcn7pKeOcFMOg/edit?usp=sharing)')

def get_project_id():
    return 'dadbod_4_27_23'

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
    


    game1numsonly = game1[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]
    game2numsonly = game2[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]
    game3numsonly = game3[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]
    game4numsonly = game4[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]
    game5numsonly = game5[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]
    game6numsonly = game6[[ 'atbats', 'walks', 'single', 'double', 'triple', 'homerun', 'run', 'rbi', 'games_played']]

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

    st.markdown("# Home Page")
    st.markdown("--------")

    with st.sidebar: get_sideBar('Home Page')

    project_id = get_project_id()
    df = get_data(project_id)
    full_set, game1, game2, game3, game4, game5, game6 = manage_dfs(df, recent=False)

    df = batting_average(full_set)

    st.markdown("### End of Season Feedback")
    
    feed = pd.read_excel('data/Spring23 Survey (Responses).xlsx')
    feed = feed[['Overall Vibes', 'Coaching quality', 'Did you agree with the lineups?', 'Did you agree with where you played in the field?']]

    col1, col2 = st.columns(2)
    with col1:
        st.metric('0=Bad, 10=Best', "Overall Team Vibes", feed['Overall Vibes'].mean(), )
        #feed['Did you agree with the lineups?'].value_counts().plot(kind='barh')
        st.markdown('----------')

        category_counts = feed['Did you agree with the lineups?'].value_counts()
        st.markdown('#### Did you agree with the lineups?')
        # Plot the pie chart
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the chart using Streamlit
        st.pyplot(fig)
        #st.pyplot(feed['Did you agree with where you played in the field?'].value_counts().plot(kind='barh'))
    with col2:
        st.metric('0=Bad, 10=Best', "Coaching Quality", feed['Coaching quality'].mean(), )
        st.markdown('----------')


        category_counts = feed['Did you agree with where you played in the field?'].value_counts()
        st.markdown('#### Did you agree with where you played in the field?')
        # Plot the pie chart
        fig, ax = plt.subplots(figsize=(6,6))
        ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Display the chart using Streamlit
        st.pyplot(fig)


    st.markdown('----------')
    st.markdown("#### Open response feedback")
    openresponse = Image.open('assets/wordcloud.png')

    st.image(openresponse)

    st.markdown('----------')


    st.markdown("### Team Leaders")

    c1, c2, c3, c4, c5 = st.columns(5)
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
    with c5:
        st.markdown("#### Total Bases")
        total_bases = df.loc[df.total_bases>0].sort_values(by=['total_bases'], ascending=False).head(5)[['name', 'total_bases']]
        st.write(total_bases)

    st.markdown("--------")
    cl1, cl2, cl3, cl4, cl5 = st.columns(5)
    with cl1:
        st.markdown("#### Batting Average")
        baframe = df.sort_values(by=['batting_average'], ascending=False).head(5)[['name', 'batting_average']]
        st.write(baframe)
    with cl2:
        st.markdown("#### On Base %")
        onbase = df.sort_values(by=['onbase'], ascending=False).head(5)[['name', 'onbase']]
        st.write(onbase)
    with cl3:
        st.markdown("#### Slugging %")
        slugging = df.sort_values(by=['slugging'], ascending=False).head(5)[['name', 'slugging']]
        st.write(slugging)
    with cl4:
        st.markdown("#### Runs")
        runs = df.sort_values(by=['run'], ascending=False).head(5)[['name', 'run']]
        st.write(runs)
    with cl5:
        st.markdown("#### RBI")
        rbi = df.sort_values(by=['rbi'], ascending=False).head(5)[['name', 'rbi']]
        st.write(rbi)

    st.markdown('--------')
    st.markdown("## See the full stats sheet:")

    with st.expander('click here'):
        st.write(df)


if __name__ == "__main__":
    labeler()
