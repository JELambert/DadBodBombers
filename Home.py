import streamlit as st
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

    st.markdown("# Home Page")
    st.markdown("--------")

    with st.sidebar: get_sideBar('Home Page')


    big_dict = make_data_dict()



    with st.form('selection'):
        

        topcol1, topcol2 = st.columns(2)
        with topcol1:
            split = st.radio("Select a Homepage split:", ("All-Time", 'Season 1', 'Season 2', 'Season 3', 'Season 4', 'Season 5'))
            submit = st.form_submit_button('Select')

            if split == 'All-Time':
                df_agg = big_dict['df_agg_all']
                df = big_dict['df_cumulative_all']
            elif split == 'Season 1':
                df_agg = big_dict['df_agg_s1']
                df = big_dict['df_cumulative_s1']
            elif split == 'Season 2':
                df_agg = big_dict['df_agg_s2']
                df = big_dict['df_cumulative_s2']
            elif split == 'Season 3':
                df_agg = big_dict['df_agg_s3']
                df = big_dict['df_cumulative_s3']
            elif split == 'Season 4':
                df_agg = big_dict['df_agg_s4']
                df = big_dict['df_cumulative_s4']
            elif split == 'Season 5':
                df_agg = big_dict['df_agg_s5']
                df = big_dict['df_cumulative_s5']

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
                    st.write("#### Cody - Cy young")
                    st.write("* From 13 runs given up per game to 9")
                    st.write("* Multiple strikeouts...in slow pitch softball")
                with sub2:
                    st.write("### :hammer: Offensive MVP :hammer:")
                    st.write('#### Sweet - 1000')
                    st.write("* The man got on base 13 straight times.")

            elif split == 'Season 4':
                sub1, sub2 = st.columns(2)
                with sub1:
                    st.write("### MVP Offense - Spangler")
                with sub2:
                    st.write("### MVP Defense - Gump")

            elif split == 'Season 5':
                sub1, sub2 = st.columns(2)
                with sub1:
                    st.write("### MVP - Ryan")
                    st.write("* Two walk offs...nuff said")
                with sub2:
                    st.write("### Rookie of the year - Clint")
                    st.write("* Major moves in batting order in sight.")


    st.markdown("### Team Leaders")

    c1, c2, c3, c4, c5 = st.columns(5)
    with c1:
        st.markdown("#### Singles")
        singles = df.loc[df.single>0].sort_values(by=['single'], ascending=False).head(5)[['name', 'single']]
        
        # ar_all = []
        # for player in singles['name'].unique()[:5]:
        #     ar_all.append(make_cumulative_array(player, df_all, 'single'))
        # singles['array'] = ar_all
        # col_config(singles, 'hits')

        st.dataframe(singles, hide_index=True)

    with c2:
        st.markdown("#### Doubles")
        doubles = df.loc[df.double>0].sort_values(by=['double'], ascending=False).head(5)[['name', 'double']]
        st.dataframe(doubles, hide_index=True)

    with c3:
        st.markdown("#### Triples")
        triples = df.loc[df.triple>0].sort_values(by=['triple'], ascending=False).head(5)[['name', 'triple']]
        st.dataframe(triples, hide_index=True)

    with c4:
        st.markdown("#### Homeruns")
        homers = df.loc[df.homerun>0].sort_values(by=['homerun'], ascending=False).head(5)[['name', 'homerun']]
        st.dataframe(homers, hide_index=True)

    with c5:
        st.markdown("#### Total Bases")
        total_bases = df.loc[df.total_bases>0].sort_values(by=['total_bases'], ascending=False).head(5)[['name', 'total_bases']]
        st.dataframe(total_bases, hide_index=True)

    st.markdown("--------")
    cl1, cl2, cl3, cl4, cl5 = st.columns(5)
    with cl1:
        st.markdown("#### Batting Average")
        baframe = df.sort_values(by=['batting_average'], ascending=False).head(5)[['name', 'batting_average']]
        st.dataframe(baframe, hide_index=True)

    with cl2:
        st.markdown("#### On Base %")
        onbase = df.sort_values(by=['onbase'], ascending=False).head(5)[['name', 'onbase']]
        st.dataframe(onbase, hide_index=True)

    with cl3:
        st.markdown("#### Slugging %")
        slugging = df.sort_values(by=['slugging'], ascending=False).head(5)[['name', 'slugging']]
        st.dataframe(slugging, hide_index=True)

    with cl4:
        st.markdown("#### Runs")
        runs = df.sort_values(by=['run'], ascending=False).head(5)[['name', 'run']]
        st.dataframe(runs, hide_index=True)

    with cl5:
        st.markdown("#### RBI")
        rbi = df.sort_values(by=['rbi'], ascending=False).head(5)[['name', 'rbi']]
        st.dataframe(rbi, hide_index=True)


    st.markdown("--------")
    st.markdown("## Defensive Performance Index (DPI)")

    st.bar_chart(big_dict['fielding']['overall']['aggregate'].sort_values(by='DPI', ascending=False), x='name', y='DPI')


    st.markdown('''
                Defensive Performance Index is a defensive metric that combines:
                * Errors
                * Outs Caught
                * Outs Caught Hard
                * Outs Thrown
                * Outs Thrown Hard
                * Range Missed (Player unable to get to ball given range)
                * Positional difficulty
                ''')
    st.markdown("")
    with st.expander("For algorithm:"):
        st.markdown('''
                    def build_raw_defense_totals(x):
                        position_config = {'1B': 3, 
                        '2B': 3, 
                        '3B': 4, 
                        'SS': 5, 
                        'LF': 4, 
                        'LC': 4, 
                        'RC': 4,
                        'RF': 3, 
                        'P': 3, 
                        'C': 2}
    return 
((x['E'] *-2 / position_config[x['Positions']]) + 
(x['OC']*position_config[x['Positions']]) + 
(x['OCH'] * 2 * position_config[x['Positions']]) + 
(x['OT']*position_config[x['Positions']]) + 
(x['OTH']*2 * position_config[x['Positions']]) + 
(x['RM']*-1 /position_config[x['Positions']]))")
                    ''')

    with st.expander("## See full defensive stats:"):
        st.write(big_dict['fielding']['overall']['disaggregate'])

    with st.expander("Explainer of raw stats:"):
        st.markdown('''
Error- A defensive mistake made by a player that allows an opposing batter or baserunner to advance safely
Error hard- An error that would be difficult for anyone to make a play 
Out caught- A defensive play on a ball that was thrown, or hit by the batter to a player that results in an out. 
Out caught hard- A ball that is thrown or hit towards a player that would’ve been difficult for them to make a play on the ball. 
Out thrown- If a player has the ball and they throw to a bag that a runner isn’t on or has reached and it results in an out. 
Out thrown hard- If a player has the ball and the throw to get the out is not an easy throw to make but they deliver a good throw for their teammate to catch it for a possible out. 
Range miss- If the ball is hit near a player but its just outside of your possible area that you wouldn’t be able to reach. ''')

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
        st.write(big_dict['df_full'])

        csv = convert_df(big_dict['df_full'])

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='full_data.csv',
            mime='text/csv',
        )

    # ar_all = []

    # for player in singles['name'].unique()[:5]:
    #     ar_all.append(make_cumulative_array(player, df_full, 'single'))

    # col_config(newonbase, 'hits')



    # st.dataframe(
    #     df,
    #     column_config={
    #         "name": "App name",
    #         "stars": st.column_config.NumberColumn(
    #             "Github Stars",
    #             help="Number of stars on GitHub",
    #             format="%d ⭐",
    #         ),
    #         "url": st.column_config.LinkColumn("App URL"),
    #         "views_history": st.column_config.LineChartColumn(
    #             "Views (past 30 days)", y_min=0, y_max=5
    #         ),
    #     },
    #     hide_index=True,
    # )

# def col_config(df, colname):
#     mapping = {'hits': {'format': "Hits", 'y_min': 0, 'y_max': 5},
#                'singles': {'format': "Singles", 'y_min': 0, 'y_max': 5},
#     }

#     return st.dataframe(
#         df,
#         column_config={
#             "name": "Player",
#             colname: st.column_config.NumberColumn(
#                 mapping[colname]['format'],
#             ),
#             "array": st.column_config.LineChartColumn(
#                 "", y_min=mapping[colname]['y_min'], y_max=mapping[colname]['y_max']
#             ),
#         },
#         hide_index=True,
#     )


    #streamlit_analytics.stop_tracking(firestore_key_file='temp_json.json', firestore_collection_name="home")
    #delete_file_store()


# def make_temp_array(player, df_full, category):
#     game_list = []
#     for i in df_full['game'].unique():
#         game_df = df_full.loc[(df_full['game']==i) & (df_full['name']==player)]
#         game_df_stats = add_cumulative_stats(game_df)
#         game_df_stats['game'] = 'Game ' + str(i)
#         game_list.append(game_df_stats)
#     temporal = pd.concat(game_list)
#     temporal['Game Number'] = temporal['game'].str.split(' ').str[1].astype(int)
#     temporal = temporal.sort_values(by='Game Number')

#     df_sorted = temporal.sort_values(by='game')
#     hits_array = df_sorted['hits'].to_numpy()
#     return hits_array

if __name__ == "__main__":
    labeler()
