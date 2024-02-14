import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime as dt

st.title('podio shoutouts and chats')
shoutouts = [
    {
    'type':'shoutout',
    'colleague':'WRE',
    'timestamp':dt(2024,2,12,17,21,00),
    'item':"automation project",
    'link':'https://podio.com/evologic-technologiescom/corefacility/apps/projects/items/13',
    'text': """i printed out what is linked in the notes section. The notes section and the diagram for the "level above the tech stack" is the next topic from my side.""",
    'answered': None,#dt(2024,12,31,00,00,00),
    },
    {
    'type': 'chat',
    'colleague': 'MBR',
    'timestamp': dt(2024,2,13,7,46,00),
    'text': """the goal mentions "our key capabilities" would a more granular breakdown of these be available?""",
    'answered': dt(2024,2,13,8,52,00),
    },
    {
    'type':'shoutout',
    'colleague': 'WRE',
    'timestamp': dt(2024,2,13,8,10,00),
    'item': 'WRE prios', 
    'link':'',
    'text': """i'm curious how you DISTINGUISH between "DIY" and "ready-to-use". How would you classify the "weidmuller fieldbus coupler"? The Dasgip modules?""",
    'answered': None, #dt(2024,12,31,00,00,00)
    },
    {
    'type':'shoutout',
    'colleague': 'WRE',
    'timestamp': dt(2024,2,13,14,20,00),
    'item': 'WRE prios', 
    'link':'',
    'text': """is building software part of the solution to the data standardization topic?""",
    'answered': dt(2024,2,14,21,34,00)
    },
    {
    'type':'',
    'colleague': None,
    'timestamp': None, #dt(2024,12,31,00,00,00),
    'text': """""",
    'answered': None #dt(2024,12,31,00,00,00)
    },
]

df = pd.DataFrame(shoutouts)
df.insert(0, 'time_since', dt.now()-df['timestamp'])
df.insert(0, 'time_answered', df['answered']-df['timestamp'])

df.sort_values('time_since', ascending=False, inplace=True)
df=df[['type','time_answered','time_since','colleague','item','text']]

st.dataframe(data=df, hide_index=True)