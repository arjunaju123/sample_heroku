import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

df = pd.read_csv("Kerala_election_2021.csv")

st.markdown(f'<p style="color:#33ff33;font-size:32px;border-radius:1%;">Vote share analysis of major partys in Kerala election 2021</p>', unsafe_allow_html=True)
st.markdown('The .csv file contains the information about votes in each constituency in the 2021 Kerala legislative assembly election. The columns are as follows: ')
st.markdown('Constituency = The name of the specific constituency (geographical area)')
st.markdown('District = The district in which the constituency is located (geographical area)')
st.markdown('LDF = The number of votes obtained by the Left Democratic Front')
st.markdown('UDF = The number of votes obtained by the United Democratic Front')
st.markdown('NDA = The number of votes obtained by the National Democratic Alliance')
st.markdown('NOTA = The number of protest votes (None of the above)')
st.markdown('Others = The number of votes obtained by other parties ')
st.markdown('EVM votes = The number of votes recorded in the electronic voting machine')
st.markdown('Postal votes = The number of postal votes')
st.markdown('Total votes = EVM votes + Postal votes')
st.markdown('Lead = Difference of votes of top candidate vs second best candidate')
st.markdown(' Winner = Name of the winning party (LDF, UDF, NDA, Others)')
st.markdown('%LDF = (LDF votes/Total votes)100')
st.markdown('%UDF = (UDF votes/Total votes)100 ')
st.markdown(' %NDA = (NDA votes/Total votes)100 ')
st.markdown('%NOTA = (NOTA votes/Total votes)100')
st.markdown(' %Postal = (Postal votes/Total votes)100')
st.markdown(' %Lead = (Lead/Total votes)100')


st.title("Kerala legislative assembly election 2021 Dataset")

st.markdown(' 10 Records of the data set is given below:')
st.markdown(f'<p style="color:#33ff33;font-size:24px;border-radius:2%;">10 Records of the data set is given below:</p>', unsafe_allow_html=True)

tab = df.head(10)
st.table(tab)

st.title("The lead of winners in the Legislative assembly of each party is given graphically below:")

sns.swarmplot(x='WINNER', y='LEAD', data=df)
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

st.title(' WINNERS OF THRISSUR DISTRICT')

df1=df.loc[124:136, ['CONSTITUENCY', 'WINNER']]

df1.reset_index(drop=True, inplace=True)

st.table(df1)
