import streamlit as st
import pandas as pd
from PIL import Image

import matplotlib.pyplot as plt
from utils import *

st.set_page_config(layout="wide")
@st.cache_data()
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

def labeler():

    st.markdown("# Home Page")
    st.markdown("--------")

    with st.sidebar: get_sideBar('Home Page')

    df_full, df_full_nums = data_munging()
    df_agg = df_full.groupby(['id', 'name'])[['atbats', 'run', 'rbi', 'walks', 'single', 'double', 'triple', 'homerun', 'games_played']].sum().reset_index()
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

    st.markdown('--------')
    st.markdown('\n')
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


if __name__ == "__main__":
    labeler()
