import streamlit as st
import streamlit_analytics
from google.cloud import firestore
import pandas as pd
from PIL import Image

import matplotlib.pyplot as plt
from utils import *
import os

st.set_page_config(layout="wide")
@st.cache_data()
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def labeler():
    get_file_store()
    streamlit_analytics.start_tracking(firestore_key_file='temp_json.json', firestore_collection_name="home")

    st.markdown("# Home Page")
    st.markdown("--------")

    with st.sidebar: get_sideBar('Home Page')

    df_full, df_full_nums = data_munging()
    
    topcol1, topcol2 = st.columns(2)
    with topcol1:
        split = st.radio("Select a Homepage split:", ("All-Time", 'Season 1', 'Season 2', 'Season 3'))
        if split == 'All-Time':
            df_agg = df_full.groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
        elif split == 'Season 1':
            df_agg = df_full.loc[df_full.game <7].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
        elif split == 'Season 2':
            df_agg = df_full.loc[(df_full.game >6) & (df_full.game <15)].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
        elif split == 'Season 3':
            df_agg = df_full.loc[df_full.game >14].groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
    
    with topcol2:
        if split == 'All-Time':
            st.write("")
        elif split == 'Season 1':
            st.write('## :crown: Co-MVP Awards :crown:')
            sub1, sub2 = st.columns(2)
            with sub1:
                st.write("### Ben")
                st.write("* Homerun and Total bases leader.")
                st.write("* Top 5 in 9/10 categories.")
                st.write("* Top 2 in 5/10 categories.")

            with sub2:
                st.write("### Tyler")
                st.write("* Averaged 4 bases per game.")
                st.write("* Top 5 in 9/10 categories.")
                st.write("* Missed the cyle in Game 5 by only a single.")
        elif split == 'Season 2':
            sub1, sub2 = st.columns(2)
            with sub1:
                st.write("### :shield: Defensive MVP :shield:")
                st.write("#### Spangler")
                st.write("* When starting SS, 4 runs given up per game vs 14")
            with sub2:
                st.write("### :hammer: Offensive MVP :hammer:")
                st.write("#### Grace")
                st.write('* Top 5 in 10/10 categories.')
                st.write("* Top 2 in 6/10 categories.")
        elif split == 'Season 3':
            sub1, sub2 = st.columns(2)
            with sub1:
                st.write("### :shield: CyYoung MVP :shield:")
                st.write("#### Frontrunners:")
                st.write("* Cody - Cy young")
            with sub2:
                st.write("### :hammer: Offensive MVP :hammer:")
                st.write('* Sweet - 1000')

    df = add_cumulative_stats(df_agg)

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

    with st.expander('Click here for aggregated stats'):
        st.write(df)

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='agg_data.csv',
            mime='text/csv',
        )

        st.download_button(
            label="Download data as Json",
            data=df.to_json(orient='records', lines=True),
            file_name='agg_data.jsonl',
            mime='application/json',
        )
    with st.expander('Click here for broken down stats'):
        st.write(df_full)

        csv = convert_df(df_full)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='full_data.csv',
            mime='text/csv',
        )

    
    streamlit_analytics.stop_tracking(firestore_key_file='temp_json.json', firestore_collection_name="home")
    delete_file_store()

if __name__ == "__main__":
    labeler()
