import streamlit as st
import pandas as pd
import plotly.express as px
data = pd.read_csv("dataset.csv")
st.header('SDT Project')

for artist in data['artists']:
    print(artist)

artist_counts = data['artists'].value_counts().reset_index()
artist_counts.columns = ['artists', 'count']
top_artists = artist_counts.head(20)['artists'].tolist()

show_top_artists = st.checkbox('Show only Top 20 artists')
if show_top_artists:
    data = data[data['artists'].isin(top_artists)]
    st.write("Top Artists:", top_artists)

fig = px.histogram(
    top_artists,
    x='artists',
    y='count',
    labels={'artists': 'Artist', 'count': 'Frequency of Artists'},
    title='Top Artists'
)
st.plotly_chart(fig)

fig_1 = px.scatter(
    top_artists,
    x='artists',
    y='count',
    labels={'artists': 'Artist', 'count': 'Number of Occurrences'},
    title='Frequency of Artists'
)
st.plotly_chart(fig_1)

data_filtered = data[data['popularity'] !=0]
popular_counts = data_filtered[['popularity', 'track_name']].value_counts().reset_index()
popular_counts.columns = ['popularity','track_name', 'count']

# Sort and take only the top 20 songs
popular_songs = popular_counts.head(20)['popularity'].tolist()

show_popular_songs = st.checkbox('Show only Popular Songs')
if show_popular_songs:
    data = data[data['track_name'].isin(popular_songs)]
    st.write("Popular Songs:", popular_songs)

# Create the histogram
fig_2 = px.histogram(
    popular_songs,
    x='track_name',
    y='count',
    labels={'track_name': 'Track Name', 'count': 'Popularity of Track'},
    title='Popularity of a Track'
)
fig_2.update_layout(xaxis_tickangle=-45)
fig_2.update_yaxes(range=[0, 50])

# Display the plot
st.plotly_chart(fig_2)

fig_3 = px.scatter(
    popular_songs,
    x='track_name',
    y='count',
    labels={'track_name': 'Track Name', 'count': 'Popularity of Track'},
    title='Popularity of a Track'
)
fig_3.update_layout(xaxis_tickangle=-45)
fig_3.update_yaxes(range=[0, 30])
st.plotly_chart(fig_3)
